import os

from . import common


class Settings(common.Settings):
    """
    Development settings for the service
    """

    DEBUG = False
    ENVIRONMENT_CODE = os.environ.get('ENVIRONMENT_CODE', 'prod')
