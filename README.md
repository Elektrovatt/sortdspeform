<h2 align="center">Forms for DSP</h2>

### Описание проекта:
Формы для заполения операторами


### Инструменты разработки

**Стек:**
- Python = 3.8
- Django = 3.2
- PostgreSQL

## Разработка

##### 1) Сделать форк репозитория 

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) Создать виртуальное окружение

    python -m venv venv
    
##### 4) Активировать виртуальное окружение

##### 5) Устанавливить зависимости:

    pip install -r requirements.txt

##### 6) Создайте базу данных postgres и добавьте учетные данные в settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

##### 7) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 8) Создать суперпользователя

    python manage.py createsuperuser
    
##### 9) Запустить сервер

    python manage.py runserver
