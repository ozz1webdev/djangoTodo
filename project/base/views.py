from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'base/base.html')


def addTodo(request):
    return render(request, 'base/add.html')


def viewTodos(request):
    return render(request, 'base/viewall.html')


def deleteTodo(request):
    return render(request, 'base/delete.html')


def viewTodo(request):
    return render(request, 'base/viewtodo.html')

