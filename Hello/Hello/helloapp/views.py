from django.shortcuts import render,HttpResponse

def show(request):
    return HttpResponse("<h1>Hello  world! </h1>")
# Create your views here.
