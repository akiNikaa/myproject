# witaj/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('witaj/', views.hello, name='witaj'),
]