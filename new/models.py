from audioop import reverse
from enum import unique
from django.db import models
from calendar import c
from pickle import FALSE, TRUE
from weakref import proxy
from django.contrib.auth.models import AbstractUser
from django.forms import DateField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here
#class AbstractUserManager(AbstractUser):
   
 #  def get_queryset(self, *args, **kwargs):
  #      return super().get_queryset(self, *args, **kwargs).filter(type=User.username)

#class UserManager(AbstractUserManager):
 # pass

class User(AbstractUser):
    class Category(models.TextChoices):
        COLLECTOR = "COLLECTOR","COLLECTOR"
        RECYCLER = "RECYCLER","RECYCLER"
    category=models.CharField(_("Category"),max_length=50,choices=Category.choices,default=Category.COLLECTOR)
    username = models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.username

class RecyclerManager(models.Manager):
     def __str__(self):
        return User.category=='RECYCLER'

class CollectorManager(models.Manager):
     def __str__(self):
        return User.category=='COLLECTOR'

class collector(User):
    objects = CollectorManager()

    class Meta:
        proxy=TRUE

class recycler(User):
    objects = RecyclerManager()

    class Meta:
        proxy=TRUE     

  
class Garbage(models.Model):

    class GarbageType(models.TextChoices):
        ORGANIC= 'ORGANIC', ('Organic')
        GLASS= 'GLASS', ('Glass')
        PAPER= 'PAPER', ('Paper')
        WOOD= 'WOOD', ('Wood')
        PLASTIC= 'PLASTIC', ('Plastic')
        ELECTRONIC= 'ELECTRONIC', ('Electronic')
        CLOTH= 'CLOTH', ('Cloth')
        METAL= 'METAL', ('Metal')
        

    class Accepted(models.TextChoices):
        REQUEST = "REQUEST","REQUEST"
        PENDING = "PENDING","PENDING"
        RECYCLED = "RECYCLED","RECYCLED"

    User = get_user_model()
    ID = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Date = models.DateTimeField(auto_now_add=True)
    Garbage_Type = models.CharField(
        max_length=20,
        choices=GarbageType.choices,
        default=GarbageType.PLASTIC,
    )
    Amount = models.CharField(null=TRUE, blank=TRUE,max_length=50)
    Status = models.CharField(
        max_length=20,
        choices=Accepted.choices,
        default=Accepted.REQUEST,
    )

    class Meta:
        ordering = ['Status']

    def __str__(self):
        return self.Garbage_Type

    
class Firm(models.Model):

    User = get_user_model()
    # ID = models.BigAutoField(primary_key=True,)
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=FALSE)
    Name = models.CharField(null=TRUE, blank=TRUE,max_length=50,unique=TRUE)
    Phone = models.CharField(null=TRUE, blank=TRUE,max_length=50)
    Address = models.CharField(max_length=50,unique=True,primary_key=True,default='35067-NAIROBI')


    def __str__(self):
        return self.Address

class GarbageRequest(Garbage):
    Address = models.ForeignKey(Firm, on_delete=models.CASCADE,null=FALSE)
    
    def __str__(self):
        return self.Garbage_Type


# Create your models here.
