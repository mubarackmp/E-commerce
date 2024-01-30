from django.urls import path
from buyers import views

app_name = 'buyers'

urlpatterns = [
    # path('bl/',views.home,name='blogin'),
    path('m/',views.main,name='maine'),
    path('home/',views.signup_buyer,name='signup_buyer'),
    path('login/',views.login_buyer,name='login_buyer'),
]