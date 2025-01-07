from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, project
from .forms import createProjectForm


def index(request):
    return render(request, 'index.html')


@login_required
def home(request):
    if request.user.is_authenticated:
        projects = project.objects.filter(owner=request.user)
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
        return render('base/base.html')


@login_required
def createProject(request):
    if request.method == 'GET':
        form = createProjectForm()
        return render(request, 'base/createProject.html', {'form': form})

    if request.method == 'POST':
        form = createProjectForm(request.POST)
        projectName = request.POST.get('projectName')

        if project.objects.filter(owner=request.user, projectName=projectName).exists():
            message = 'Project name already exists'
            context = {
                'message': message
            }
            return render(request, 'base/base.html', context)
        else:
            if form.is_valid():
                formProjectName = form.cleaned_data['projectName']
                formDescription = form.cleaned_data['description']
                project.objects.create(owner=request.user, projectName=formProjectName, description=formDescription)

                message = 'Project created successfully'                
                context = {
                    'message': message
                }
                return render(request, 'base/base.html', context)


@login_required
def projectDetail(request, project_id):
    selProject = project.objects.get(pk=project_id)
    return render(request, 'base/projectDetail.html', {'project': selProject})


@login_required
def projectDelete(request, project_id):
    project.objects.filter(pk=project_id).delete()
    return redirect('home')
