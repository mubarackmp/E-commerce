from django.urls import path
from . import views

app_name = 'sellers'

urlpatterns = [
    path('sl/',views.Slogin,name='slogin'),
]