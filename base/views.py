from django.shortcuts import render
#from django.http import HttpResponse

from .models import Room
# Create your views here.

# rooms = [
#     {'id':1, 'name':'lets learn python'},
#     {'id':2, 'name':'Design with me '},
#     {'id':3, 'name':'Front end development'},
# ]

def home(request):
    rooms = Room.objects.all()
    #return HttpResponse('This is the Home Page') using httpresponse
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context) # Using template

def room(request, pk):
    rooms = Room.objects.get(id=pk)
    context = {'room':rooms}
    return render(request, 'base/room.html',context)