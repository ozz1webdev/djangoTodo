from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('createProject/', views.createProject, name='createProject'),
    path('delete/<int:todo_id>', views.deleteTodo, name='delete'),
]
