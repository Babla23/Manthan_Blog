from django.shortcuts import render
from Blog.models import Manthan
# Create your views here.

def Home(request):
    project = Manthan.objects
    return render(request, 'index.html', {'Man':project})

def register(request):
    return render(request, 'register.html')