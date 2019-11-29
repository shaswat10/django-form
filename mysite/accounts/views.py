from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.error(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,"login.html")



def register(request):

    if request.method == 'POST':
        first_name = request.POST['Name']
        last_name = request.POST['Lname']
        username = request.POST['Uname']
        email = request.POST['Email']
        password = request.POST['Password']

        if User.objects.filter(username = username).exists():
            messages.info(request, 'Take a different username')
            return redirect('register')

        elif User.objects.filter(email = email).exists():
            message.info(request, 'already registered')
            return redirect('register')

        else:
            user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
            user.save();
            print("User created")
            return redirect('login')



    else:
        return render(request,"register.html")
