# from django.db.models import Q
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Comment, Project, Reminder, Task
from .serializers import (CommentSerializer, ProjectSerializer,
                          ReminderSerializer, TaskSerializer)


######### PROJECT VIEW #########
class ProjectView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # def get_queryset(self):
    #     qs = Project.objects.all()
    #     query = self.request.get('q')
    #     if query is not None:
    #         qs = qs.filter(name__icontains=query)
    #     return qs


######### TASK VIEW #########
class TaskView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def get_queryset(self):
    #     qs = Task.objects.all()
    #     query = self.request.get('q')
    #     if query is not None:
    #         qs = qs.filter(Q(title__icontains=query) |
    #                        Q(description__icontains=query)
    #                        ).distinct()
    #     return qs


######### COMMENT VIEW #########
class CommentView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


######### REMINDER VIEW #########
class ReminderView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
