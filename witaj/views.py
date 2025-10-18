from django.shortcuts import render

# Create your views here.
# witaj/views.py

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Witaj w Django!")