from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('viewall/', views.viewTodos, name='viewall'),
    path('add/', views.addTodo, name='add'),
    path('delete/<int:todo_id>', views.deleteTodo, name='delete'),
    path('todo/<int:todo_id>', views.viewTodo, name='viewtodo'),
]
