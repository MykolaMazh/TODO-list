from django.db import models


class Task(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(related_name='tasks')
    is_done = models.BooleanField()
    # atetime, when a task was created
# optional deadline datetime if a task should be done until some datetime
# the boolean field that marks if the task is done or not
# tags that are relevant for this task
# Tag - a tag symbolizes the theme of the task and consists only of a name.

class Tag(models.Model):
    name = models.CharField(max_length=75)