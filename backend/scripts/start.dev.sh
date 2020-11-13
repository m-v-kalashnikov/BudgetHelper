#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
python manage.py create_custom_super_user
python manage.py change_site_credentials
python manage.py create_user_fixtures --runs=15
python manage.py runserver 0.0.0.0:8000
