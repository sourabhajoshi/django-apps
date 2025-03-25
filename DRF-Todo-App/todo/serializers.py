from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task #define model to serialize
        fields = '__all__' # serialize all fields