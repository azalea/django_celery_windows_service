from __future__ import absolute_import, unicode_literals

# Create your views here.
from django.http import HttpResponse
import demoapp.tasks as tasks

def home(request):
    return HttpResponse('Try:<br>'
                        'http://localhost:8000/add/1/2<br>'
                        'or:<br>'
                        'http://localhost:8000/mul/1/2'
                        )

def add(request, x, y):
    tasks.add.delay(x, y)
    return HttpResponse('task add is scheduled.')


def mul(request, x, y):
    tasks.mul.delay(x, y)
    return HttpResponse('task mul is scheduled.')
