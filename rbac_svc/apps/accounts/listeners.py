import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from rbac_svc.apps.accounts.serializers.model_serializers import UserSerializer
from apps.accounts.models import User
from apps.accounts.producer import UserProducer

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def user_save_listener(sender, instance, created, *args, **kwargs):
    """
    Post save listener for user model
    """

    UserProducer().produce_user(
        user_type=instance.user_type.name,
        created=created,
        data=UserSerializer(instance=instance).data
    )
