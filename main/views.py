from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Room, Review, Person
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
            return render(request,'dashboard.html')
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
            return render(request,'dashboard.html')

        else:
            return HttpResponse("something wend wrong")


def roomlistview(request):
    return render(request,'roomlistview.html')
    

def AddRoom(request):
    if request.method =="POST":
        user = request.user
        type = request.POST['type']
        city = request.POST['city']
        state = request.POST['state']
        price = request.POST['price']
    #   photo = request.FILES.get('photo', False)
        photo = request.FILES['upload']
        zipcode= request.POST['zipcode']
        print(user, type, city, state, price ,photo )

        Room(user=user,type=type,photo=photo,price=price,city=city,state=state,Zipcode=zipcode).save();
        return HttpResponse("something happened at there..")

