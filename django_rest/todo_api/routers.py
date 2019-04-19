from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from . import views


######### NESTING ROUTER CLASS #########
class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


######### NESTING ROUTER OBJECT #########
todo_api_router = NestedDefaultRouter()


######### REGISTER ProjectView #########
projects_router = todo_api_router.register('projects', views.ProjectView)

# 1st Degree: NESTINGVIEW: TaskView
projects_tasks = projects_router.register('tasks',
                                          views.TaskView,
                                          base_name='project-tasks',
                                          parents_query_lookups=['project'])
# parents_query_lookups = Task.objects.filter(task={task_id})

# 2nd Degree: NESTINGVIEW: CommentView
projects_tasks.register('comments',
                        views.CommentView,
                        base_name='project-task-comments',
                        parents_query_lookups=['task__project', 'task'])
# parents_query_lookups = Reminder.objects.filter(task__project={project_id}, task={task_id})

# 2nd Degree: NESTINGVIEW: ReminderView
projects_tasks.register('reminders',
                        views.ReminderView,
                        base_name='project-task-reminders',
                        parents_query_lookups=['task__project', 'task'])
# parents_query_lookups = Reminder.objects.filter(task__project={project_id}, task={task_id})


######### REGISTER TaskView #########
tasks_router = todo_api_router.register('tasks', views.TaskView)
# NESTINGVIEW: CommentView and ReminderView
tasks_router.register('comments',
                      views.CommentView,
                      base_name='task-comments',
                      parents_query_lookups=['task'])
tasks_router.register('reminders',
                      views.CommentView,
                      base_name='task-reminders',
                      parents_query_lookups=['task'])


######### REGISTER CommentView and ReminderView #########
todo_api_router.register('comments', views.CommentView)
todo_api_router.register('reminders', views.ReminderView)
