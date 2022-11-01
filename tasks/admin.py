from django.contrib import admin

# Register your models here.
from .models import Task


class Task_admin(admin.ModelAdmin):
    readonly_fields = ('creation_date', )

admin.site.register(Task, Task_admin)