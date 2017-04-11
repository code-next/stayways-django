from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Room, Review, Person
from django.contrib.auth.decorators import login_required
import json
import math


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

# @login_required
# def roomlistview(request):
#     if request.method == "POST":
#         place  = request.POST['place']
#         rooms = Room.objects.all()

#         class Empty:
#             id =0
#             room =0
#             avg = 0
#             count=0

#         data =[]
#         if rooms:
#             print("ntho ind akath")
#         for room in rooms:
#             avg = 0
#             reviewcount = Review.objects.filter(room=room.room_id).count()
#             ratings = Review.objects.filter(room=room.room_id)
#             norating =0
#             for rating in ratings:
#                 norating += rating.rating
#             if reviewcount != 0:
#                 avg=norating/reviewcount
#             obj= Empty()
#             obj.id = room.room_id
#             obj.avg = math.floor(avg)
#             obj.room = room
#             obj.count = reviewcount
#             data.append(obj)
#         for i in data:
#             print(i.id)
#             print(i.avg)
#         return render(request,'roomlistview.html',{'rooms' : data,


#                                                    })


#     if request.method == "GET":
#         rooms = Room.objects.all()

#         class Empty:
#             id = 0
#             room = 0
#             avg = 0
#             count = 0

#         data = []
#         if rooms:
#             print("ntho ind akath")
#         for room in rooms:
#             avg = 0
#             reviewcount = Review.objects.filter(room=room.room_id).count()
#             ratings = Review.objects.filter(room=room.room_id)
#             norating = 0
#             for rating in ratings:
#                 norating += rating.rating
#             if reviewcount != 0:
#                 avg = norating / reviewcount
#             obj = Empty()
#             obj.id = room.room_id
#             obj.avg = math.floor(avg)
#             obj.room = room
#             obj.count = reviewcount
#             data.append(obj)
#         for i in data:
#             print(i.id)
#             print(i.avg)
#         return render(request,'roomlistview.html',{'rooms': data})



def roomlistview(request):
    if request.method == "POST":
        place  = request.POST['place']
        place = place.strip()
        place = place.upper()
        rooms = Room.objects.filter(city = place).values()  
        return render(request,'roomlistview.html',{'rooms' : rooms, 'city': place})

@login_required
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
        city = city.strip()
        price = price.strip()
        zipcode = zipcode.strip()
        state = state.strip()
        city = city.upper()
        state = state.upper()
        Room(user=user,type=type,photo=photo,price=price,city=city,state=state,Zipcode=zipcode).save();
        return HttpResponse("something happened at there..")


@login_required
def dashboard(request):
    if request.method == "GET":
        return render(request,"dashboard.html")
        
def room_detail(request,rid):
    room = Room.objects.get(room_id=rid)
    return render(request,'detail.html',{
        'room' : room
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def ajax_getCity(request):
    if request.is_ajax():
        search_text = request.GET.get('term', '')
        search_text = search_text.upper()
        rooms = Room.objects.filter(city__icontains = search_text)
        results = []
        for room in rooms:
            city = room.city
            city = city.title()
            city_json = {}
            city_json['label'] = city
            city_json['value'] = city
            try:
                index = results.index(city_json)
            except ValueError:
                index = -1

            if index == -1:
                results.append(city_json)
        data = json.dumps(results)
        
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)