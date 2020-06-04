"""
WSGI config for examkhojo_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examkhojo_backend.settings')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
