from django.urls import path

from .views import TodoListView, TaskCreateView, update_task_status

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("create_task/", TaskCreateView.as_view(), name="create_task"),
    path(
        "update_task_status/<int:pk>",
        update_task_status,
        name="update_task_status",
    ),
]

app_name = "todo_list"
