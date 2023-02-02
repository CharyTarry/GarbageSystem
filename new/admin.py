import imp
from django.contrib import admin
from .models import Garbage, GarbageRequest, User,Firm
from .models import AbstractUser

# Register your models here.
admin.site.register(Garbage)
admin.site.register (User)
admin.site.register (Firm)
admin.site.register (GarbageRequest)



