from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_event(request):
    return render(request, 'events/create_event.html')

def logout_view(request):
    logout(request)
    return redirect("login")

def view_event(request):
    return render(request, 'events/view_event.html')