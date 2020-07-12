from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='blog_home'),
    path('debug/',views.debug,name='Login'),
    path('<slug:blog_slug>/',views.view,name = 'new')
]