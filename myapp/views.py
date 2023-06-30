from django.shortcuts import render, redirect
from .models import Register,Query,States,Countries,Images, Locations,Cities,Booked,Gallery,Packages, Packagelocation,Card
import smtplib
from smtplib import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import random
from datetime import datetime
import math

def index(request):
    images=Images.objects.all()
    cards=Card.objects.all()
    # images.save()
    for image in images:
        print(image)
    if request.method=='GET':
        return render(request,"index.html",{"images":images, "cards":cards})

def card(request):
    cards=Card.objects.all()
    for card in cards:
        print(card)
    if request.method=='GET':
        return render(request,"index.html",{'cards':cards})


success=False
def registration(request):
    states=States.objects.all()
    countries=Countries.objects.all()
    if request.method == 'GET':
        return render(request, "registration.html",{"states":states,"countries":countries})
    if request.method == 'POST':

        obj = Register()
        obj.username=request.POST.get('username')
        #obj.password=request.POST.get('password')
        obj.gender=request.POST.get('gender')
        obj.email=request.POST.get('email')
        obj.idproof=request.POST.get('idproof')
        obj.idnum=request.POST.get('idnum')
        obj.mobile=request.POST.get('mobile')
        obj.city=request.POST.get('city')
        obj.address=request.POST.get('address')
        obj.state=request.POST.get('state')
        obj.pincode=request.POST.get('pincode')
        obj.country=request.POST.get('country')


        chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        obj.password=''
        for c in range(10):
            obj.password += random.choice(chars)

       # print(password)

        obj.save()
        success=True

        return render(request,"registration.html" ,{'success':success,'password':obj.password})

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')

        #To check with database value
        try:
            user = Register.objects.filter(email=email,password=password)
            request.session['email'] = user[0].email
            request.session['id']=user[0].id
            success=True
            return render(request,"myprofile.html",{'success':success,'my_data': user})
        except:
            return render(request,"login.html",{'error':True})


def forgot(request):
    if request.method == "POST":
        subject = 'Forgot Password'
        from_email = "chunnitiwari1995@gmail.com"
        email = request.POST.get('email')
        random.seed(datetime.now())
        code = math.floor(random.random() * 1000000)
        print (code)
        message = "Your Code is: "+str(code)
        request.session['code'] = str(code)
        request.session['temp'] = email

        try:
            send_mail(subject, message, from_email, [email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, "change.html")
    else:
        return render(request, "forgot.html")

def changepassword(request):
    if request.method == 'GET':

        return render(request,"changepassword.html")
    if request.method == 'POST':
        email = request.POST.get('email')
        opass = request.POST.get('opass')
        npass = request.POST.get('npass')
        cpass = request.POST.get('cpass')

        if npass == cpass:
            try:
                user = Register.objects.get(email=email,password=opass)
                user.password = npass
                user.save()
                return render(request,"changepassword.html",
                                {'success':True,
                                 'success_msg':"Password Changed Successfully"})
            except Register.DoesNotExist:
                return render(request,"changepassword.html",{'email':email})
        else:
            return render(request,"changepassword.html",
                            {'error':True,
                             'error msg':"New Password and confirm password does not matched"})

def header(request):
    return render(request,"header.html")

success=False
def contactus(request):
    if request.method == 'GET':
        return render(request, "contactus.html")
    if request.method == 'POST':

        obj = Query()
        obj.username=request.POST.get('username')
        obj.email=request.POST.get('email')
        obj.mobile=request.POST.get('mobile')
        obj.query=request.POST.get('query')

        obj.save()
        success=True

        return render(request,"contactus.html" ,{'success':success})

def editprofile(request):

    if request.method=='GET':
        email=request.session['email']
        x = Register.objects.get(email = email)
        #print("Data: ", x.idnum)
        return render(request,"editprofile.html",{'user':x})
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # gender = request.POST.get('gender')
        # email = request.POST.get('email')
        idproof = request.POST.get('idproof')
        idnum = request.POST.get('idnum')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        address = request.POST.get('address')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        country = request.POST.get('country')

        email = request.session['email']
        user = Register.objects.get(email = email)
        user.username = username
        user.password=password
        user.idproof=idproof
        user.idnum=idnum
        user.mobile=mobile
        user.city=city
        user.address=address
        user.state=state
        user.pincode=pincode
        user.country=country
        user.save()
        return render(request,'editprofile.html', {'user': user})

success=False
def change(request):
    code = request.POST.get('code')
    npass = request.POST.get('npass')
    cpass = request.POST.get('cpass')
    print(code, npass, cpass, request.session['code'], request.session['temp'])
    if (code == request.session['code']):
        print("code match")
        if (npass == cpass):
            print("pass match")
            x=Register.objects.get(email=request.session['temp'])
            x.password = cpass
            x.save()
            del request.session['temp']
            del request.session['code']
            success=True
            return render(request, "change.html",{'success':success})
        else:
            return render(request,"change.html",{'error':True,'error_msg':'Password and Confirm Password does not Match'})
            #print("Password and Confirm Password doesn't Match")

    else:
        print("code not matched")
        return render(request, "change.html",{'error':True,'error_msg':'Code not Matched'})

def filter(request):
    cities = Cities.objects.all()
    if request.method=="POST":
        city=request.POST.get('city')
        if city == "all":
            locations=Locations.objects.all()
        else:
            locations=Locations.objects.filter(city=city)
        return render(request,"eticketing.html",{"locations":locations, "cities":cities, "filter":city})
    else:
        locations = Locations.objects.all()
        return render(request,"eticketing.html",{"locations":locations, "cities":cities})



def booked(request):
     booked=Booked.objects.filter(user_id=request.session['id'])
     bookingids = Booked.objects.only('package_id').filter(user_id=request.session['id'])
     packages = Packages.objects.filter(id__in=bookingids)
     bookings = []
     for booking in booked:
            for package in packages:
                if package.id == booking.package_id:
                    bookings.append({"booking": booking, "package":package})
     print(bookings)
     return render(request, 'booked.html', {'bookings': bookings})


def place(request, id):
    # images = Gallery.objects.all()
    # packages=Packages.objects.all()
    # locations=Locations.objects.all()
    if request.method == 'GET':
        l = Locations.objects.get(id = id)
        images = Gallery.objects.filter(location_id = id)
        # packages = Packages.objects.filter(location_id = id)
        packagelocs = Packagelocation.objects.only('package_id').filter(location_id = id)
        packages = Packages.objects.filter(id__in=packagelocs)
        length = len(images)
        return render(request, "place.html", {"images": images,"packages":packages, "length": length,"location":l, "id":id})

    else:
        if request.method=="POST":
            person = request.POST.get('person')
            package_id = request.POST.get('packageid')
            current = datetime.today()
            user_id=request.session['id']
            obj = Booked( person=person, package_id=package_id, current=current, user_id=user_id )
            #obj.current=request.POST.get('current')
            # obj.user = Register.objects.get(id=request.session['id'])
            obj.save()
            print("Booking ID=", id)
            #success=True
            return redirect('booked')
            #return redirect('booked')


