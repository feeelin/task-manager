from django.forms import ModelForm, TextInput, Textarea
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст задачи'
            })
        }
