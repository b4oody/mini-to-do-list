from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
    )

    class Meta:
        ordering = ["is_completed", "created_at"]

    def status_display(self):
        return "Completed" if self.is_completed else "In progress"

    def status_class(self):
        return "active" if self.is_completed else "inactive"

    def clean(self):
        super().clean()
        if self.deadline <= timezone.now().date():
            raise ValidationError({"deadline": "The due date cannot be in the past!"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"({self.content}): {self.status_display()}"
