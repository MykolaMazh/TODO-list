from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Task
from django.urls import reverse


class TaskUpdateViewTest(TestCase):
    def setUp(self):
        Task.objects.create(description="New Test Task")

    def test_post_to_update_status_only(self):
        self.client.post(
            reverse(
                "todo_list:task-update", kwargs={"pk": 1}
            ), data={"change-task-status": "change"}
        )
        self.assertEqual(Task.objects.get(pk=1).is_done, True)
        self.client.post(
            reverse(
                "todo_list:task-update", kwargs={"pk": 1}
            ), data={"change-task-status": "change again"}
        )
        self.assertEqual(Task.objects.get(pk=1).is_done, False)

    def test_post_default(self):
        response = self.client.get(
            reverse("todo_list:task-update", args=[1])
        )
        self.assertEqual(Task.objects.get(pk=1).is_done, False)
        self.assertEqual(response.status_code, 200)
