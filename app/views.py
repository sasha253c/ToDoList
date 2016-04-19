"""
Definition of views.
"""

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core import serializers

from django.db.models import Q

from _datetime import datetime, date, timedelta

from tasks.models import Task

from app.forms import AddTask, ChangeTask

def todolist(request, interval='all'):

    assert isinstance(request, HttpRequest)

    if request.method == 'GET' and 'search' in request.GET:
        search = request.GET['search']
        if not search:
           tasks = {}
        else:
           tasks = Task.objects.filter(Q(name__icontains=search) |
                                       Q(description__icontains=search) |
                                       Q(date__icontains=search))
        return render(request,
                      'app/todolist.html',
                      {
                          'title': 'ToDoList',
                          'year':datetime.now().year,
                          'message': "Hello",
                          'tasks': tasks,
                      })

    now = date.today()
    step = request.GET.get('step', timedelta(days=1))
    tasks = False
    gap = now
    if interval == 'today':
        gap = now
    elif interval == 'tomorrow':
        now += timedelta(days=1)
        gap = now
    elif interval == 'week':
        gap = now + timedelta(days=7)
    elif interval == 'month':
        gap = now + timedelta(days=31)
    elif interval == 'year':
        gap = now + timedelta(days=365)
    else:
        tasks = Task.objects.all()

    if not tasks:
        currentDay = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        nextDay = str(gap.year) + '-' + str(gap.month) + '-' + str(gap.day)
        tasks = Task.objects.filter(date__range=[currentDay, nextDay])

    return render(
        request,
        'app/todolist.html',
        {
            'title': 'ToDoList',
            'year':datetime.now().year,
            'message': "Hello",
            'tasks': tasks,

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
        results = {'success':True, 'name': Task.objects.get(id=id).name}
    return JsonResponse(results)


def deleteTask(request):
    result = {'success':False}
    if request.method == 'POST':
        try:
            id = request.POST.get('id', '')
            Task.objects.get(id=id).delete()
        except Exception:
            raise
        else:
            result = {'success':True}
    return JsonResponse(result)





def getTasksForCalendar(request):
    results = {'success':False}

    taskForDay = {}

    if request.method == 'GET':
        try:
            for task in Task.objects.filter(completed=False):
                date = str(task.date)
                if date in taskForDay:
                    taskForDay[date]['number'] += 1
                    taskForDay[date]['name'] += str(task.name) + '\n'
                else:
                    taskForDay[date] = {'number': 1, 'name': str(task.name)+'\n'}

        except Task.DoesNotExist:
            raise
        else:
            results['success'] = True
            results['name'] = 'GetLenTasksForDay'
        
        results['tasks'] = taskForDay
        #assert False;
    #results = {'success':True, 'name': 'GetLenTasksForDay', '2016-04-13': {'number': 5}}
    return JsonResponse(results)


def calendar(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    results = {'title': 'Calendar',

               'message':'Hello',
               'year':datetime.now().year,
               'tasks': Task.objects.all(),
              }
    return render(
        request,
        'app/calendar.html',
        results
    )


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
            'message':'My contact page.',
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
            'message':'My simple ToDoList',
            'year':datetime.now().year,
        }
    )
