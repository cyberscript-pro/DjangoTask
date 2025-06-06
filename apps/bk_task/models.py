from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from enum import Enum

class Project(models.Model):
    name = models.CharField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
