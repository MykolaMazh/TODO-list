from django.urls import path

from .views import TodoListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("create_task/", TaskCreateView.as_view(), name="create-task"),
    path("update_task/<int:pk>/<int:change_status>", TaskUpdateView.as_view(), name="task-update")
]

app_name = "todo_list"
