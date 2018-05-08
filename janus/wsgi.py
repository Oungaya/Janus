"""
WSGI config for janus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

path = '/app/janus'
if path not in sys.path:
    sys.path.append(path)
    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "janus.settings")

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
