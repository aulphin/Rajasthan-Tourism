from django.urls import path
from . import views

urlpatterns=[
    path('header/',views.header,name="header"),
    path('index/',views.index,name="index"),
    path('registration',views.registration,name="registration"),
    path('login/',views.login,name="login"),
    path('forgot/',views.forgot,name="forgot"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('eticketing/',views.filter,name="eticketing"),
    path('contactus/',views.contactus,name="contactus"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('change/',views.change,name="change"),
    path('filter/',views.filter,name="filter"),
    path('booked/',views.booked,name="booked"),
    path('place/<int:id>',views.place,name="place"),
    path('card/',views.card,name="card"),



]
