from django.db.models import Case, When, Value
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .forms import TaskForm
from .models import Task


class TodoListView(ListView):
    model = Task
    template_name = "app_todo_list/home.html"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


class TaskCreateView(CreateView):
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:home")
    template_name = "app_todo_list/task_form.html"


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy("todo_list:home")
    fields = "__all__"
    
    def get(self, request, *args, **kwargs):
        if kwargs["change_status"]:
            Task.objects.filter(pk=kwargs["pk"]).update(
                is_done=Case(
                    When(is_done=True, then=Value(False)), default=Value(True)
                )
            )
            return redirect("todo_list:home")
        else:
            return super().get(request, *args, **kwargs)
