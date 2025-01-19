from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,"Todo_app/home.html")

def signup(request):
    if (request.method == "POST"):
        unm = request.POST.get("uname")
        eml = request.POST.get("email")
        pwd = request.POST.get("pwd")
        print(unm,eml,pwd)        
        obj = User.objects.create_user(unm,eml,pwd)
        obj.save()
        return redirect('signin')
    return render(request,"Todo_app/signup.html")

def signin(request):
    if(request.method == "POST"):
        unm = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        print(unm,pwd)
        user = authenticate(request,username = unm, password = pwd)
        if user is not None:
            login(request,user)
            return redirect('todo')
    return render(request,"Todo_app/signin.html")

@login_required
def todo(request):
    if(request.method == "POST"):
        tsk = request.POST.get("task")
        print(tsk)
        obj = models.Todo(title=tsk,user=request.user)
        obj.save()
    return render(request,"Todo_app/todo.html")

def signout(request):
    logout(request)
    return redirect('home')
# start youtube video from 39:47 and check why its not working after after adding task
