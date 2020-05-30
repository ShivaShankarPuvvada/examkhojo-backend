release: python manage.py migrate
release: python manage.py collectstatic
web: gunicorn examkhojo_backend.wsgi --log-file -