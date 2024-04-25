from django.db import models


class Task(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["is_done", "-created_at"]


class Tag(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name
