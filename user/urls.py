from django.urls import path
from . import views

urlpatterns=[
    path('master',views.master,name='master'),
    path('home',views.home_user,name='home'),
    path('about',views.about_user,name='about'),
    path('contact',views.contact_user,name='contact')
] 