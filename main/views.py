from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import models
from . import forms 



def index(request):
    if request.method =="GET":
        return render(request, "index.html")

def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username + password)
        User.objects.create_user(username,username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse("you are logged in")
        else:
            return HttpResponse("something wend wrong")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse("you are logged in")

        else:
            return HttpResponse("something wend wrong")


def roomlistview(request):
    return render(request,'roomlistview.html')
