from django.shortcuts import render

def login(request):
    return render(request,'login.html')

def details(request):
    return render(request,'details.html')

# Create your views here.
