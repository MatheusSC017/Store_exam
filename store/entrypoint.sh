#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostGres started"
fi

python manage.py flush --no-input
python manage.py migrate
if [ "$INITIAL_DATA" = "True" ]
then
  echo "Waiting for the initial data generator..."

  python data_generator.py

  echo "Generated data"
fi

exec "$@"
