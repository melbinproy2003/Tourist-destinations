from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Usertable
from tourist_destinations.models import Destination

def userregistration(request):
    usertable = Usertable()
    if request.method == 'POST':
        usertable.username = request.POST['username']
        usertable.email = request.POST['email']
        usertable.password = request.POST['password']

        if request.POST['password'] == request.POST['cpassword']:
            usertable.save()
            messages.success(request,'Registration success')
            return redirect('login')
        else:
            messages.error(request, 'Password is not matching')
            return redirect('registration')
    return render(request, 'guest/signup.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = Usertable.objects.get(username=username, password=password)
            request.session['username'] = user.username
            request.session['id'] = user.id
            return redirect('home')
        except Usertable.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'guest/signin.html')

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'home.html', {'destinations': destinations})

def index(request):
    destinations = Destination.objects.all()
    return render(request, 'Index.html', {'destinations': destinations})

def logout_view(request):
    logout(request)
    return redirect('index')