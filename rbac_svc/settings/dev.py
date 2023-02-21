import os

from . import common


class Settings(common.Settings):
    """
    Development settings for the service
    """

    DEBUG = True
    ENVIRONMENT_CODE = os.environ.get('ENVIRONMENT_CODE', 'dev')
