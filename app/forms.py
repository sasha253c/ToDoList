"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from tasks.models import Task

import datetime


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class AddTask(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Name',
        }))

    description = forms.CharField(widget=forms.Textarea({
        'class': 'form-control',
        'placeholder': 'Description', 
        }),
                                  required=False)

    date = forms.DateField(widget=forms.DateInput({
        'class': 'form-control',
        'type':'date',
        'value': datetime.datetime.date(datetime.datetime.now()),
        }))

    #completed = forms.BooleanField(widget=forms.CheckboxInput({
    #    'class': 'form-control'
    #    }))

    class Meta:
        model = Task
        fields = '__all__'




#class AddTask(forms.Form):
#    name = forms.CharField(max_length=30)
#    description = forms.CharField(max_length=300)
#    date = forms.CharField(max_length=30)
#    completed = forms.CharField(max_length=10)