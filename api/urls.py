from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views
from .views import  FileUploadView

from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name='index'),
    path('html', views.html, name='html'),
    path('file', FileUploadView.as_view()),
]