from django.db import models


class BaseModel(models.Model):
    """
    Abstract Generic model for updated_at and created_at field
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True
