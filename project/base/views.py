from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Project
from .forms import createProjectForm, AddTaskForm
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def home(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(owner=request.user)
        if projects.count() == 0:
            message = 'No projects found for this user yet'
        else:
            message = ''
        context = {
            'projects': projects,
            'message': message
        }
        return render(request, 'base/base.html', context)
    if request.user.is_anonymous:
        return render(request, 'base/base.html')


@login_required
def createProject(request):
    if request.method == 'GET':
        form = createProjectForm()
        return render(request, 'base/createProject.html', {'form': form})

    if request.method == 'POST':
        form = createProjectForm(request.POST)
        projectName = request.POST.get('projectName')

        if Project.objects.filter(owner=request.user, projectName=projectName).exists():
            message = 'Project name already exists'
            context = {
                'message': message
            }
            return render(request, 'base/base.html', context)
        else:
            if form.is_valid():
                formProjectName = form.cleaned_data['projectName']
                formDescription = form.cleaned_data['description']
                Project.objects.create(owner=request.user, projectName=formProjectName, description=formDescription)

                messages.success(request, 'Project created successfully')
                return redirect('home')


@login_required
def projectDetail(request, project_id):
    selProject = Project.objects.get(pk=project_id)
    return render(request, 'base/projectDetail.html', {'project': selProject})


@login_required
def projectDelete(request, project_id):
    Project.objects.filter(pk=project_id).delete()
    messages.success =(request, 'Project deleted successfully')
    return redirect('home')


@login_required
def addtask(request, project_id):
    if request.method == 'GET':
        form = AddTaskForm()
        return render(request, 'base/addtask.html', {'form': form})
