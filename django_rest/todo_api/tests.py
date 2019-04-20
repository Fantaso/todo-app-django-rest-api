from datetime import datetime, timedelta

import pytz

from pprint import pprint
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Comment, Project, Reminder, Task

'''
class Project(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
class Reminder(models.Model):
    task = models.ForeignKey('Task', related_name='reminders_ids', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Comment(models.Model):
    task = models.ForeignKey('Task', related_name='comments_ids', on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
'''

######### TESTS PROJECT #########


class ProjectTests(APITestCase):
    def setUp(self):
        project = Project.objects.create(name='Python Project')

    def test_create_project(self):
        """Ensure we can create a project."""

        url = reverse('project-list')
        data = {'name': 'Python Project 2'}

        response = self.client.post(url, data)
        print(response.data,  response.render, response.cookies)
        print('------------')
        print(response.render)
        print('------------')
        print(response.cookies)
        print('------------')
        print(response.request)
        print(response.context_data)
        print('------------')
        print('------------')
        print(response.client)
        pprint(dir(response))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)
        # self.assertEqual(Project.objects.filter(name='Python Project 2').name,
        # response.data['name'])

    def test_update_project(self):
        """Ensure we can update a project."""

        url = reverse('project-list')
        data = {'name': 'Python Project'}

        response = self.client.post(url, data)

        # print(response.data)
        # print(response.data['url'])

        # response_put = self.client.put()

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Project.objects.count(), 1)
        # self.assertEqual(Project.objects.get().name, 'Python Project')


######### TESTS TASK #########
class TaskTests(APITestCase):
    def setUp(self):
        project = Project.objects.create(name='Python Project')

    def test_create_task(self):
        """Ensure we can create a Task."""

        project = Project.objects.filter(name='Python Project').first()

        url = reverse('task-list')
        data = {'project': project.id,
                'title': 'Define App API',
                'description': 'all URIs, serializers, views, etc',
                'deadline': (timezone.now() + timedelta(days=5)),
                'priority': Task.LOW}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Define App API')
        self.assertEqual(Task.objects.get().priority, 1)


######### TESTS COMMENT #########
class CommentTests(APITestCase):
    def setUp(self):
        project = Project.objects.create(name='Python Project')
        task = Task.objects.create(project=project,
                                   title='Define App Features',
                                   description='apps, models, permissions, etc',
                                   deadline=(timezone.now() + timedelta(days=1)),
                                   priority=Task.LOW,)

    def test_create_comment(self):
        """Ensure we can create a Comment."""

        task = Task.objects.filter(title='Define App Features').first()

        url = reverse('comment-list')
        data = {'task': task.id,
                'comment': 'Donot forget to register the models in the admin site'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().comment,
                         'Donot forget to register the models in the admin site')


######### TESTS REMINDER #########
class ReminderTests(APITestCase):
    def setUp(self):
        project = Project.objects.create(name='Python Project')
        task = Task.objects.create(project=project,
                                   title='Define App Features',
                                   description='apps, models, permissions, etc',
                                   deadline=(timezone.now() + timedelta(days=1)),
                                   priority=Task.LOW,)

    def test_create_reminder(self):
        """Ensure we can create a Reminder."""

        task = Task.objects.filter(title='Define App Features').first()

        url = reverse('reminder-list')
        data = {'task': task.id,
                'date': datetime(2019, 4, 20, 21, 0, 0, tzinfo=pytz.UTC)}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reminder.objects.count(), 1)
        self.assertEqual(Reminder.objects.get().date,
                         datetime(2019, 4, 20, 21, 0, 0, tzinfo=pytz.UTC))
