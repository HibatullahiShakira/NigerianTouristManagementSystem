from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from users.models import User


class UserRegisterViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
