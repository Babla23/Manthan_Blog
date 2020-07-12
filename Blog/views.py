from django.shortcuts import render, get_object_or_404
from Blog.models import Manthan

def home(request):
    project = Manthan.objects
    return render(request, 'Blog/index.html', {'Man':project})

def debug(request):
    return render(request, 'Blog/debug.html')

def view(request,blog_slug):
    blog = Manthan.objects.get(slug=blog_slug)
    return render(request,'Blog/detail.html',{'full_blog':blog})