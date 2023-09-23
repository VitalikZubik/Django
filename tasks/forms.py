from .models import Tasks
from django.forms import ModelForm, TextInput, DateTimeInput, Select, Textarea

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'date_create', 'deadline', 'execution_status', 'date_execution', 'user']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя задачи'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание задачи'
            }),
            'date_create': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'дд.мм.гггг чч:мм:сс'
            }),
            'deadline': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Срок выполнения задачи'
            }),
            'execution_status': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус выполнения'
            }),
            'date_execution': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'дд.мм.гггг чч:мм:сс'
            }),
            'user': Select(attrs={
                'class': 'form-control',
            }),
        }

