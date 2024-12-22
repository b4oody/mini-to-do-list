from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.models import Task


def home_page_view(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.prefetch_related("tags__tasks")
    context = {"tasks": tasks}
    return render(request, "home.html", context=context)


def toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("core:home")


class CreateTaskView(CreateView):
    model = Task
    fields = ["tags", "content", "deadline", "is_completed"]
    template_name = "create_task_form.html"
    success_url = reverse_lazy("core:home")


def tags_page_view(request: HttpRequest) -> HttpResponse:
    return render(request, "tags.html")
