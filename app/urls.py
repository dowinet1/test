from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index),
    path('iniciosesion/', views.iniciosesion),
    path('cerrarsesion/', views.cerrarsesion),
    path('testuno/', views.testuno),
   # path('testdos/', views.testdos),
]