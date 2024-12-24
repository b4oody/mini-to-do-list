from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from core.form import StatusFilterForm
from core.models import Task, Tag


class HomePageView(ListView):
    model = Task
    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        tasks = Task.objects.prefetch_related("tags__tasks")
        form = StatusFilterForm(self.request.GET)
        if form.is_valid():
            status = form.cleaned_data.get("status")
            if status and status != "all":
                if status == "completed":
                    tasks = tasks.filter(is_completed=True)
                elif status == "active":
                    tasks = tasks.filter(is_completed=False)
        return tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = StatusFilterForm(self.request.GET)
        return context


class ToggleStatusView(View):
    @staticmethod
    def post(request: HttpRequest, task_id: id) -> HttpResponse:
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


class TagsListView(ListView):
    model = Tag
    template_name = "tags.html"
    paginate_by = 3


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
