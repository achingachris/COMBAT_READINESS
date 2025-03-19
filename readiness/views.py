from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Combat Readiness System Home")

# Create your views here.
