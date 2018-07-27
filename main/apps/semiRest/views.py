from django.shortcuts import render, redirect
from apps.semiRest.models import *

def index(request):
    context ={
        'users': User.objects.all()
    }
    return render(request, "semiRest/users.html", context)

def new(request):
    return render(request, "semiRest/add.html")

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, "semiRest/edit.html", context)

def display(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, "semiRest/userdisplay.html", context)

def create(request):
    if User.objects.validate(request.POST):
        User.objects.register(request.POST)
        return redirect("home")
    else:
        return redirect("new_user_form")

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("home")

def update(request):
    if User.objects.validate_change(request.POST):
        user = User.objects.get(id=request.POST['id'])
        user.name=request.POST['name']
        user.email=request.POST['email']
        user.save()
        return redirect("home")
    else:
        return redirect("home")


