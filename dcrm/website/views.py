from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log in successful")
            return redirect('home')
        else:
            messages.success(request, "Login error. Plase try again.")
            return redirect('home')

    else:
        return render(request, 'home.html', context={})

def logout_user(request):
    pass
