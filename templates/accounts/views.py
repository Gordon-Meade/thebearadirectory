from django.shortcuts import render
from django.urls import path
from .views import logout_view, login_view, signup_view

def logout_view(request):
    logout(request)
    # Redirect to some other page after logout
    return redirect('home') 
