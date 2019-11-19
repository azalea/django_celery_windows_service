Django celery Windows service
=============================
A demo Django project with celery running as a Windows service

Prerequisites
-------------

This project builds upon [celery's official Django example project](https://github.com/celery/celery/tree/4.4/examples/django/).

See [celery documentation](http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html) for a step-by-step guide to use celery with Django.

This README assumes that Python, Django, celery and RabbitMQ are already installed.

Installation
------------

### Install pywin32

pywin32 is needed for running celery as a Windows service.

Download and install [pywin32](http://sourceforge.net/projects/pywin32/files/pywin32/).

Please make sure the pywin32 version matches your Python version and the architecture your Python is built with (your Python can be 32-bit even if your OS is 64-bit). This information can be obtained by typing python in the command line. i.e.

    C:\>python
    Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
    >>>

### Clone this repository

You can either run the following in [Git Bash](https://desktop.github.com/)

    git clone git@github.com:azalea/django_celery_windows_service.git

Or click "Download ZIP" on the right sidebar, and decompress it. 

### Set up and run

Go to the directory

    cd django_celery_windows_service

Setup Django database

    python manage.py syncdb

Correctly set python scripts path.

It is usually the "Scripts" folder under your python's installation path

e.g. C:\Python27\Scripts

Either append it to your system's PATH,

or edit celery_service.py

    # in celery_service.py
    PYTHONSCRIPTPATH = r'C:\Python27\Scripts'

Install and start celery Windows service

    python acelery_service.py install
    python celery_service.py start

Start Django development server

    python manage.py runserver

### Check whether installation is successful

Two files: celery_service.log and celery.log should be found in the directory.
celery_service.log should contain the following information:

    Starting Celery service ...
    cwd: ****
    command: ****
    pid: ****

celery.log should contain something like the following:
    
    Connected to amqp://guest:**@127.0.0.1:5672//
    ...
    celery@melody ready.

Now when you visit [http://localhost:8000/add/1/2](http://localhost:8000/add/1/2)

celery.log should have the following:

    Received task: demoapp.tasks.add[****]
    Task demoapp.tasks.add[****] succeeded in 0.00399994850159s: 3

### Have fun!

You can play with urls like

[http://localhost:8000/add/123/456](http://localhost:8000/add/123/456)

[http://localhost:8000/mul/78/90](http://localhost:8000/mul/78/90)

### Stop and remove the celery Windows service

    python acelery_service.py stop
    python celery_service.py remove

