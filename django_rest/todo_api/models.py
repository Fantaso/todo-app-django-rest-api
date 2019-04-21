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

    project = models.ForeignKey('Project', related_name='tasks_ids', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    is_done = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<task: {self.title}>'

    class Meta:
        ordering = ('-priority',)
        verbose_name = 'task'
        verbose_name_plural = 'tasks'


class Reminder(models.Model):
    task = models.ForeignKey('Task', related_name='reminders_ids', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<reminder: {self.date}>'

    class Meta:
        ordering = ('-date',)
        verbose_name = 'reminder'
        verbose_name_plural = 'reminders'


class Comment(models.Model):
    task = models.ForeignKey('Task', related_name='comments_ids', on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<comment: {self.comment}>'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
