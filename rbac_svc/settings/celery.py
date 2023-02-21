from enum import Enum, unique
import os

from celery.schedules import crontab


@unique
class Queue(Enum):
    """
    List of all queues available for Service
    """

    DEFAULT = "default"


class CelerySettingsMixin:
    """
    Celery Settings
    """

    CELERY_BROKER_URL = property(lambda self: self.REDIS_URL)
    CELERY_TASK_ANNOTATIONS = {'*': {'max_retries': 3}}

    # Settings for celery longterm scheduler
    CELERY_LONGTERM_SCHEDULER_BACKEND = f'{CELERY_BROKER_URL}/1'

    CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

    CELERY_RESULT_BACKEND = 'django-db'

    CELERY_TIMEZONE = os.environ.get('TZ', 'UTC')

    CELERY_BEAT_SCHEDULE = {
        "test_task_schedule": {
            "task": "apps.tracking.tasks.test_task",
            "schedule": 30.0,
            "enabled": True
        }
    }

    CELERY_TASK_ROUTES = ([
        ("apps.tracking.tasks.*", {"queue": Queue.DEFAULT.value}),
    ],)

    CELERY_TASK_DEFAULT_QUEUE = Queue.DEFAULT.value
