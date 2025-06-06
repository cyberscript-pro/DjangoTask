from rest_framework import serializers
from apps.bk_task.models import Project
from .task_serializer import TaskSerializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'tasks': TaskSerializer(instance.tasks.all(), many=True).data
        }