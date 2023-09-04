from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def methodinfo(request):  
    return HttpResponse("Welcome Indore.:"+request.method)  

