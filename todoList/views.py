from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm,UserRegister,TodoItemForm
from django.http import HttpResponse
from .models import TodoItem


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
    todoList = TodoItem.objects.all().filter(user_id = request.user.id)
    return render(request , 'dashboard.html', {'todo_list':todoList})


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


def addItem(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user_id = request.user.id
            new_form.save()
            return redirect('/dashboard')
    else:
        form = TodoItemForm()
    return render(request, 'add-item.html', {'form':form})


def removeItem(request, id):
    item = TodoItem.objects.get(id=id)
    item.delete()
    return redirect('/dashboard')


def editItem(request, id):
    selectedItem = get_object_or_404(TodoItem, id=id)
    form = TodoItemForm(request.POST or None,instance=selectedItem)
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
            # item = TodoItem.objects.filter(id=id)
            # item.update(request.POST)
            return redirect('/dashboard')
    # else:
    #     form = TodoItemForm()
    return render(request, 'add-item.html', {'form':form, 'item':selectedItem})

    