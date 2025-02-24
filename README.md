# Telegram NLP Analyzer
# 0_o

## Описание проекта

**Telegram NLP Analyzer** - это инструмент для анализа текстовых сообщений в Telegram чатах с использованием методов обработки естественного языка (NLP). Проект позволяет извлекать полезную информацию из сообщений, такую как ключевые слова, тональность текста, и другие лингвистические характеристики.

## Основные возможности

- Подключение к Telegram API для получения сообщений из выбранных чатов
- Предобработка текста (токенизация, лемматизация, удаление стоп-слов)
- Анализ тональности сообщений
- Извлечение ключевых слов и фраз
- Визуализация результатов анализа

## Требования

- Python 3.7+
- Telegram API ключ
- Необходимые библиотеки (список в `requirements.txt`)

## Установка

### 1. Клонируйте репозиторий:
```sh
git clone https://github.com/your-username/tg_nlp_analyzer.git
cd tg_nlp_analyzer
```
### 2. Создайте виртуальное окружение и активируйте его:
```sh
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
```
### 3. Установите зависимости:
```sh
pip install -r requirements.txt
```
## Использование

### 1. Скачайте обученые модели по ссылкам:
  Яндекс Диск => https://mega.nz/file/g70zXQYR#INQ92EtaqrzhyrKzGJhhMPmxFaMzPi3er4iIqIrqULM
  Мега => https://disk.yandex.ru/d/428laQ7XmKT0CQ

### 2. Разорхивируйте __models.zip__ в __model_training__

### 3. В скрипте __main__ укажите свой токен в переменную __TOKEN__

### 4. Запустите основной скрипт:
```sh
python main.py
```
