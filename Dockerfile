# 1. Вказуємо базовий образ з Python
FROM python:3.12-slim

# 2. Встановлюємо змінну оточення
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Створюємо робочу директорію в контейнері
WORKDIR /app

# 4. Копіюємо файли проєкту в контейнер
COPY . /app/

# 5. Встановлюємо pip та залежності
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Команда запуску сервера за замовчуванням
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]