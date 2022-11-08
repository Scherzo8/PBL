from curses import meta
from django.shortcuts import render
from home import models

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        print(name + ", " + email + ", " + username + ", " + password)
        models.Contact(name=name, email=email,
                       username=username, password=password).save()
        print('Hello')
        return render(request, 'login.html')
    elif request.method == 'GET':
        return render(request, 'register.html')
    else:
        print("Hello")

def test(request):
    return render(request, 'test.html')
