from django.shortcuts import render

# Create your views here.

def master (request):
    return render (request,'master.html')

def home_user (request):
    return render (request,'home.html')

def about_user (request):
    return render (request,'about.html')

def contact_user (request):
    return render (request, 'contact.html')