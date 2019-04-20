from django.utils import timezone
from rest_framework import serializers

from .models import Comment, Project, Reminder, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Project
        fields = ('id', 'url', 'name', 'tasks_ids',)
        read_only_fields = ('id', 'tasks_ids',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Task
        fields = ('id', 'url', 'project', 'title', 'description',
                  'deadline', 'priority', 'is_done', 'reminders_ids', 'comments_ids')
        read_only_fields = ('id', 'reminders_ids', 'comments_ids')

    def validate_deadline(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Comment
        fields = ('id', 'url', 'task', 'comment')
        read_only_fields = ('id',)


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Reminder
        fields = ('id', 'url', 'task', 'date')
        read_only_fields = ('id',)

    def validate_date(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('date must be in the future.')
        return value
