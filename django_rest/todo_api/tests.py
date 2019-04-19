from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from datetime import datetime, timedelta

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase

from .models import Comment, Project, Reminder, Task


class ProjectAPITestCase(APITestCase):
    def setUp(self):
        project = Project.objects.create(name='Django Rest Framework')
        task_one = Task.objects.create(project=project,
                                       title='Define App Features',
                                       description='apps, models, permissions, etc',
                                       deadline=datetime.today() + timedelta(days=1),
                                       priority=Task.LOW)

        task_two = Task.objects.create(project=project,
                                       title='Define App API',
                                       description='all URIs, serializers, views, etc',
                                       deadline=datetime.today() + timedelta(days=5),
                                       priority=Task.LOW)

        task_three = Task.objects.create(project=project,
                                         title='Define App Tests',
                                         description='create,retrieve, delete, requests, validations, etc',
                                         deadline=datetime.today() + timedelta(days=10),
                                         priority=Task.LOW)

        comment_one_task_one = Comment.objects.create(task=task_one,
                                                      comment='Donot forget to register the models in the admin site')
        comment_two_task_one = Comment.objects.create(task=task_one,
                                                      comment='It is done!')
        comment_one_task_two = Comment.objects.create(task=task_two,
                                                      comment='Add a custom queryset')
        comment_one_task_three = Comment.objects.create(task=task_three,
                                                        comment='Test deadline validation')

        reminder_one_task_one = Reminder.objects.create(task=task_one,
                                                        date=(datetime.today() + timedelta(hours=12)))
        reminder_two_task_one = Reminder.objects.create(task=task_one,
                                                        date=(datetime.today() + timedelta(hours=18)))
        reminder_one_task_two = Reminder.objects.create(task=task_two,
                                                        date=(datetime.today() + timedelta(days=2)))

    def test_single_project(self):
        project_count = Project.objects.count()
        self.assertEqual(project_count, 1)

    def test_triple_tasks(self):
        tasks_count = Task.objects.count()
        self.assertEqual(tasks_count, 3)

    def test_triple_tasks(self):
        tasks_count = Task.objects.count()
        self.assertEqual(tasks_count, 3)

    def test_project_list(self):
        data = {}
        url = api_reverse('todo:projects')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
