from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'dashboard.html')