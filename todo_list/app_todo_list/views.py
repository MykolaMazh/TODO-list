from django.shortcuts import render
from django.views.generic import ListView

from app_todo_list.models import Task


class TodoListView(ListView):
    model = Task
    template_name = 'app_todo_list/home.html'