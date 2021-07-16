
from django.urls import path,include
from app2 import views

urlpatterns = [
    path('labadmin/',views.labadmin ,name ="labadmin"),
    path('userprofile/',views.userprofile,name = "like"),
    path('adminlogin/',views.adminlogin,name="adminlogin")

]