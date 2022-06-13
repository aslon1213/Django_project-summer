from multiprocessing import context
from django.shortcuts import render, redirect
# Create your views here.de
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreation, updateProfileForm
from django.contrib.auth.decorators import login_required

def all_profiles(request):
    context = {'profiles':Profile.objects.all()}
    return render(request, 'users/all_profiles.html', context)


def singleprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'users/single_profile.html', context)


def loginPage(request):

    page = 'login'
    context = {'page':page}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('all_profiles')
        else:
            messages.error(request,"Wrong Password or Login")

    return render(request, 'users/login_and_registration.html', context)


def logoutUser(request):
    logout(request)
    messages.error(request,"User Logout")
    return redirect('login')


def registerUser(request):

    form = CustomUserCreation()

    page = 'registration'

    if request.method == "POST":
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was succesfully created')
            login(request,user)
            return redirect('update_account')
    else:
        messages.success(request, "An Error occurred during registration - Please Try Again")
    context = {'page':page, 'form': form}

    return render(request, 'users/login_and_registration.html',context)


@login_required(login_url='login')
def accountPage(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request, 'users/account.html', context)






@login_required(login_url='login')
def update_profile(request):
    profile = request.user.profile
    form = updateProfileForm(instance=profile)
    context = {'form':form}

    if request.method == "POST":
        form = updateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    return render(request, 'users/account_form.html', context)



def deleteProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()
    return redirect('all_profiles')


def delete_profile(request):
    profile = request.user.profile
    profile.detele()
    return redirect('all_profiles')