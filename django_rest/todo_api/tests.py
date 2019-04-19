# from django.contrib.auth import get_user_model
# from rest_framework_jwt.settings import api_settings


from django.urls import reverse

from rest_framework import status
# from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase

from .models import Comment, Project, Reminder, Task

from django.utils import timezone
from datetime import datetime, timedelta
import pytz


######### TESTS PROJECT #########
class ProjectTests(APITestCase):
    def test_create_project(self):
        """Ensure we can create a project."""

        url = reverse('project-list')
        data = {'name': 'Python Project'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, 'Python Project')


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
