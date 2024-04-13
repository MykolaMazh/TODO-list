from django.db import models


class Task(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField("Tag", related_name='tasks')
    is_done = models.BooleanField()

    def __str__(self):
        return self.description


class Tag(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name