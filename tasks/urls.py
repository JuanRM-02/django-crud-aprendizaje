from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('tasks/', tasks, name='tasks'),
    path('new_task/', create_new_task, name='new_task'),
]
