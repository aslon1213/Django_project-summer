from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from .utils import search_in_projects

def projects(request):
    projects, search_value = search_in_projects(request)
    context = {"projects":projects, 'search_value': search_value}
    return render(request, 'projects/projects.html',context)


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project':projectObj, 'tags':tags,})

@login_required(login_url='login')
def new_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            return redirect('account')

    context = {'form':form}
    return render(request,'projects/add-new-project.html',context)

@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES ,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form}
    return render(request,'projects/add-new-project.html',context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object':project}

    if request.method == "POST":
        project.delete()
        return redirect('account')

    return render(request,'projects/delete_template.html',context)