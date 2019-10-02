#!/bin/bash
export DJANGO_SETTINGS_MODULE=server.settings.development
forceexitfn () {
    trap SIGINT
    echo '------EMERGENCY SHUTDOWN------'
    kill -SIGKILL %1
    kill -SIGKILL %2
    exit
}

exitfn () {
    trap SIGINT
    trap "forceexitfn" INT
    echo 'Shutdown gracefully...'
    kill -SIGTERM %1
    kill -SIGTERM %2
    wait $(jobs -rp)
    echo '!!BYE!!'
    trap SIGINT
    exit
}

trap "exitfn" INT

celery worker -P gevent -A server -l info &
sleep 2
celery flower -P gevent -A server -l info &
if ! python manage.py runserver; then
    exitfn
    exit
else
    trap SIGINT
    exit
fi
