import logging

from apps.accounts.constants import KafkaActions, KafkaTopics, UserType
from apps.base.kafka import Producer
from rbac_svc.apps.accounts.constants import KeyLabels, Errors

logger = logging.getLogger(__name__)


class UserProducer(Producer):
    """
    User producer
    """

    def __init__(self) -> None:
        super().__init__()
        self.user_type_producer_map = {
            UserType.SELLER: self._produce_seller,
            UserType.PLATFORM: self._produce_platform_user
        }

    def _produce_seller(self, created: bool, data: dict):
        """
        produce seller to the required kafka topic
        """

        self.produce(
            topic=KafkaTopics.SELLER_SYNC,
            message={
                KeyLabels.PAYLOAD: data,
                KeyLabels.META: {
                    KeyLabels.JOB_TYPE: KafkaActions.CREATE_SELLER if created else KafkaActions.UPDATE_SELLER
                }
            }
        )

    def _produce_platform_user(self, created: bool, data: dict):
        """
        produce platform to the required kafka topic
        """

        self.produce(
            topic=KafkaTopics.PLATFORM_SYNC,
            message={
                KeyLabels.PAYLOAD: data,
                KeyLabels.META: {
                    KeyLabels.JOB_TYPE: (
                        KafkaActions.CREATE_PLATFORM_USER
                        if created
                        else KafkaActions.UPDATE_PLATFORM_USER
                    )
                }
            }
        )

    def produce_user(self, user_type: str, created: bool, data: dict):
        """
        Produce user to kafka topic
        """

        producer = self.user_type_producer_map.get(user_type)

        if not producer:
            logger.info(f'{Errors.NO_PRODUCER_FOUND} for user_type :: {user_type}')
            return

        producer(created=created, data=data)
