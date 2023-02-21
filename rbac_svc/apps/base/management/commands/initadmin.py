"""Command for creating super-user."""
import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Defines initadmin command that creates admin account
    """

    def handle(self, *args, **options):
        """
        Create an admin account if no user is present.
        """

        user = get_user_model()
        if not user.objects.count():
            user.objects.create_superuser(
                username=os.environ.get("ADMIN_SUPERUSER_USERNAME", "admin"),
                email=os.environ.get("ADMIN_SUPERUSER_EMAIL", "admin@gmail.com"),
                password=os.environ["ADMIN_SUPERUSER_PASSWORD"],
            )
            self.stdout.write(
                self.style.SUCCESS('Admin account created! :)'))
        else:
            error = 'Admin accounts can only be initialized if no Accounts exist'
            self.stdout.write(self.style.ERROR('Error:- ' + str(error)))
