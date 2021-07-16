from django.urls import path, include
from app1 import views

urlpatterns = [

    path('home/', views.indexfunction, name='indexfunction'),
    path('homepage/', views.homefunction, name='homefunction'),
    path('aboutus/',views.aboutusfunction,name ='aboutus'),
    path('moreinfo/',views.moreinfofunction, name="moreinfo"),
    path('contact/',views.contactfunction,name="contact"),
    path('signin/',views.sigin,name="signin"),
    path('more/',views.more,name='more'),
    path('welcome/',views.welcome,name='welcome'),
    path('logout/',views.signout,name="logout"),
    path('booknow/',views.booknow, name="booknow"),
    path('thanks/',views.thnaks,name="thanks")

]
