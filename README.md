# Homework_07

Цей проєкт включає в себе роботу з базою даних PostgreSQL, використання Alembic для міграцій, заповнення бази даних випадковими даними за допомогою Faker та написання запитів до бази даних з використанням SQLAlchemy.

## Встановлення

1. Клонуйте репозиторій: `git clone https://github.com/Homework_07.git`
2. Перейдіть до папки проекту: `cd Homework_07`
3. Встановіть залежності: `pip install -r requirements.txt`

## Використання

1. Перед початком використання проекту переконайтеся, що у вас встановлені всі необхідні залежності. Виконайте наступну команду в терміналі для встановлення залежностей з файлу requirements.txt:

pip install -r requirements.txt


2. Створіть файли міграцій для бази даних та оновіть її до поточної версії. Використайте Alembic для цього:

alembic revision --autogenerate -m "Створення таблиць"
alembic upgrade head


3. Запустіть скрипт seed.py, щоб заповнити базу даних випадковими даними:

python seed.py


## Ліцензія

Цей проект ліцензований під [Ліцензією MIT](https://opensource.org/licenses/MIT).

