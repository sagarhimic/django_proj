"""
WSGI config for fbvproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
path = "/home/sagarc/django_proj/fbvproject"
if path not in sys.path:
    sys.path.append(path)

# Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fbvproject.settings")

# Import and set the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
