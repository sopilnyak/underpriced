#!/bin/bash -e
pip install -r requirements.txt
./manage.py migrate
npm install
npm run build
./manage.py runserver 8080
