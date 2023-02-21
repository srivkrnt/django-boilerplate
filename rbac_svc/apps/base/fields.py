from django.db import models


class LowerCaseCharField(models.CharField):
    """
    Lower case char field
    """

    def get_prep_value(self, value):
        return str(value).lower()
