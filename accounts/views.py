from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def index(request):
    """Return HTML file"""
    return render(request, 'index.html')

def logout(request):
    """Logs user out"""
    auth.logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect(reverse('index'))
