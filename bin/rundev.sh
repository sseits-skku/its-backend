#!/bin/bash

exitfn () {
    trap SIGINT
    echo; echo 'Shutdown gracefully...'
    kill -9 %1
    kill -9 %2
    exit
}

trap "exitfn" INT

celery worker -P gevent -A server -l info &
sleep 2
celery flower -P gevent -A server -l info &
python manage.py runserver

trap SIGINT
