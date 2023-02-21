from django.contrib.auth.hashers import make_password
from django.db import models

from apps.base.fields import LowerCaseCharField
from rbac_svc.apps.base.models import BaseModel


class Role(BaseModel):
    """
    Model storing different type of roles
    """

    name = LowerCaseCharField(max_length=50, help_text="Name of the role")
    display_name = models.CharField(max_length=50, help_text="Display name of the role")
    description = models.CharField(max_length=255, help_text="Description for the role", default='')

    def __str__(self) -> str:
        return f'{self.display_name} : {self.description}'


class Permission(BaseModel):
    """
    Model storing different type of permissions
    """

    name = LowerCaseCharField(max_length=50, help_text="Name of the Permission")
    display_name = models.CharField(max_length=50, help_text="Display name of the permission")
    description = models.CharField(max_length=255, help_text="Description for the Permission", default='')

    def __str__(self) -> str:
        return f'{self.display_name} : {self.description}'


class RolePermissionMap(BaseModel):
    """
    Model storing the mapping between roles and permission
    """

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="Reference to a row in role table"
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="Reference to a row in permisison table"
    )

    def __str__(self) -> str:
        return f'Role :: {self.role} : Permission :: {self.permission}'


class StakeholderType(BaseModel):
    """
    Model storing different stakholder types
    """

    name = LowerCaseCharField(max_length=50, help_text="Name of the stakeholder type")
    description = models.CharField(
        max_length=255,
        help_text="Description about the stakeholder type",
        default=''
    )

    def __str__(self) -> str:
        return f'{self.name} : {self.description}'


class Stakeholder(BaseModel):
    """
    Model storing stakeholders
    """

    name = LowerCaseCharField(max_length=50, help_text="Name of the stakeholder")
    display_name = models.CharField(max_length=50, help_text="Display name for the stakeholder")
    stakeholder_type = models.ForeignKey(
        StakeholderType,
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="Reference to a row in stakeholder-type table"
    )
    external_id = models.CharField(
        max_length=50,
        help_text="ID that can be used to refer this stakeholder in other systems"
    )

    def __str__(self) -> str:
        return f'{self.display_name} : {self.external_id}'


class User(BaseModel):
    """
    Model storing the users
    """

    first_name = models.CharField(max_length=50, help_text="First Name of the user")
    last_name = models.CharField(max_length=50, help_text="Last Name of the user", default='')
    email = models.EmailField(help_text="Email of the user", unique=True)
    password = models.CharField(max_length=255, help_text="encrypted password of the user")
    user_type = models.ForeignKey(
        StakeholderType,
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="Reference to a row in stakeholder-type table, tells what is the type of user"
    )

    def __str__(self) -> str:
        return f'{self.first_name} : {self.last_name} : {self.email} : {self.user_type}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs) -> None:
        """
        Saving model instance
        """

        self.email = self.email.lower()
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)


class UserPlatformAssociation(BaseModel):
    """
    Model storing association between user and platform
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="Reference to a row in user table"
    )
    platform = models.ForeignKey(
        Stakeholder,
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="Reference to a row in stakeholder table with user_type as Platform"
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="Reference to a row in Role table"
    )
    external_seller_id = models.CharField(
        max_length=50,
        help_text="ID that can be used to refer a seller platform combination in other systems",
        null=True,
        default=None
    )

    def __str__(self) -> str:
        return f'{self.user} : {self.platform} : {self.role} : {self.external_seller_id}'
