from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
#for authentification of certain pages - a user can acccess
from django.contrib.auth.decorators import login_required


def projects(request):
    projects = Project.objects.all()
    context = {"projects":projects}
    return render(request, 'projects/projects.html',context)


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project':projectObj, 'tags':tags,})

#if user is not login then user cannot see this page
@login_required(login_url='login')
def new_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            return redirect('projects')

    context = {'form':form}
    return render(request,'projects/add-new-project.html',context)


#if user is not login then user cannot see this page
@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES ,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request,'projects/add-new-project.html',context)


#if user is not login then user cannot see this page
@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {'object':project}

    if request.method == "POST":
        project.delete()
        return redirect('projects')

    return render(request,'projects/delete_template.html',context)