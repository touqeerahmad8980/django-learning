from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm,UserRegister
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username= cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/dashboard/')
                else:
                    HttpResponse('User not active')
            else:
                HttpResponse('Invalid credentials')
    else:
        form = LoginForm()
    return render(request , 'index.html', {'form':form})
    

def dashboard(request):
    return render(request , 'dashboard.html')

def userRegister(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('/')
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form':form})
    