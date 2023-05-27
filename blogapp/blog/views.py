from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")

def blogs(request):
    return render(request, "blogs.html")

def blog_details(request, id):
    return HttpResponse("Blog Details Page: " + str(id))



