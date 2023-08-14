from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('about.html',views.about,name='about'),
    path('like.html',views.like,name='like'),
    path('login.html',views.loginUser, name="login"),
    path('shop.html',views.shop,name='shop'),
]
