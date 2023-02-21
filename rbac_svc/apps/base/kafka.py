from confluent_kafka import Producer as ConfluentKafkaProducer, Consumer as ConfluentKafkaConsumer
from django.conf import settings
import json


def _default_delivery_callback(err, message):
    """
    Default delivery callback
    """

    if err:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(message.topic(), message.partition()))


class Producer:
    """
    Kafka producer class
    """

    _instance = None

    def __init__(self) -> None:
        if not self._instance:
            self._instance = ConfluentKafkaProducer({
                'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVER
            })

    def produce(self, topic: str, message: dict, key=None, delivery_callback=None):
        """
        Produce a message
        """

        delivery_callback = delivery_callback or _default_delivery_callback
        self._instance.produce(
            topic,
            key=key,
            value=json.dumps(message).encode('utf-8'),
            callback=delivery_callback
        )
        self._instance.flush()


class Consumer:
    """
    Kafka consumer class
    """

    _instance = None

    def __init__(self, group_id: str, topics: list) -> None:

        # TODO: Raise custom exception later
        if not group_id or not topics:
            raise Exception("Invalid Configuration")

        self._instance = ConfluentKafkaConsumer({
            'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVER,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        })

        self._instance.subscribe(topics)

    def poll(self, message_processor, poll_size=1.0):
        """
        Poll messages and pass them to message_producer
        """

        while True:
            message = self._instance.poll(poll_size)

            if not message:
                continue

            if message.error():
                print("Consumer error: {}".format(message.error()))
                continue

            decoded_message = json.loads(message.value().decode('utf-8'))
            print('Received message: {}'.format(decoded_message))

            message_processor(decoded_message)
