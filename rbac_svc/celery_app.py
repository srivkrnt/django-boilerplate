from __future__ import absolute_import, unicode_literals
import os

import configurations
from celery import Celery
import dotenv


dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rbac_svc.settings.prod')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Settings')

configurations.setup()
app = Celery('rbac_svc')

# namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
