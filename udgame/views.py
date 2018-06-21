from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import random

GLOBAL_Entry = None
# Create your views here.

temp=0
x=0


def index(request):
    global temp
    temp=0
    global x
    x=random.randrange(1,101)
    return render(request, 'udgame/main.html', {})


def game(request):
    return render(request, 'udgame/game.html',{})

def plus_try(temp):
    
    temp=temp+1
    return temp

def playing_game(request):
    global x
    y=int(request.GET['number_x'])

    global temp
    temp=plus_try(temp)
    
    if temp<6:
        if x<y:
            return render(request,'udgame/down.html',{})
        elif x>y:
            return render(request,'udgame/up.html',{})
        elif x==y:
            return render(request,'udgame/win.html',{})
    elif temp==6:
        return render(request,'udgame/lose.html',{})
        
