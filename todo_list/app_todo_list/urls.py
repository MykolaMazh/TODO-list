from django.urls import path

from app_todo_list.views import (
    TodoListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("create_task/", TaskCreateView.as_view(), name="create-task"),
    path(
        "update_task/<int:pk>/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "delete_task/<int:pk>/", TaskDeleteView.as_view(), name="delete-task"
    ),
    path("tag_list/", TagListView.as_view(), name="tag-list"),
    path("tag_create/", TagCreateView.as_view(), name="tag-create"),
    path("tag_update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag_delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_list"
