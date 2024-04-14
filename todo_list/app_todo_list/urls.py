from django.urls import path

from .views import TodoListView, TaskCreateView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("create_task/", TaskCreateView.as_view(), name="create_task" )
]

app_name = "todo_list"
