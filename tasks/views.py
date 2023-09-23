from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import Tasks
from .forms import TasksForm

def tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/index.html',{
        'tasks' : tasks
    })

class UpdateTask(UpdateView):
    model = Tasks
    template_name = 'tasks/update.html'

    form_class = TasksForm

def create (request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Форма заполнена неверно'
            print(form)

    form = TasksForm()

    data = {
        'form' : form,
        'error': error
    }
    return render(request, 'tasks/create.html', data)
