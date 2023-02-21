from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import loaddata

from apps.accounts import models as account_models


class Command(BaseCommand):
    """
    Defines check_and_load_fixture command that loads the fixture
    """

    def load_fixture(self, model_klass, fixture_name):
        try:
            if not model_klass.objects.exists():
                management.call_command(loaddata.Command(), fixture_name)
                self.stdout.write(self.style.SUCCESS(f"Successfully applied fixture :: {fixture_name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Data already present for fixture :: {fixture_name}"))
        except Exception as exc:
            self.stdout.write(self.style.ERROR(f'Failed to apply {fixture_name} fixture due to err : {exc}'))

    def handle(self, *args, **kwargs):
        """
        Process all fixtures
        """

        self.load_fixture(account_models.Permission, "permissions")
