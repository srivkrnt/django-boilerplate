from rest_framework import serializers

from apps.accounts.models import Role, Permission, User, StakeholderType, Stakeholder


class RoleSerializer(serializers.ModelSerializer):
    """
    Role Model serializer
    """

    class Meta:
        model = Role
        fields = (
            'pk',
            'name',
            'display_name',
            'description',
        )


class PermissionSerializer(serializers.ModelSerializer):
    """
    Permission Model Serializer
    """

    class Meta:
        model = Permission
        fields = (
            'pk',
            'name',
            'display_name',
            'description',
        )


class UserSerializer(serializers.ModelSerializer):
    """
    User Model Serializer
    """

    class Meta:
        model = User
        fields = (
            'pk',
            'first_name',
            'last_name',
            'name',
            'email',
            'user_type',
        )


class StakeholderTypeSerializer(serializers.ModelSerializer):
    """
    StakholderType Model serializer
    """

    class Meta:
        model = StakeholderType
        fields = (
            'pk',
            'name',
            'description'
        )


class StakeholderSerializer(serializers.ModelSerializer):
    """
    Stakeholder Serializer
    """

    class Meta:
        model = Stakeholder
        fields = (
            'pk',
            'name',
            'stakeholder_type',
            'external_id'
        )
