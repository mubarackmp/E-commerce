from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Slogin(request):
    return render(request,'indexS.html')
