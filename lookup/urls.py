# ! Hier werden die URLS der Webseite gespeichert und mit der views.py verknüpft !

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
]
