#!/bin/sh

export DJANGO_SETTINGS_MODULE=api_yamdb.settings

python manage.py migrate --noinput

python manage.py collectstatic --noinput

python manage.py load_data

gunicorn --bind 0:8000 api_yamdb.wsgi:application
