from django.db import models
from django.db import models
from django.contrib.auth.models import User




class Person(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image    = models.ImageField(null=True)
    age = models.IntegerField("Age")
    home_town = models.CharField("Home Town", max_length=100)

    def __str__(self):
        return str(self.first_name)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField("Type of Room",max_length=255)
    photo = models.FileField()
    no_rooms= models.CharField(max_length=2)
    no_bedrooms = models.CharField(max_length=2)
    no_beds = models.CharField(max_length=2)
    desc = models.TextField()
    internet = models.BooleanField()
    kitchen = models.BooleanField()
    pets = models.BooleanField()
    price = models.FloatField("Price")
    city = models.CharField("City", max_length=100)
    state = models.CharField("State", max_length=100)
    # country = models.CharField("Country", max_length=100)
    Zipcode = models.CharField("Zip Code", max_length=20)
    avgrating = models.IntegerField("Average Rating",null=True)
    def __str__(self):
        return str(self.room_id)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.IntegerField("Rating")
    review = models.TextField("Review", null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.room_id)











