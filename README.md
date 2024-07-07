# Nice Django CRUD

The purpose of this project is to demonstrate how to create a nice Django CRUD with minimal amount of code.

The project uses `django-tables2`, `django-filter`, `django-crispy-forms`, `crispy-bootstrap5` and `django-select2`
libraries.

## How to create and activate the python environment

Execute:
```commandline
poetry install
poetry shell
```

## How to run the application locally

Start database:
```commandline
make db-start
```
Execute migrations:
```commandline
python manage.py migrate
```
Populate database with test data:
```commandline
python manage.py populate
```
Start server:
```commandline
python manage.py runserver
```

To stop the database, execute:
```commandline
make db-stop
```

## How to run tests
Start database:
```commandline
make db-start
```
Launch tests:
```commandline
pytest
```
