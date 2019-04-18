from django.shortcuts import render
from rest_framework import viewsets

from .models import Comment, Project, Reminder, Task
from .serializers import (CommentSerializer, ProjectSerializer,
                          ReminderSerializer, TaskSerializer)


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReminderView(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
