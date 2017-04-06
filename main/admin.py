from django.contrib import admin
from .models import Person,Review,Room

# Register your models here.
admin.site.register(Person)
admin.site.register(Review)
admin.site.register(Room)