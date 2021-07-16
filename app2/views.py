import self as self
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from app2.models import Labadmin


def labadmin(request):
        if request.method == "POST":
            print("post method requested")
            lab = Labadmin()
            lab.adminemail = request.POST['email']
            lab.adminpssword = request.POST['password']
            lab.labname = request.POST['lab']
            lab.labaddress = request.POST['address']
            lab.lablocation = request.POST['lablocation']
            lab.labtests = request.POST['tests']
            lab.gst = request.POST['gstcode']
            lab.file = request.FILES['file']
            lab.save()
            data = Labadmin.objects.all()

            return render(request,'app2/adminlogin.html',{'data':data})
        elif request.method == "GET":
                print('get requested')
                return render(request,'app2/labadmin.html')


def adminlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            print('this user exist')
            user = authenticate(email=email,password=password)

            if user is not None:
                print(user)
                login(request, user)
                return redirect('labadmin')
            else:
                messages.error(request, 'password dosent match')
                print(user)

        else:
            messages.error(request, 'username doesnot match')
            print('username doesnot match')

    return render(request,'app2/adminlogin.html')


def userprofile(request):

    if request.method == "POST":
        lablocation1 = request.POST['search']

        print("post requested")
        if Labadmin.objects.filter(lablocation=lablocation1).exists():
            print("location requested")




            data1 = Labadmin.objects.filter(lablocation=lablocation1)
            data1 = {"data": data1}
            return render(request, 'app1/userprofile.html',data1)
        else:
            errormsg ="Sorry No labs available in your location! Try Another Location"
            errormsg ={"error":errormsg}
            return render(request, 'app1/userprofile.html', errormsg)
            print("no lab available")

    return render(request, 'app1/userprofile.html')

