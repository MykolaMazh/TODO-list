from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from app_todo_list.models import Task


class TodoListView(ListView):
    model = Task
    template_name = 'app_todo_list/home.html'

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")

class TaskCreateView(CreateView):
    model = Task
    fields = ['description', 'deadline', 'tags']
    success_url = reverse_lazy("todo_list:home")
