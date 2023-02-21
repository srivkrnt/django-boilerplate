from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from apps.accounts.models import Stakeholder, User
from apps.accounts.constants import Stakeholders, Errors, KeyLabels


class PlatformAssignmentRequestSerializer(serializers.Serializer):
    """
    Serializes platform assignment request
    """

    platform_id = serializers.IntegerField()

    def validate_platform_id(self, value):
        """
        Validates if platform_id exists or not
        """

        platform = Stakeholder.objects.filter(pk=value).prefetch_related(KeyLabels.STAKEHOLDER_TYPE).first()
        if not platform or platform.stakeholder_type__name != Stakeholders.PLATFORM:
            raise serializers.ValidationError(Errors.INVALID_PLATFORM_ID)

        return value


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for handling user login request
    """

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        email, password = attrs.get(KeyLabels.EMAIL), attrs.get(KeyLabels.PASSWORD)

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError(Errors.INVALID_EMAIL.format(email=email))

        if not check_password(password=password, encoded=user.password):
            raise serializers.ValidationError(Errors.INVALID_PASSWORD)

        return attrs


class UserLogoutSerializer(serializers.Serializer):
    """
    Serializer for handling user logout request
    """

    email = serializers.EmailField()
