from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h1>this is about the page</h1>")

def submit(request):
    return HttpResponse("<b></h1>you submitted data succesfully</b><h1>")