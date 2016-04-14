"""
Definition of views.
"""

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core import serializers


from datetime import datetime

from tasks.models import Task

from app.forms import AddTask


def todolist(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/todolist.html',
        {
            'title': 'ToDoList',
            'year':datetime.now().year,
            'message': "Hello",
            'tasks': Task.objects.all(),

        }
    )

def addTask(request):
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            description = request.POST.get('description', '')
            date = request.POST.get('date', '')
            completed = request.POST.get('completed', False)
            task = Task(name=name, description=description, date=date, completed=completed)
            task.save()
            return render(request, 'app/thanks.html', {'title':'Thanks', 'year':datetime.now().year, 'message': 'task added',})
    else:
        form = AddTask()
    return render(request, 'app/addtask.html', {'form': form, 'title':'AddTask', 'year':datetime.now().year, 'massage': 'addtask',})


def change_completed(request):
    results = {'success':False}
    if request.method == 'POST':
        
        id = request.POST.get('id', '')
        try:
            task = Task.objects.get(id=id)
            task.completed = not task.completed
            task.save()
        except Task.DoesNotExist:
            raise

        #chenge db

        results = {'success':True, 'name': Task.objects.get(id=id).name}
    return JsonResponse(results)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
