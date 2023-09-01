from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def methodinfo(request):  
    return HttpResponse("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics developed by Guido van Rossum. It was originally released in 1991. Designed to be easy as well as fun, the name "Python" is a nod to the British comedy group Monty Python.:"+request.method)  
