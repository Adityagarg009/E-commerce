from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate ,login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'login.html')
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get ('password')
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
        #check if user has entered correct credentials
    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")
def about(request):
    return render(request,'about.html')
def like(request):
    return render(request,'like.html')
def shop(request):
    return render(request,'shop.html')