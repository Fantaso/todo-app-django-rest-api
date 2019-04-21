from datetime import datetime, timedelta

import pytz
import os
import time

from pprint import pprint
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Comment, Project, Reminder, Task


######### TESTS PROJECT #########
class ProjectTests(APITestCase):
    def setUp(self):
        project = Project.objects.create(name='Python Project')

    ########## BASIC TESTING (CRUDL) AND FIELDS VALIDATORS AND INITIAL STATE ##########

    def test_project_list_get(self):
        """
        Projects retrieve.
        """

        url = reverse('project-list')
        req = self.client.get(url)

        req_project = req.data[0]
        db_project = Project.objects.filter(name='Python Project').first()

        self.assertEqual(req.status_code, status.HTTP_200_OK)
        self.assertEqual(req_project['name'], db_project.name)
        self.assertIsNotNone(req_project['url'])
        self.assertEqual(len(req_project['tasks_ids']), len(db_project.tasks_ids.all()))

    def test_project_list_post(self):
        """
        Project create.
        """

        url = reverse('project-list')
        data = {'name': 'Python Project 2'}

        req = self.client.post(url, data)
        db_project = Project.objects.filter(name='Python Project 2').first()

        self.assertEqual(req.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)
        self.assertEqual(db_project.name, req.data['name'])

    def test_project_detail_get(self):
        """
        Project retrieve.
        """

        db_project = Project.objects.filter(name='Python Project').first()
        url = reverse('project-detail', args=(db_project.id,))

        req = self.client.get(url)

        self.assertEqual(req.status_code, status.HTTP_200_OK)
        self.assertEqual(db_project.name, req.data['name'])
        self.assertIsNotNone(req.data['url'])
        self.assertEqual(len(req.data['tasks_ids']), len(db_project.tasks_ids.all()))

    def test_project_detail_put(self):
        """
        Project update put.
        """

        db_project = Project.objects.filter(name='Python Project').first()
        url = reverse('project-detail', args=(db_project.id,))
        data = {'name': 'Python Project Updated with PUT method'}

        req = self.client.put(url, data)

        self.assertEqual(req.status_code, status.HTTP_200_OK)
        self.assertEqual(req.data['name'], data['name'])

    def test_project_detail_patch(self):
        """
        Project update patch.
        """

        db_project = Project.objects.filter(name='Python Project').first()
        url = reverse('project-detail', args=(db_project.id,))
        data = {'name': 'Python Project Updated with PATCH method'}

        req = self.client.patch(url, data)

        self.assertEqual(req.status_code, status.HTTP_200_OK)
        self.assertEqual(req.data['name'], data['name'])

    def test_project_detail_delete(self):
        """
        Project delete.
        """

        project_to_delete = Project.objects.create(name='Test Project')

        url = reverse('project-detail', args=(project_to_delete.id,))
        req = self.client.delete(url)

        self.assertEqual(req.status_code, status.HTTP_204_NO_CONTENT)
        print(req.data)
        self.assertIsNone(req.data)

    def test_project_list_post_name_unique(self):
        """
        Project name unique.
        """

        url = reverse('project-list')
        data = {'name': 'Python Project'}

        req = self.client.post(url, data)
        req_error_msg = req.data['name'][0]

        self.assertEqual(req.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(req_error_msg, 'project with this name already exists.')

    def test_project_list_post_name_length(self):
        """
        Project name length.
        """

        url = reverse('project-list')
        data = {'name': 10*'project name with more than 50 characters'}

        req = self.client.post(url, data)
        req_error_msg = req.data['name'][0]

        self.assertEqual(req.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(req_error_msg, 'Ensure this field has no more than 50 characters.')

    def test_project_list_post_name_blank(self):
        """
        Project name blank.
        """

        url = reverse('project-list')
        data = {'name': ''}

        req = self.client.post(url, data)
        req_error_msg = req.data['name'][0]

        self.assertEqual(req.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(req_error_msg, 'This field may not be blank.')

    def test_project_list_post_created_at(self):
        """
        Project created at.
        """

        url = reverse('project-list')
        data = {'name': 'Python Project Created At'}

        req = self.client.post(url, data)
        db_project = Project.objects.filter(name='Python Project Created At').first()

        self.assertEqual(req.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)
        self.assertEqual(db_project.created_at.date(), timezone.now().date())

    def test_project_list_put_updated_at(self):
        """
        Project updated at.
        """

        url = reverse('project-list')
        data = {'name': 'Python Project 2'}

        # create a new project
        req = self.client.post(url, data)

        # retrieve from database and check created_at and updated_at
        db_project = Project.objects.filter(name='Python Project 2').first()
        self.assertEqual(db_project.created_at.second, db_project.updated_at.second)

        # wait 2 seconds and update the project
        time.sleep(2)
        url = reverse('project-detail', args=(db_project.id,))
        data = {'name': 'Python Project 2 Updated'}

        req = self.client.put(url, data)

        # retrieve from database and check created_at and updated_at must have changed
        db_project = Project.objects.filter(name='Python Project 2 Updated').first()
        self.assertNotEqual(db_project.created_at.second, db_project.updated_at.second)

    def test_project_list_get_db_retrieve_ordering(self):
        """
        Project db retrieve ordering.
        """

        # retreive the project that was created in setUp test method.
        project_setup = Project.objects.filter(name='Python Project').first()

        # create 3 new projects
        project_one = Project.objects.create(name='Python Project 1')
        project_two = Project.objects.create(name='Pathon Project 2')
        project_three = Project.objects.create(name='Python Project 3')

        # retrieve all projects
        url = reverse('project-list')
        req = self.client.get(url)

        # assert the ammount of project retrieve and in the right order (sorted by name)
        self.assertEqual(len(req.data), 4)
        self.assertEqual(req.data[0]['name'], project_two.name)
        self.assertEqual(req.data[1]['name'], project_setup.name)
        self.assertEqual(req.data[2]['name'], project_one.name)
        self.assertEqual(req.data[3]['name'], project_three.name)

    ########## NESTED TESTING (CRUDL) ##########

    def project_tasks_list_get(self):
        """
        Project tasks retrieve.
        """
        pass

    def project_tasks_list_post(self):
        """
        Project tasks create.
        """
        pass


######### TESTS PROJECT #########
class TaskTests(APITestCase):
    def setUp(self):
        project = Project.objects.create(name='Django Project')
        task = Task.objects.create(project=project,
                                   title='Define Features',
                                   description='apps, models, permissions, etc',
                                   deadline=(timezone.now() + timedelta(days=1)),
                                   priority=Task.LOW)

    ########## BASIC TESTING (CRUDL) AND FIELDS VALIDATORS AND INITIAL STATE ##########

    def test_task_list_get(self):
        """
        Tasks retrieve.
        """

        url = reverse('task-list')
        req = self.client.get(url)

        req_task = req.data[0]
        db_task = Task.objects.filter(title='Define Features').first()
        db_project = Project.objects.filter(name='Django Project').first()

        self.assertEqual(req.status_code, status.HTTP_200_OK)
        self.assertEqual(req_task['title'], db_task.title)
        self.assertEqual(req_task['priority'], db_task.priority)
        self.assertEqual(req_task['description'], db_task.description)
        # self.assertEqual(req_task['deadline'], db_task.deadline)
        self.assertFalse(req_task['is_done'])
        self.assertEqual(len(req_task['comments_ids']), len(db_task.comments_ids.all()))
        self.assertEqual(len(req_task['reminders_ids']), len(db_task.reminders_ids.all()))

    def test_task_list_post(self):
        """
        Task create.
        """

        # task data
        project = Project.objects.filter(name='Django Project').first()
        data = {
            'project': project.id,
            'title': 'Define App API',
            'description': 'all URIs, serializers, views, etc',
            'deadline': (timezone.now() + timedelta(days=5)),
            'priority': Task.MEDIUM,
        }

        # request
        url = reverse('task-list')
        req = self.client.post(url, data)

        # get data just created from database
        db_task = Task.objects.filter(title='Define App API').first()

        self.assertEqual(req.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(req.data['project'], db_task.project.id)
        self.assertEqual(req.data['title'], db_task.title)
        self.assertEqual(req.data['priority'], db_task.priority)
        self.assertEqual(req.data['description'], db_task.description)
        self.assertIsNotNone(req.data['url'])
        self.assertFalse(req.data['is_done'])
        self.assertEqual(len(req.data['comments_ids']), len(db_task.comments_ids.all()))
        self.assertEqual(len(req.data['reminders_ids']), len(db_task.reminders_ids.all()))


######### TESTS PROJECT #########
class CommentTests(APITestCase):
    def setUp(self):
        pass


######### TESTS PROJECT #########
class ReminderTests(APITestCase):
    def setUp(self):
        pass
