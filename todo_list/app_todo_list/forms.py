from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["description", "deadline", "tags"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "cols": 10}),
            "tags": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateInput(attrs={"type": "date"})
        }
