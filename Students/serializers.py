from rest_framework.serializers import ModelSerializer
from .models import *

class Task_Serializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# class RankSheet_Serializer(ModelSerializer):
#     class Meta:
#         model = RankSheet
#         fields = '__all__'