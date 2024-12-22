from django.urls import path

from core.views import (
    home_page_view,
    tags_page_view,
    toggle_status,
    CreateTaskView,
    UpdateTaskView,
)

urlpatterns = [
    path("", home_page_view, name="home"),
    path("<int:task_id>/", toggle_status, name="toggle_status"),
    path("create-task/", CreateTaskView.as_view(), name="create-task"),
    path("update-task/<int:pk>/", UpdateTaskView.as_view(), name="update-task"),
    path("tags/", tags_page_view, name="tags"),
]
app_name = "mini_to_do_list"
