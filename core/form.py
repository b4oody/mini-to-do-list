from django import forms

STATUS_CHOICES = [
    ("all", "Всі статуси"),
    ("active", "Активні"),
    ("completed", "Завершені"),
]


class StatusFilterForm(forms.Form):
    STATUS_CHOICES = STATUS_CHOICES
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
