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
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name='tasks',
    )

    class Meta:
        ordering = ["is_completed", "created_at"]

    def status_display(self):
        return "Виконано" if self.is_completed else "У процесі"

    def clean(self):
        super().clean()
        if self.deadline <= timezone.now().date():
            raise ValidationError({"deadline": "Дата виконання не може бути в минулому!"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"({self.content}): {self.status_display()}"
