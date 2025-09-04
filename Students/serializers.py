from rest_framework.serializers import ModelSerializer
from .models import *


class Student_Serializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class Task_Serializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class Student_Task_Serializer(ModelSerializer):

    all_tasks = Task_Serializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'

class Task_data_Serializer(ModelSerializer):

    student_reference = Student_Serializer()

    class Meta:
        model = Task
        fields = '__all__'

class RankSheet_Serializer(ModelSerializer):
    class Meta:
        model = RankSheet
        fields = '__all__'