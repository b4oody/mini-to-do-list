from django.contrib import admin

from core.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "get_tags",
        "content",
        "created_at",
        "deadline",
        "status_display",
    ]
    list_filter = [
        "tags__name",
        "content",
        "created_at",
        "deadline",
    ]
    search_fields = [
        "tags__name",
        "content",
        "created_at",
        "deadline",
        "status_display",
    ]

    @staticmethod
    def get_tags(obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
