from email.headerregistry import Address
from tokenize import Name
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ast import If, Pass
from cmath import e
import imp
from unicodedata import category
from django.shortcuts import redirect, render
from new import models
from .import views
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from new.models import CollectorManager, Garbage, GarbageRequest, RecyclerManager,Firm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


# Create your views here.
def landing(request):
    return render(request, 'new/landing.html')

def collector(request):
    User = get_user_model()
    username = request.user.username
    posts= models.Garbage.objects.filter(username=(User.objects.get(username=username)))
    User=get_user_model()
    if request.method == "POST":
        #username= request.POST(User.get(username))
        Garbage_Type = request.POST['category']
        Amount = request.POST['amount']
        username = request.user.username
        ins = Garbage(Garbage_Type=Garbage_Type,Amount=Amount,username=(User.objects.get(username=username)))     
        inse = GarbageRequest(Garbage_Type=Garbage_Type,Amount=Amount,username=(User.objects.get(username=username))) 
        ins,inse.save()
        #inse.save()

        messages.info(request,"Successfully added")
        return redirect('collector')
    else:
        return render(request, 'new/collector.html',{'posts':posts})

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        category = request.POST['category']
        password = request.POST['password']

        User = get_user_model()

        if User.objects.filter(email=email).exists():
            messages.info(request,"A user with this email already exists")
            return redirect('signup')
        else:
          user = User.objects.create_user(username=email,first_name=fname,last_name=lname,email=email,password=password,category=category)
          user.save()
          messages.info(request,"Account has been created successfully")
          return redirect('login')
    else:
        return render(request, 'new/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        User = get_user_model()
        user= authenticate(username=email,password=password)
        if user:
    
            auth.login(request,user)   
            if User.objects.get(email=email).category=='recycler':
               return redirect('recycler')
            
            else: 
              return redirect('collector')

        else:
           messages.error(request,"Invalid credentials")
           return redirect('login')
    else:     
        return render(request, 'new/login.html')

def recycler(request):
    garbage_list = Garbage.objects.all()
    User = get_user_model()
    if request.method == "POST":
        Name = request.POST['name']
        Phone = request.POST['phone']
        Address = request.POST['address']
        # if User.objects.get(username=username):
        username = request.user.username
        print(User.objects.get(username=username))
        if Firm.objects.filter(Name=Name).exists():
            messages.info(request,"This firm was already registered")
            return redirect('recycler')

        else:
            ins = Firm(Name=Name,Phone=Phone,Address=Address,username=(User.objects.get(username=username)))      
            ins.save()
            messages.info(request,"Successfully added")
            return redirect('recycler')
    else:
        return render(request, 'new/recycler.html',{'garbage_list':garbage_list})

def myposts(request):
    User = get_user_model()
    username = request.user.username
    print(username)
    posts= models.Garbage.objects.filter(username=(User.objects.get(username=username)))
    return render(request, 'new/myposts.html',{'posts':posts})

def sendrequest(request,ID=None,):
    update= Garbage.objects.get(ID=ID)
    update.Status='PENDING'
    update.save()
    messages.info(request,"Request sent")
    User = get_user_model()
    username = request.user.username
    hey = Firm.objects.get(username=username)
    upsy = GarbageRequest.objects.get(ID=ID)
    upsy.Address = hey
    #a=Firm.objects.all()
    #print(a)
    #b= Firm.objects.name
    #print(b)
    #upsy.Address = Firm.objects.get(Address)
    print(upsy)
    upsy.save()
    return HttpResponse(status=204)

def garbagerequests(request,ID=None):
    #update= Garbage.objects.get(ID=ID)
    #update.Status='RECYCLED'
    #update.save()
    #if models.Garbage.objects.filter(Status='PENDING'):

    requests = models.GarbageRequest.objects.filter(Status='PENDING')
    print(requests)
    #{'requests':requests}
    return render(request,'new/garbagerequests.html',{'requests':requests})

def acceptgarbreq(request,ID=None):
    update= Garbage.objects.get(ID=ID)
    update.Status='RECYCLED'
    update.save()
    messages.info(request,"Request Accepted")
    return HttpResponse(status=204)

def firm(request):
    User = get_user_model()
    username = request.user.username
    print(username)
    firms= models.Firm.objects.filter(username=(User.objects.get(username=username)))
    return render(request,'new/firm.html',{'firms':firms})

def myrequests(request):
    User = get_user_model()
    username = request.user.username
    print(username)
    myreq= models.GarbageRequest.objects.filter(Address=(Firm.objects.get(username=username)))
    return render(request,'new/myrequests.html',{'myreq':myreq})
    
def delgarb(request,ID=None):
    delg= Garbage.objects.get(ID=ID)
    delg.delete()
    messages.info(request,"Item has been successfully deleted")
    return HttpResponse(status=204)

def delfirm(request,Name=None):
    delf= Firm.objects.get(Name=Name)
    delf.hide()
    messages.info(request,"Firm has been successfully deleted")
    return HttpResponse(status=204)

def cancelreq(request,ID=None):
    canc= GarbageRequest.objects.get(ID=ID)
    canc.Status='REQUEST'
    canc.save()
    messages.info(request,"canceled")
    return HttpResponse(status=204)




