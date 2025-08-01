from django.shortcuts import render
from .models import Vacant
# Create your views here.

def home(request):
    vacants = Vacant.objects.all()
    return render(request , 'finder/index.html' , {'vacants': vacants})

def login(request):
    return render(request , 'finder/manager_login.html')

def signup(request):
    return render( request, 'finder/signup.html' )

def find_house(request):
    return render(request , 'finder/finder.html')

def dashboard(request):
    return(request , 'finder/manager_dashboard.html')
    
