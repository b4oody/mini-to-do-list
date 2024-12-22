from django.urls import path

from core.views import (
    home_page_view,
    tags_page_view,
    toggle_status,
    CreateTaskView,
    UpdateTaskView,
    DeleteTaskView,
    CreateTagView,
    UpdateTagView,
    DeleteTagView,
)

urlpatterns = [
    path("", home_page_view, name="home"),
    path("<int:task_id>/", toggle_status, name="toggle_status"),
    path("create-task/", CreateTaskView.as_view(), name="create-task"),
    path("update-task/<int:pk>/", UpdateTaskView.as_view(), name="update-task"),
    path("delete/<int:pk>/", DeleteTaskView.as_view(), name="delete-task"),
    path("tags/", tags_page_view, name="tags"),
    path("create-tag/", CreateTagView.as_view(), name="create-tag"),
    path("update-tag/<int:pk>/", UpdateTagView.as_view(), name="update-tag"),
    path("delete-tag/<int:pk>/", DeleteTagView.as_view(), name="delete-tag"),
]
app_name = "mini_to_do_list"
