#!/usr/bin/env bash
pip3 install -r requirements.txt
python3 manage.py loaddata fixtures/*.json
python3 manage.py runserver