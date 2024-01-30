from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import *

# Create your views here.
# def home(request):
#     return render (request,'indexB.html')
# signup

def signup_buyer(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists!!!!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                print("signup successfull")
                return redirect(login_buyer)
        else:
            print("wrong password")

    return render(request,'indexB.html')


def login_buyer(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(main)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(login_buyer)
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect(login_buyer)

def main(request):
    return render(request,'indexM.html')