from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tag
from django.contrib import messages
from .forms import ProjectForm, ReviewForm, TagForm
from django.contrib.auth.decorators import login_required
from .utils import search_in_projects, paginate_projects


def projects(request):

    projects, search_value = search_in_projects(request)
    projects, custom_page_range = paginate_projects(request, projects, 6)

    context = {"projects":projects, 'search_value': search_value, 'custom_pagination':custom_page_range}
    return render(request, 'projects/projects.html',context)


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.project = projectObj
        review.save()
        messages.success(request, 'Voted succesfully')
        return redirect('project', id = pk)

    reviewers = projectObj.get_reviewers()

    tags = projectObj.tags.all()
    projectObj.update_votes()
    return render(request, 'projects/single-project.html', {'project':projectObj, 
    'tags':tags, 
    'form':form, 
    'reviewers':reviewers})

@login_required(login_url='login')
def new_project(request):
    form = ProjectForm()
    if request.method == "POST":
        tags = request.POST.get('tags_field').split(',')
        for tag in tags:
            tag_split = tag.split(' ')
            tag = ''
            for t in tag_split:
                tag += t

        print("TAGS",tags)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            for tag in tags:
                tag, created = Tag.objects.get_or_create(name = tag)
                project.tags.add(tag)
            project.save()
            return redirect('account')

    context = {'form':form}
    return render(request,'projects/add-new-project.html',context)

@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    old_tags = project.tags.all()

    if request.method == "POST":
        tags = request.POST.get('tags_field').split(',')
        for tag in tags:
            index_of_tag = tags.index(tag)
            tag_split = tag.split()
            print(tag_split)
            tag = ''
            for t in tag_split:
                if t != "" or t != " ":
                    tag += t + " "
            tags[index_of_tag] = tag

        form = ProjectForm(request.POST, request.FILES ,instance=project)
        if form.is_valid():
            for tag in tags:
                tag, created = Tag.objects.get_or_create(name = tag)
                project.tags.add(tag)
            project.save()
            form.save()
            return redirect('account')

    context = {'form':form, 'project':project}
    return render(request,'projects/add-new-project.html',context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object':project}

    if request.method == "POST":
        project.delete()
        return redirect('account')

    return render(request,'projects/delete_template.html',context)


def add_tag(request):
    form = TagForm()

    context = {'form':form}

    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form}
    return render(request, 'projects/form.html', context)