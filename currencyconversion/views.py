from django.shortcuts import render,redirect
from .models import Users
from django.http import HttpResponse
from django.contrib.auth.models import User
import requests
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout 
from .forms import MyForm
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

def index(request):
    return render(request , 'currencyconversion/home.html')

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


@csrf_exempt
def landingpage(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            fc = request.POST.get('fc')
            tc = request.POST.get('tc')
            prices = requests.get("https://api.fixer.io/latest?base="+str(fc))
            price = prices.json()['rates'][tc]
            date = prices.json()['date']
            context = {
            'fc':fc,
            'tc':tc,
            'price':price
            }
            actionrecorded = str(fc)+ "to" +str(tc) + "is done at " + str(date)
            me = User.objects.get(id=request.user.id)
            Users.objects.create(name=me, conversion=actionrecorded)
            template = loader.get_template('currencyconversion/conversion.html')
            return HttpResponse(template.render(context, request))
        else:
            #if post request is not true
            #returing the form template
            prices = requests.get("https://api.fixer.io/latest")
            countries = prices.json()['rates'].keys()
            print(countries)
            template = loader.get_template('currencyconversion/landingpage.html')
            return HttpResponse(template.render({'countries':countries}))
    else:
        return redirect('index')

def nofile(request):
    return render(request, 'currencyconversion/nofile.html')



