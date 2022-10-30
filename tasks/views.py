from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def hello(request):
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
                return HttpResponse('User has been created')
            except Exception as e:
                print(e)
                return HttpResponse('Error creating user')
        else:
            return HttpResponse('Password do not match')
        
    