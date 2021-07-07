"""
- ブラウザから受け取ったrequestをもとにオブジェクトを作成し、
Djangoの内部で複雑な処理を行う上での準備をする役割。
- ウェブサーバーとDjangoの間を取り持つような役割を担う

WSGI config for helloworldproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworldproject.settings')

application = get_wsgi_application()
