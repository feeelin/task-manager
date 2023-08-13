from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')

    render_data = {
        'title': 'Главная страница',
        'tasks': tasks
    }

    return render(request, 'main/index.html', render_data)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Данные введены неправильно'

    form = TaskForm()
    render_data = {
        'title': 'Создание формы',
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', render_data)
