#!/usr/bin/env bash
source ./venv/bin/activate
python3 manage.py makemigrations snippets --settings=robot_view.dev_settings
python3 manage.py migrate --settings=robot_view.dev_settings
python3 manage.py runserver --settings=robot_view.dev_settings