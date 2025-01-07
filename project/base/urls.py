from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('createProject/', views.createProject, name='createProject'),
    path('projectDetail/<int:project_id>', views.projectDetail, name='projectDetail'),
    path('projectDelete/<int:project_id>', views.projectDelete, name='projectDelete'),
]
