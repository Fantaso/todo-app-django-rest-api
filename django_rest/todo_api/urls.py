from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('projects', views.ProjectView)
router.register('tasks', views.TaskView)
router.register('comments', views.CommentView)
router.register('reminders', views.ReminderView)

urlpatterns = [
    path('', include(router.urls)),
]
