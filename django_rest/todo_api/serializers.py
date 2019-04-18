from rest_framework import serializers

from .models import Comment, Project, Reminder, Task


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'url', 'name', 'tasks_ids')
        read_only_fields = ('id', 'tasks_ids',)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'url', 'project', 'title', 'description',
                  'deadline', 'priority', 'reminders_ids', 'comments_ids')
        read_only_fields = ('id', 'reminders_ids', 'comments_ids')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'url', 'task', 'comment')
        read_only_fields = ('id',)


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'url', 'task', 'date')
        read_only_fields = ('id',)

        # read_only_fields = ('id', 'url', 'task', 'date') # '__all__'
        # depth = 1 # depth of relationship should print flat
        # exclude = ('users',)

    # def save(self):
    #     email = self.validated_data['email']
    #     message = self.validated_data['message']
    #     send_email(from=email, message=message)
    # def validate_title(self, value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value
    # def validate(self, data):
    #     """
    #     Check that start is before finish.
    #     """
    #     if data['start'] > data['finish']:
    #         raise serializers.ValidationError("finish must occur after start")
    #     return data
