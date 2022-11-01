from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from tasks.forms import Task_form
from .models import Task

# Create your views here.


def index(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('tasks')
            except Exception as e:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': e})

        else:
            return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'Password do not match'})


def tasks(request):
    tasks = Task.objects.all()    
    return render(request, 'tasks.html', {'tasks': tasks})


def create_new_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': Task_form})
    else:
        try:
            form = Task_form(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except Exception as e:
            return render(request, 'create_task.html', {'form': Task_form, 'error': e})



def signout(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('tasks')
