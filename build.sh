#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
python manage.py createsuperuser --noinput --rol 0 --phone 'empty' --adress 'emtpy' --employeeNumber 'empty' --schedule 0
fi