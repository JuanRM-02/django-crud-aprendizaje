from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('tasks/', tasks, name='tasks'),
    path('new_task/', create_new_task, name='new_task'),
    path('task/<int:id>', task, name='task'),
    path('task/<int:id>/complete', complete_task, name='complete_task'),
    path('task/<int:id>/delete', delete_task, name='delete_task'),
]
