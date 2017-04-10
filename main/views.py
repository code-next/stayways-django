from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
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
    if request.method == "POST":
        place  = request.POST['place']
        rooms = Room.objects.filter(city = place).values()
        return render(request,'roomlistview.html',{'rooms' : rooms})
    if request.method == "GET":
        return render(request,'roomlistview.html',{'rooms': Room.objects.filter().values()})

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

def dashboard(request):
    if request.method == "GET":
        return render(request,"dashboard.html")

def room_detail(request,rid):
    room = Room.objects.get(room_id=rid)
    return render(request,'detail.html',{
        'room' : room
    })


def logout_view(request):
    logout(request)
    return redirect('/')