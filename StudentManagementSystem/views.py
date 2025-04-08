from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . import forms

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = forms.UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User created successfully!')
            return redirect('home')
    else:        
        form = forms.UserSignupForm()
    return render(request, 'auth.html',{'form':form})    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request,messages.SUCCESS,'User logged in successfully!')
                return redirect('home')
            else:
                messages.add_message(request,messages.ERROR,'invalid credential!')    
    else:
        form = AuthenticationForm()
    return render(request, 'auth.html', {'form': form}) 

def user_logout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'User logged out successfully!')
    return redirect('home')