from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task


def index(request):
    return render(request, 'index.html')


@login_required
def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(owner=request.user)
        if tasks.count() == 0:
            message = 'No projects found for this user yet'
        context = {
            'tasks': tasks,
            'message': message
        }
        return render(request, 'base/base.html', context)
    if request.user.is_anonymous:
        return redirect('login')


def addTodo(request):
    return render(request, 'base/add.html')


def deleteTodo(request):
    return render(request, 'base/delete.html')


def viewTodo(request):
    return render(request, 'base/viewtodo.html')

