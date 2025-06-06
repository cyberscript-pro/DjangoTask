from rest_framework import serializers
from apps.bk_task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=5, error_messages={'min_length': 'El campo title debe tener al menos 5 caracteres'}, required=True)
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

    def validate_title(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError('El campo title debe tener al menos 5 caracteres.')
        return value