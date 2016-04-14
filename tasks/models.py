from django.db import models
from django.contrib import admin

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200,
                                   blank=True)

    date = models.DateField()

    completed = models.BooleanField(max_length=10,
                                    blank=True
                                    )

    def __str__(self):
        return 'Name: %s, Date: %s' % (self.name, self.date)

    class Meta:
        ordering = ['name']