from django.shortcuts import render, redirect
from .models import Accounts
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def accounts(request):
    return render(request,'accounts/accounts.html')

def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is invalid'})

    else:
        return render(request,'accounts/login.html')

def signoff(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    #TODO need to route to home page
    return render(request,'accounts/signoff.html')

def signup(request):
    if request.method == 'POST':
        #user wants to signup
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user=User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                auth.login(request,user)    
                return redirect('home')
        else:
            return render(request,'accounts/signup.html', {'error': 'passwords must match'})
    else:
        return render(request,'accounts/signup.html')
