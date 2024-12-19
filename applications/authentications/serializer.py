from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'fullname',
            'biography',
            'unique_user_id',
            'date_joined',
            'last_login'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user