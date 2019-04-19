from datetime import datetime

from django.db import models
# from django.urls import reverse
# from rest_framework.reverse import reverse as api_reverse


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<project: {self.name}>'

    class Meta:
        ordering = ('name',)
        verbose_name = 'project'
        verbose_name_plural = 'projects'


class Task(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    PRIORITY_CHOICES = ((LOW, 'Low'), (MEDIUM, 'Medium'), (HIGH, 'High'))

    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks_ids')
    title = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    done = models.BooleanField(default=False)
    done_when = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<task: {self.title}>'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'task'
        verbose_name_plural = 'tasks'


class Reminder(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='reminders_ids')
    date = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<reminder: {self.date}>'

    class Meta:
        ordering = ('-task', '-date')
        verbose_name = 'reminder'
        verbose_name_plural = 'reminders'


class Comment(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='comments_ids')
    comment = models.CharField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<comment: {self.comment}>'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
