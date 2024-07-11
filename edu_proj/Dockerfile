# Використовуємо базовий образ Python
FROM python:3.12-slim

# Встановлюємо системні залежності
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли проекту в контейнер
COPY . /app/example

# Копіюємо requirements.txt та встановлюємо залежності Python
# COPY example/requirements.txt /app/example/requirements.txt
RUN pip install --no-cache-dir -r /app/example/requirements.txt

# Встановлюємо робочий каталог
WORKDIR /app/example

# Використовуємо порт 9000 для сервера Django
EXPOSE 8000
