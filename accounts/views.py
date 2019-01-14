from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact


# Create your views here.

def register(request):
    if request.method == 'POST':
        #register Logic
        #form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check if passwords match
        if password == password2:
            #check usernsame
            if User.objects.filter(username=username).exists():
                messages.error(request,"That username is taken, please choose another username")
                return redirect('register')

            elif User.objects.filter(email= email).exists():
                messages.error(request,"That Email is taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                         email=email,
                                         first_name=first_name,
                                         last_name=last_name,
                                         password=password)
                #login
                # auth.login(user)
                # messages.success(request,'You are not loggied in')
                # return redirect("index")
                user.save()
                messages.success(request,'you are now registered and can login')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        #login logic
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials, please try again')
            return redirect('login') 
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you are now logged out')
        return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        inquiries = Contact.objects.all().filter(user_id = user_id)
        context = {'inquiry':inquiries}
        return render(request, 'accounts/dashboard.html',context=context)