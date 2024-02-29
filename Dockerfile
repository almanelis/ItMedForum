# используем python 3.11
FROM python:3.11-alpine

# создаём директорию для проекта
WORKDIR /med_it_forum

# устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем проект
COPY . .