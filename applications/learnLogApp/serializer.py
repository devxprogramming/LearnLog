from rest_framework.serializers import ModelSerializer
from .models import LearnLog


class LearnLogSerializer(ModelSerializer):
    class Meta:
        model = LearnLog
        fields = '__all__'