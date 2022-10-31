from django.urls import path

from .views import *


urlpatterns = [
    path('', hello, name='index'),
    path('signup/', signup, name='signup'),
    path('tasks/', tasks, name='tasks'),
]
