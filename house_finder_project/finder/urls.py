from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home") , 
    path('manager_login.html/',views.login , name = "login") ,
    path('finder.html/',views.find_house , name = "find_house") ,
    path('signup.html/' , views.signup , name = "signup") ,
]