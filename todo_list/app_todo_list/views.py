from django.db.models import Case, When, Value
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import TaskForm
from .models import Task, Tag


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

    def post(self, request, *args, **kwargs):
        if request.POST.get("change-task-status"):
            Task.objects.filter(pk=kwargs["pk"]).update(
                is_done=Case(
                    When(is_done=True, then=Value(False)), default=Value(True)
                )
            )
            return redirect("todo_list:home")
        else:
            return super().post(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:home")


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
    fields = "__all__"


class TagUpdateView(UpdateView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
    fields = "__all__"


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
