from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os.path




class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=100,default="")
    image    = models.FileField(default='/default/avatar.png')
    #age = models.IntegerField("Age")
    home_town = models.CharField("Home Town", max_length=100,default="")

    def __str__(self):
        return str(self.first_name)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField("Type of Room",max_length=255)
    wifi = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    ac= models.BooleanField(default=False)
    furnitured =models.BooleanField(default=False)
    #no_rooms= models.CharField(max_length=2)
    service = models.IntegerField(default=0)
    guest =models.IntegerField("no.of guests",default=1)
    no_bedrooms = models.IntegerField("no.of bed rooms",default=1)
    no_beds = models.IntegerField(default=1)
    title = models.CharField(max_length=255,default="Title")
    desc = models.TextField(default="")
    price = models.IntegerField("Price",default=0)
    city = models.CharField("City", max_length=100,default="")
    state = models.CharField("State", max_length=100,default="")
    # country = models.CharField("Country", max_length=100)
    Zipcode = models.CharField("Zip Code", max_length=20,default="")
    avgrating = models.IntegerField("Average Rating",default=0)
    def __str__(self):
        return str(self.title)

class Portfolio(models.Model):
    photo_id = models.AutoField(primary_key=True)
    photo = models.FileField(upload_to='room/')
    user = models.ForeignKey(User)
    room = models.ForeignKey(Room ,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.room.title)

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    Person = models.ForeignKey(Person)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.IntegerField("Rating",default=0)
    review = models.TextField("Review", null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.room_id)










