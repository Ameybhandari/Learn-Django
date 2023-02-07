from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('This is Home Page')
    return render(request, 'home.html') # Using template

def room(request):
    return render(request, 'room.html')
