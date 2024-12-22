from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Task, Tag


def pagination(request: HttpRequest, queryset, items_per_page=5):
    """
    Функція для пагінації.

    Аргументи:
    request: HttpRequest - об'єкт запиту.
    queryset: QuerySet або список - дані, які потрібно розбити на сторінки.
    items_per_page: int - кількість елементів на сторінку (за замовчуванням 5).

    Повертає:
        page_obj: об'єкт пагінації для шаблону.
    """
    paginator = Paginator(queryset, items_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


def home_page_view(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.prefetch_related("tags__tasks")
    page_obj = pagination(
        request=request,
        queryset=tasks,
        items_per_page=5
    )
    context = {"page_obj": page_obj}
    return render(request, "home.html", context=context)


def toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("core:home")


class CreateTaskView(CreateView):
    model = Task
    fields = ["tags", "content", "deadline", "is_completed"]
    template_name = "task_form.html"
    success_url = reverse_lazy("core:home")


class UpdateTaskView(UpdateView):
    model = Task
    fields = ["tags", "content", "deadline", "is_completed"]
    template_name = "task_form.html"
    success_url = reverse_lazy("core:home")


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy("core:home")


def tags_page_view(request: HttpRequest) -> HttpResponse:
    tags = Tag.objects.all()
    page_obj = pagination(
        request=request,
        queryset=tags,
        items_per_page=3
    )
    return render(
        request,
        "tags.html",
        context={"page_obj": page_obj}
    )


class CreateTagView(CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tag_form.html"
    success_url = reverse_lazy("core:tags")


class UpdateTagView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "task_form.html"
    success_url = reverse_lazy("core:tags")


class DeleteTagView(DeleteView):
    model = Tag
    success_url = reverse_lazy("core:tags")
