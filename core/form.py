from django import forms

STATUS_CHOICES = [
    ("all", "All"),
    ("active", "Active"),
    ("completed", "Completed"),
]


class StatusFilterForm(forms.Form):
    STATUS_CHOICES = STATUS_CHOICES
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
