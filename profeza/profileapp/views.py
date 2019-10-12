from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserProfile, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


def home(request):
    return render(request, 'profileapp/home.htm')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #u_form = UserProfile(request.POST)

        if form.is_valid(): #and u_form.is_valid():
            user = form.save()
            #info = u_form.save(commit=False)
            #info.user = user

            #info.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, You can now Login and make profile!')
            return redirect('profileapp:home')
    else:
        form = UserRegisterForm()
        #u_form = UserProfile()
    context = {
        #'u_form': u_form,
        'form': form
    }

    return render(request, 'profileapp/register.htm', context)


def login_view(request):
    next = request.GET.get('/')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('profileapp:home')
    context = {
        'form': form,
    }
    return render(request, 'profileapp/login.htm', context)



def logout_view(request):
    logout(request)
    return redirect("/")