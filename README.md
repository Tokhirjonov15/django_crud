Install pipenv & create Virtual Environment:

  -  python -m pipenv shell
  -  python -m pipenv --python 3.11
  -  pipenv install
  -  python -m pipenv install django==4.2

Install Project and Applications:

  - django-admin startproject crud_django .
  - python manage.py startapp app_name

Migrate Database:
  
  - python manage.py migrate

Run Project via activated venv:

  - python manage.py runserver


