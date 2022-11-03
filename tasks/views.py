from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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

@login_required
def tasks(request):
    tasks = Task.objects.filter(user = request.user)    
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def task(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Task, id=id, user=request.user)
        form = Task_form(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, id=id, user=request.user_id)
            #Manera de hacer update
            edit = Task_form(request.POST, instance=task)
            edit.save()
            return redirect(tasks)
        except Exception as e:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': e})
        
@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.finish_date = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

@login_required
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


@login_required
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
