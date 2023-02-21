from django.urls import include, path
from rest_framework import routers

from apps.accounts import views

AccountsRouter = routers.DefaultRouter()
AccountsRouter.register('stakeholder', viewset=views.StakeholderViewset, basename='stakeholder')
AccountsRouter.register('stakeholder-type', viewset=views.StakeholderTypeViewset, basename='stakeholder-type')
AccountsRouter.register('user', viewset=views.UserViewset, basename='user')


urlpatterns = [
    path('', include(AccountsRouter.urls)),
]
