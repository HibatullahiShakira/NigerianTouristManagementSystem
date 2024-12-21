from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
