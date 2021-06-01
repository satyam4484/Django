from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import signupform   #usercreated form 

# Create your views here.

def user_sign_built(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = signupform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Account created ')
                fm=signupform()
        else :
            fm = signupform()
        return render(request,'home.html',{'form':fm})
    else :
        return HttpResponseRedirect('/profile/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            fm = AuthenticationForm(request==request,data =request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass  = fm.cleaned_data['password']
                user = authenticate(username = uname,password = upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
        else :
            fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else :
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else :
        return HttpResponseRedirect('/login/')

def user_logout(request):
    if request.method =='POST':
        logout(request)
        return HttpResponseRedirect('/login/')


    
def login_us(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request = request,data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname , password = upass)
                if user is not None:
                    login(request,user)
                    # messages.success("login succefully ")
                    return HttpResponse("logged in")
        else:
            fm = AuthenticationForm()
        return render(request,'login_sign.html',{'form':fm,'value':1})
    else :
        return HttpResponse("you are already login ")
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = signupform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Account created ')
                fm=signupform()
        else :
            fm = signupform()
        return render(request,'home.html',{'form':fm})
    else :
        return HttpResponseRedirect('you are already login ')