import numpy as np
import pandas as pd
import keras
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
from os.path import join, exists, abspath, dirname

active_model_name = 'tz' # name of the active model
model_names = []
model = None
tokenizer = None
label_encoder = None
max_length = 0
path = '..\\model_training\\models'
is_ready = False
filesForSave = ['model.keras', 'tokenizer.pickle', 'label_encoder.pickle', 'max_length.pickle']

def init(model_name):
    global model, tokenizer, label_encoder, max_length, path, is_ready, active_model_name
    active_model_name = model_name

    for filename in filesForSave:
        if not exists(join(path, active_model_name, filename)):
            is_ready = _train(active_model_name)
            return is_ready

    model = keras.saving.load_model(join(path, active_model_name, filesForSave[0]))
    with open(join(path, active_model_name, filesForSave[1]), 'rb') as file:
        tokenizer = pickle.load(file)
    with open(join(path, active_model_name, filesForSave[2]), 'rb') as file:
        label_encoder = pickle.load(file)
    with open(join(path, active_model_name, filesForSave[3]), 'rb') as file:
        max_length = pickle.load(file)

    is_ready = True
    print('initializing complated!')
    return is_ready


def _train(model_name):
    global model, tokenizer, label_encoder, max_length, path, is_ready
    if not model_name in model_names: return False
    if model_name == 'tz':
        df = pd.read_csv(join(path, model_name, 'dataset.сsv'), names=['Text', 'Emotions'], sep=';')
    elif model_name == 'another model':
        df = pd.read_csv(join(path, model_name, 'dataset.csv'), names=['ind', 'Text', 'Emotions'], sep=',')
    else:
        try:
            df = pd.read_csv(join(path, model_name, 'dataset.csv'), names=['Text', 'Emotions'], sep=',')
        except:
            print(f'dataset file not found ({model_name})')
            return False

    labels = df['Emotions'].tolist()
    texts = df['Text'].tolist()

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(texts)

    sequences = tokenizer.texts_to_sequences(texts)
    max_length = max([len(seq) for seq in sequences])
    padded_sequences = pad_sequences(sequences,maxlen = max_length)

    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)

    one_hot_labels = keras.utils.to_categorical(labels)
    xtrain, xtest, ytrain, ytest = train_test_split(padded_sequences,one_hot_labels,test_size=0.2)

    model = Sequential()
    model.add(Embedding(input_dim=len(tokenizer.word_index) + 1,
                        output_dim=128, input_length=max_length))
    model.add(Flatten())
    model.add(Dense(units=128, activation="relu"))
    model.add(Dense(units=len(one_hot_labels[0]), activation="softmax"))

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    model.fit(xtrain, ytrain, epochs=20, batch_size=32, validation_data=(xtest, ytest))

    model.save(join(path, model_name, filesForSave[0]))

    with open(join(path, model_name, filesForSave[1]), 'wb') as file:
        pickle.dump(tokenizer, file, protocol=pickle.HIGHEST_PROTOCOL)

    with open(join(path, model_name, filesForSave[2]), 'wb') as file:
        pickle.dump(label_encoder, file, protocol=pickle.HIGHEST_PROTOCOL)

    with open(join(path, model_name, filesForSave[3]), 'wb') as file:
        pickle.dump(max_length, file, protocol=pickle.HIGHEST_PROTOCOL)
    print('training complated!')
    return True

def analyse(input_text):
    global model, tokenizer, label_encoder, max_length
    if not is_ready:    return 'not ready model!'
    input_sequence = tokenizer.texts_to_sequences([input_text])
    padded_input_sequence = pad_sequences(input_sequence, maxlen=max_length)
    prediction = model.predict(padded_input_sequence)
    return label_encoder.inverse_transform([np.argmax(prediction[0])])[0]