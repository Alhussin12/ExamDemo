from django.shortcuts import render,redirect
from .models import ExamUser
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    username=None
    password=None
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        print(username,password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
        #     #for one login
            if 'rem' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request,user)
            return redirect('index')
        else:
            print('username or passowrd invalid')
    return render(request,'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')