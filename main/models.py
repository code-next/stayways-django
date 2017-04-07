from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    age = models.IntegerField("Age")
    home_town = models.CharField("Home Town", max_length=100)

    def __str__(self):
        return str(self.username)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField("Type of Room", max_length=10)
    photo = models.FileField()
    price = models.IntegerField("Price")
    city = models.CharField("City", max_length=100)
    state = models.CharField("State", max_length=100)
    country = models.CharField("Country", max_length=100)
    Zipcode = models.CharField("Zip Code", max_length=20)

    def __str__(self):
        return str(self.room_id)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.IntegerField("Rating")
    review = models.TextField("Review", null=True)

    def __str__(self):
        return str(self.room_id)











