from django.http import HttpResponse
from django.template import loader
from quart import template_rendered
from django.contrib.auth.models import auth, User 
from django.shortcuts import render,redirect
from .models import signup

def index(request):
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')

def SignUp(request):
    return render(request, 'signup.html')

def reg(request):
    if request.method=="POST":      
        firstName= request.POST["fname"]
        lastName= request.POST["lname"]
        startUpName= request.POST["sname"]
        email= request.POST["email"]
        contactNumber=request.POST["number"]
        passwords=request.POST["password"]
        sign=signup.objects.create(firstName=firstName, lastName=lastName,startUpName=startUpName,email=email,contactNumber=contactNumber, password=passwords)
        sign.save()
        return redirect("/")
    else: 
        return render(request, 'signup.html')