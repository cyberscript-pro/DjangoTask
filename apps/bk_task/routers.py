from rest_framework import routers
from .views.project_view import ProjectViewSet
from .views.task_view import TaskViewSet

router = routers.DefaultRouter()

router.register(prefix = 'project', viewset = ProjectViewSet, basename='Projects')
router.register(prefix='task', viewset = TaskViewSet, basename='Tasks')

urlpatterns = router.urls