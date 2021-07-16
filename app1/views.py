from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#creating account for a new user



def indexfunction(request):
    if request.method == "POST":

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if User.objects.filter(email=email).exists():
            print("email already exist")

        elif password == confirmpassword:

            user = User.objects.create_user(username=firstname , password=confirmpassword,first_name =firstname,last_name =lastname,email= email)
            user.save()


        return redirect('signin')
    return render(request,'app1/index.html',)

def homefunction(request):
    return render(request, 'app1/home.html')


def aboutusfunction(request):
    return render(request,'app1/aboutus.html')

def moreinfofunction(request):
    return render(request,'app1/moreinfo.html')

def contactfunction(request):
    return render(request,'app1/contact.html')


#signin function for an existing user/created account just now

def sigin(request):

    if request.method == "POST":
        username1 = request.POST['name']
        password1 = request.POST['password']
        data1 = {}
        data1['username1'] = username1
        print(data1,'',"welcome")

        if User.objects.filter(username = username1).exists():
            print('this user exist')
            user = authenticate(username = username1,password = password1)

            if user is not None:
                print(user)
                login(request,user,username1)
                return redirect('like')
            else:
                messages.error(request,'password dosent match')
                print(user)

        else:
            messages.error(request,'username doesnot match')
            print('username doesnot match')



    return render(request,'app1/sigin.html')


def more(request):
    return render(request,'app1/moreinformation.html')

def welcome(request):
    return render(request,'app1/welcome.html')


def signout(request):
    logout(request)
    return redirect('indexfunction')


def booknow(request):
    if request.method == "POST":
        return render(request, "app1/thanksforbooking.html")
    return render(request,"app1/booknow.html")



def thnaks(request):
    return  render(request,"app1/thanksforbooking.html")