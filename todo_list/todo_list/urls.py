from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_todo_list.urls', namespace="todo_list")),
    path("admin/", admin.site.urls),
]
