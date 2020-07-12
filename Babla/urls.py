from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home, name ='babla_home'),
    path('register/',views.Second, name='Register'),
    path('<int:babla_id>/',views.detail,name='open')
]
