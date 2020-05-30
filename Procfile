web: gunicorn examkhojo-backend.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py migrate