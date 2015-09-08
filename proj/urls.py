from django.urls import path  # noqa
from demoapp import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('', views.home),
    path('add/<int:x>/<int:y>/', views.add),
    path('mul/<int:x>/<int:y>/', views.mul),
]
