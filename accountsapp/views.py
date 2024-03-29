from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
       # [signup]버튼을 눌렀을 때 일어나는 일
       if request.POST['password1'] == request.POST['password2']:
           try:
               user = User.objects.get(username=request.POST['username'])
               return render(request, 'accountsapp/signup.html', {'error': 'Username has already been taken'})
           except User.DoesNotExist:
               user = User.objects.create_user(
                   request.POST['username'], password=request.POST['password1'])
               auth.login(request, user)
               return redirect('home')
       else:
           return render(request, 'accountsapp/signup.html', {'error': 'Passwords must match'})
    else:
       # User wants to enter info --> 유저가 정보를 입력하고 있는 중임.
       return render(request, 'accountsapp/signup.html')

def login(request):
    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accountsapp/login.html', {'error':'ID 혹은 비밀번호가 다릅니다.'})
    else:
        return render(request, 'accountsapp/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accountsapp/login.html')
