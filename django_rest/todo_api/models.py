from django.db import models
from datetime import datetime


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<project: {self.name}>'

    class Meta:
        ordering = ('name',)


class Task(models.Model):
    PRIORITY_CHOICES = ((1, 'Low'), (2, 'Medium'), (3, 'High'))

    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks_ids')

    title = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=500, blank=True)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    # child_task
    # parent_task

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<task: {self.title}>'

    class Meta:
        ordering = ('-created_at',)


class Reminder(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='reminders_ids')

    date = models.DateTimeField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<reminder: {self.date}>'

    class Meta:
        ordering = ('-date',)


class Comment(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='comments_ids')

    comment = models.CharField(max_length=500, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<comment: {self.comment}>'

    class Meta:
        ordering = ('-created_at',)
