from django.contrib import admin

from . import models


######### PROJECT ADMIN #########
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


######### TASK ADMIN #########
@admin.register(models.Task)
class TasktAdmin(admin.ModelAdmin):
    list_display = ['project', 'title', 'description', 'deadline',
                    'priority', 'is_done', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


######### COMMENT ADMIN #########
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'comment', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


######### REMINDER ADMIN #########
@admin.register(models.Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['task', 'date', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
