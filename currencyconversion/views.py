from django.shortcuts import render,redirect
from .models import Users
import requests
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout 


def index(request):
    return render(request , 'currencyconversion/index.html')


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landingpage')
    else:
        form = AuthenticationForm()
    return render(request, 'currencyconversion/signin.html',{'form': form})


def signout(request):
    logout(request)
    return render(request, 'currencyconversion/signout.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            obj = form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('landingpage')
    else:
        form = UserCreationForm()
    return render(request, 'currencyconversion/signup.html',{'form':form})



def landingpage(request):
    prices = requests.get('https://api.fixer.io/latest?base=USD')
    
    return render(request,'currencyconversion/landingpage.html',{"prices":prices})
