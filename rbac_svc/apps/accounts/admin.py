from django.contrib import admin

from apps.accounts import models as account_models


class RoleAdmin(admin.ModelAdmin):
    """
    Admin for Role Model
    """


class PermissionAdmin(admin.ModelAdmin):
    """
    Admin for Permission Model
    """


class UserAdmin(admin.ModelAdmin):
    """
    Admin for User Model
    """


class StakeholderAdmin(admin.ModelAdmin):
    """
    Admin for Stakeholder Model
    """

    search_fields = ['name', 'external_id']
    list_filter = ['stakeholder_type__name']


class StakholderTypeAdmin(admin.ModelAdmin):
    """
    Admin for StakehoderType Model
    """

    search_fields = ['name']


class RolePermissionMapAdmin(admin.ModelAdmin):
    """
    Admin for Role Permission map model
    """


class UserPlatformAssociationAdmin(admin.ModelAdmin):
    """
    Admin for user platform association model
    """


admin.site.register(account_models.Role, RoleAdmin)
admin.site.register(account_models.Permission, PermissionAdmin)
admin.site.register(account_models.User, UserAdmin)
admin.site.register(account_models.Stakeholder, StakeholderAdmin)
admin.site.register(account_models.StakeholderType, StakholderTypeAdmin)
admin.site.register(account_models.RolePermissionMap, RolePermissionMapAdmin)
admin.site.register(account_models.UserPlatformAssociation, UserPlatformAssociationAdmin)
