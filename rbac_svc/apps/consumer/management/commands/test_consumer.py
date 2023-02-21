from django.core.management.base import BaseCommand

from rbac_svc.apps.base.kafka import Consumer


def message_processor(message):
    """
    This function should redirect the message to required class
    """

    print(message, "Currently this is dummy")


class Command(BaseCommand):
    help = 'Run a test kafka consumer'

    def handle(self, *args, **options):
        consumer = Consumer("test-consumer-group", ['test-topic'])
        consumer.poll(message_processor)
