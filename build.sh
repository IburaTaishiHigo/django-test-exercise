#!/usr/bin/env bash
set -o erreexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate