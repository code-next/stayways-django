from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Room, Review, Person,Portfolio
from django.contrib.auth.decorators import login_required
import json
import math

# index page
def index(request):
    if request.method =="GET":
        if request.user.is_authenticated():
            person=Person.objects.get(user=request.user)
            return render(request, "index.html",{'onlineUser' : person})
        else:
            return render(request, "index.html")

# user registration
def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        print(username + password)
        regUser=User.objects.create_user(username,username, password,first_name=first_name,last_name=last_name)
        Person.objects.create(user=regUser,first_name=first_name,last_name=last_name)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            person=Person.objects.get(user=regUser)
            return render(request,'index.html',{'onlineUser' : person})
        else:
            return HttpResponse("something wend wrong")

# user login
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            person=Person.objects.get(user=user)
            return render(request,'index.html',{'onlineUser' : person})

        else:
            return HttpResponse("something wend wrong")

# review adding
def AddReview(request):
    if request.method == "POST":
        rating = request.POST['rating']
        review = request.POST['review']
        room_id= request.POST['roomId']
        room = Room.objects.get(room_id=room_id)
        person= Person.objects.get(user=request.user)
        rev = Review(review=review,rating=rating,user=request.user,room=room,Person=person)
        rev.save()
        reviews = Review.objects.filter(room=room)
        count =reviews.count()
        sum=0
        avg =0
        for r in reviews:
            sum += r.rating
        if count !=0:
            avg = sum/count

        room.avgrating = avg
        room.save()
        return render(request,'ajax_review.html',{'review' : rev})

# viewing room list
def roomlistview(request):
    if request.method == "POST":
        place  = request.POST['place']
        place = place.strip()
        place = place.upper()
        rooms = Room.objects.filter(city = place)
        roomObj=[]
        for item in rooms:
            tTemp={}
            reviews=Review.objects.filter(room=item.room_id)
            photo = Portfolio.objects.filter(room=item.room_id)[0]
            rcount = reviews.count()
            tTemp['room']=item
            tTemp['rcount']=rcount
            tTemp['photo']=photo
            roomObj.append(tTemp)
            
        return render(request,'roomlistview.html',{'roomObj' : roomObj, 'city': place,'rooms':rooms})
    return redirect('/')

# room adding
@login_required
def AddRoom(request):
    if request.method =="POST":
        

        user = request.user
        title = request.POST['title'].strip()
        desc = request.POST['desc'].strip()
        type = request.POST['type'].strip()
        wifi = False if 'wifi' not in request.POST else True
        furnitured =False if 'furnitured' not in request.POST else True
        kitchen = False if 'kitchen' not in request.POST else True
        petsallowed = False if 'petsallowed' not in request.POST else True
        ac = False if 'ac' not in request.POST else True
        bedroom = request.POST['bedroom'].strip()
        bed = request.POST['bed'].strip()
        guest = request.POST['guest'].strip()
        city = request.POST['city'].strip()
        state = request.POST['state'].strip()
        service = request.POST['service'].strip()
        price = request.POST['price'].strip()
        zipcode= request.POST['zipcode'].strip()
        city = city.upper()
        state = state.upper()
        type = type.upper()
        price = int(service)+int(price)

        room = Room.objects.create(
            user=user,
            title=title,
            desc=desc,
            type=type,
            wifi=wifi,
            furnitured=furnitured,
            kitchen=kitchen,
            pets=petsallowed,
            ac=ac,
            no_bedrooms=bedroom,
            no_beds=bed,
            guest=guest,
            service=service,
            price=price,
            city=city,
            state=state,
            Zipcode=zipcode
            )

        files = request.FILES.getlist('uploads')
        for file in files:
            Portfolio.objects.create(user=user,photo=file,room=room)
        return redirect("/dashboard/")

#room filtering
def ajax_roomfilter(request):
    if request.method =="POST":
        place  = request.POST['roomlistCity']
        li=[]
        if 'roomlistPrivate' in request.POST:
            li.append('PRIVATE')
        if 'roomlistShared' in request.POST:
            li.append('SHARED')
        if 'roomlistEntire' in request.POST:
            li.append('ENTIRE')
        if 'roomlistHostel' in request.POST:
            li.append('HOSTEL')
        if not li:
            li = ['PRIVATE','SHARED','ENTIRE','HOSTEL']    
        wifi = False if 'roomlistWifi' not in request.POST else True
        furnitured =False if 'roomlistFurnitured' not in request.POST else True
        kitchen = False if 'roomlistKitchen' not in request.POST else True
        petsallowed = False if 'roomlistPets' not in request.POST else True
        ac = False if 'roomlistAc' not in request.POST else True
        if wifi == False and furnitured == False and kitchen == False and petsallowed == False and ac == False:
            rooms = Room.objects.filter(city = place)
            itemlist=[room for room in rooms if room.type in li]
           
        else:
            rooms = Room.objects.filter(city = place)
            roomlist=[room for room in rooms if room.type in li]
            if wifi == True and furnitured == True and kitchen == True and petsallowed ==True and ac == True:
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True and aRoom.furnitured == True and aRoom.kitchen == True and aRoom.pets == True and aRoom.ac == True ]  
            elif wifi == True and furnitured == False and kitchen == False and petsallowed ==False and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True]
            elif wifi == True and furnitured == True and kitchen == False and petsallowed ==False and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True and aRoom.furnitured == True ]
            elif wifi == True and furnitured == True and kitchen == True and petsallowed ==False and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True and aRoom.furnitured == True and aRoom.kitchen == True ]
            elif wifi == True and furnitured == True and kitchen == True and petsallowed == True and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True and aRoom.furnitured == True and aRoom.kitchen == True and aRoom.pets == True]
            elif wifi == True and furnitured == True and kitchen == False and petsallowed == True and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True  and aRoom.pets == True and aRoom.furnitured == True]
            elif wifi == True and furnitured == False and kitchen == True and petsallowed == True and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True and aRoom.kitchen == True and aRoom.pets == True and aRoom.ac == True]
            elif wifi == True and furnitured == False and kitchen == False and petsallowed == True and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True and aRoom.petsallowed == True and aRoom.ac == True]
            elif wifi == True and furnitured == False and kitchen == False and petsallowed == False and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.wifi == True and aRoom.ac == True]

            elif wifi == False and furnitured == True and kitchen == False and petsallowed == False and ac == False :    
                itemlist=[aRoom for aRoom in roomlist if aRoom.furnitured == True]
            elif wifi == False and furnitured == True and kitchen == True and petsallowed == False and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.furnitured == True and aRoom.kitchen == True]
            elif wifi == False and furnitured == True and kitchen == True and petsallowed == True and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.furnitured == True and aRoom.kitchen == True and aRoom.pets ==True]
            elif wifi == False and furnitured == True and kitchen == True and petsallowed == True and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.furnitured == True and aRoom.kitchen == True and aRoom.pets ==True and aRoom.ac == True]
            elif wifi == False and furnitured == True and kitchen == False and petsallowed == True and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.furnitured == True and aRoom.petsallowed == True and aRoom.ac == True]
            elif wifi == False and furnitured == True and kitchen == False and petsallowed == False and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.furnitured == True and aRoom.ac == True]
            elif wifi == False and furnitured == True and kitchen == False and petsallowed == True and ac == False :  
                itemlist=[aRoom for aRoom in roomlist if aRoom.furnitured == True and aRoom.petsallowed == True]

            elif wifi == False and furnitured == False and kitchen == True and petsallowed == False and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.kitchen == True]
            elif wifi == False and furnitured == False and kitchen == True and petsallowed == True and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.kitchen == True and aRoom.pets == True]
            elif wifi == False and furnitured == False and kitchen == True and petsallowed == True and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.kitchen == True and aRoom.pets == True and aRoom.ac == True]
            elif wifi == False and furnitured == False and kitchen == True and petsallowed == False and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.kitchen == True and aRoom.ac == True]

            elif wifi == False and furnitured == False and kitchen == False and petsallowed == True and ac == False :
                itemlist=[aRoom for aRoom in roomlist if aRoom.pets == True]
            elif wifi == False and furnitured == False and kitchen == False and petsallowed == True and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.pets == True and aRoom.ac == True]

            elif wifi == False and furnitured == False and kitchen == False and petsallowed == False and ac == True :
                itemlist=[aRoom for aRoom in roomlist if aRoom.ac == True]

                

        roomObj=[]
        for item in itemlist:
            tTemp={}
            reviews=Review.objects.filter(room=item.room_id)
            photo = Portfolio.objects.filter(room=item.room_id)[0]
            rcount = reviews.count()
            tTemp['room']=item
            tTemp['rcount']=rcount
            tTemp['photo']=photo
            roomObj.append(tTemp)
        return render(request,'ajax_roomfilter.html',{'roomObj' : roomObj})

# dashboard
@login_required
def dashboard(request):
    if request.method == "GET":
        return render(request,"dashboard.html")
        
# room detail view
def room_detail(request,rid):
    room = Room.objects.get(room_id=rid)
    reviews = Review.objects.filter(room=rid)
    rcount = reviews.count()
    host   = Person.objects.get(user=room.user)
    photos = Portfolio.objects.filter(room=room.room_id)
    monthlyCharge = room.price - room.service
    return render(request,'detail.html',{
        'monthlyCharge':monthlyCharge,
        'host':host,
        'room' : room,
        'reviews' :reviews,
        'count' :rcount,
        'photos':photos
    })

#user logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

# autocomplete search
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


