from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.bk_task.serializers.project_serializer import ProjectSerializer


@extend_schema(tags=['Projects Endpoints'])
class ProjectViewSet(viewsets.GenericViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(available=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, available=True).first()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self,request, pk=None, *args, **kwargs):
        if pk is not None:
            if self.get_queryset(pk):
                serializer = self.serializer_class(self.get_queryset(pk))
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({"Project not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"ID is required"}, status = status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        return Response({"Project not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()

        if not instance:
            return Response({"Project not found"}, status=status.HTTP_404_NOT_FOUND)

        instance.available = False
        instance.save()
        return Response({"Project successfully deleted"}, status=status.HTTP_200_OK)