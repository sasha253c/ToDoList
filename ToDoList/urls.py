"""
Definition of urls for ToDoList.
"""

from datetime import datetime
from django.conf.urls import url, patterns

from django.views.generic.list import ListView

import app.forms
import app.views


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^todolist/$', app.views.todolist, name='todolist'),
    url(r'^todolist/addtask/$', app.views.addTask, name='addtask'),
    url(r'^change-completed/$', app.views.change_completed),
    url(r'^calendar/', include('django_bootstrap_calendar.urls')),

    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]