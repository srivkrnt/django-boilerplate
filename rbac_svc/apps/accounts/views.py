from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from apps.accounts.constants import KeyLabels
from apps.accounts import models as account_models
from apps.accounts.serializers import model_serializers, request_serializers
from apps.base.constants import RequestMethods


class StakeholderViewset(ModelViewSet):
    """
    Viewset for stakeholders
    """

    queryset = account_models.Stakeholder.objects.all()
    serializer_class = model_serializers.StakeholderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = ['stakeholder_type', 'name']


class StakeholderTypeViewset(ModelViewSet):
    """
    Viewset for stakeholder type
    """

    queryset = account_models.StakeholderType.objects.all()
    serializer_class = model_serializers.StakeholderTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]


class UserViewset(ModelViewSet):
    """
    Viewset for users
    """

    queryset = account_models.User.objects.all()
    serializer_class = model_serializers.UserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    serializer_classes = {
        KeyLabels.LOGIN: request_serializers.UserLoginSerializer,
        KeyLabels.LOGOUT: request_serializers.UserLogoutSerializer
    }

    def get_serializer_class(self):
        """
        Returns serializer class based on the action
        defaults to serializer_class defined on the viewset
        """

        return self.serializer_classes.get(self.action, self.serializer_class)

    @action(detail=False, methods=[RequestMethods.POST], url_path=KeyLabels.LOGIN)
    def login(self, request):
        """
        Process login request
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(data={})

    @action(detail=False, methods=[RequestMethods.POST], url_path=KeyLabels.LOGOUT)
    def logout(self, request):
        """
        Process logout request
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(data={})
