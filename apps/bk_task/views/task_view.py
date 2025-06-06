from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from yaml import serialize

from apps.bk_task.serializers.task_serializer import TaskSerializer

@extend_schema(tags=['Tasks'])
class TaskViewSet(GenericViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self, pk=None):
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            if self.get_queryset(pk):
                serializer = self.serializer_class(self.get_queryset(pk))
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Task not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()

        if not instance:
            return Response({"Task not found"}, status=status.HTTP_404_NOT_FOUND)

        instance.available=False
        instance.save()
        return Response({"Task successfully deleted"}, status=status.HTTP_200_OK)
