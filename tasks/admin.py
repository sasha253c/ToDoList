from django.contrib import admin
from tasks.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'completed', )
    search_fields = ('name', 'date', )
    list_filter = ('completed', )
    ordering = ('date', 'name',)


admin.site.register(Task, TaskAdmin)