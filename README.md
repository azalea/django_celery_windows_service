Django celery Windows service
=============================
A demo Django project with celery running as a Windows service

Prerequisites
-------------

This project builds upon [celery's official Django example project](https://github.com/celery/celery/tree/4.4/examples/django/).

See [celery documentation](http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html) for a step-by-step guide to use celery with Django.

This README assumes that Python >= 3.6 and RabbitMQ are already installed, and `rabbitmq-server` is running on `localhost`.

Installation
------------

### Clone this repository

You can either run the following in [Git Bash](https://desktop.github.com/)

    git clone git@github.com:azalea/django_celery_windows_service.git

Or click "Download ZIP" on the right sidebar, and decompress it.

### Install pywin32, Django 2, celery 4, eventlet and other dependencies

pywin32 is needed for running celery as a Windows service.

Other dependencies are inherited from the offical django example project.

eventlet is required for celery 4 to run on Windows. See discussions [1](https://stackoverflow.com/questions/37255548/how-to-run-celery-on-windows/47331438#47331438) [2](https://github.com/celery/celery/issues/4082)

Install by the following steps:

Go to the repository

    cd django_celery_windows_service

Create a virtual env named `venvcelery`

    path_to\python -m venv venvcelery
    venvcelery\Scripts\activate

Install

    pip install -r requirements.txt

Copy `pywintypes36.dll` to correct location. [ref](https://stackoverflow.com/questions/41200068)

    cp venvcelery\Lib\site-packages\pywin32_system32\pywintypes36.dll venvcelery\Lib\site-packages\win32

### Set up and run

Setup Django database

    python manage.py migrate

Correctly set python scripts path, which is `path_to\venvcelery\Scripts`

Edit celery_service.py

    # in celery_service.py
    PYTHONSCRIPTPATH = r'path_to\venvcelery\Scripts'

Install and start celery Windows service

    python celery_service.py install
    python celery_service.py start

Start Django development server

    python manage.py runserver

### Check whether installation is successful

Two files `celery_service.log` and `celery.log` should be found in the current directory.

`celery_service.log` should contain the following information:

    Starting Celery service ...
    cwd: ****
    command: ****
    pid: ****

`celery.log` should contain something like the following:
    
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

    python celery_service.py stop
    python celery_service.py remove


---------------

An older version of this demo project with Python 2.7, Django 1.6 and celery 3.1 is in branch [celery3](https://github.com/azalea/django_celery_windows_service/tree/celery3)