"""
ASGI config for DjangoStarter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from decouple import config
from django.core.asgi import get_asgi_application

APP_NAME = config('APP_NAME', default='DjangoStarter')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{APP_NAME}.settings')

application = get_asgi_application()
