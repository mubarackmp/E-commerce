from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def maine(request):
    return render(request,'indexM.html')
