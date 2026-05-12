FastAPI Task Manager

Простий REST API для керування задачами, створений за допомогою FastAPI.

Можливості
Створення задач
Отримання списку задач
Оновлення задач
Видалення задач
Swagger документація
Робота з базою даних через SQLAlchemy

Встановлення
Клонувати репозиторій:
git clone https://github.com/oprymenk/fastapi-task-manager.git

Перейти в папку проєкту:
cd fastapi-task-manager

Створити та активувати віртуальне середовище:
python -m venv venv

Windows
venv\Scripts\activate

Linux / MacOS
source venv/bin/activate

Встановити залежності:
pip install -r requirements.txt

Запуск
uvicorn app.main:app --reload

API буде доступне за адресою:
http://127.0.0.1:8000

Документація API
Swagger UI:
http://127.0.0.1:8000/docs
