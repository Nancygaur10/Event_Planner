from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        username=request.POST['username']
        role=request.POST.get('role')
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')  
         
        user=CustomUser.objects.create_user(username=username, role=role, password=password1)
        user.profile.role=role
        user.profile.save()
        return redirect("index")
    return render(request, 'accounts/signup.html') 

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == "admin":
                return redirect("admin_dashboard")
            else:
                return redirect("user_dashboard")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")

@login_required
def user_dashboard(request):
    return render(request, "accounts/user_dashboard.html")


