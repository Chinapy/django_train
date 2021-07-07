"""
- 多くのリクエストの記録を取って、同時に多くの処理ができるようにする
ASGI config for helloworldproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworldproject.settings')

application = get_asgi_application()
