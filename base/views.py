from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'base/home.html')

def room(request):
    return render(request, 'base/rooms.html')