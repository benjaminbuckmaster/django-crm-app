from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

def home(request):
    records = Record.objects.all()

    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log in successful.")
            return redirect('home')
        else:
            messages.success(request, "Login error. Plase try again.")
            return redirect('home')

    else:
        return render(request, 'home.html', context={'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', context={'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')
