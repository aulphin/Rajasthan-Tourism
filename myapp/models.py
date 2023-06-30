from django.db import models
import random
# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=255,help_text="Enter the User Name")
    password=models.CharField(max_length=255,help_text="Enter Password")
    Gender=(('male','Male'),
            ('female','Female'),)
    gender=models.CharField(max_length=255,help_text="Enter Gender", default='male',choices=Gender)
    email=models.EmailField(max_length=255,help_text="Enter Email")
    Idproof=(('aadhar card','Aadhar Card'),
             ('pan card','PAN Card'),
             ('voter id card','Voter ID Card'),)
    idproof=models.CharField(max_length=12,help_text="Enter ID Number",default='aadhar card',choices=Idproof)
    idnum=models.CharField(max_length=12,help_text="Enter the Aadhar Card No./PAN Card No./Voter ID No.")
    mobile=models.IntegerField()
    city=models.CharField(max_length=255,help_text="Enter City")
    address=models.TextField(max_length=255,help_text="Enter Address")
    state=models.CharField(max_length=255,help_text="Enter State")
    pincode=models.IntegerField()
    country=models.CharField(max_length=255,help_text="Enter Country")
    def __str__(self):
        return self.username
    class Meta:
        db_table="Registration"
        ordering=('username',)
        verbose_name="Register"
        verbose_name_plural="Registers"

class Query(models.Model):
    username=models.CharField(max_length=255,help_text="Enter the User Name")
    email=models.EmailField(max_length=255,help_text="Enter Email")
    mobile=models.IntegerField()
    query=models.TextField(max_length=255,help_text="Enter Address")
    def __str__(self):
        return self.username
    class Meta:
        db_table="Contactus"
        ordering=('username',)
        verbose_name="Contact"
        verbose_name_plural="Contacts"

class States(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Countries(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Images(models.Model):
    name=models.ImageField(upload_to="images/")
    # def __str__(self):
    #     return self.name

class Cities(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Locations(models.Model):
    name = models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="locations")



class Gallery(models.Model):
    location = models.ForeignKey(Locations, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='gallery')

class Packages(models.Model):
    startdate=models.DateField()
    enddate=models.DateField()
    cost=models.IntegerField()
    #days=models.IntegerField()

class Booked(models.Model):
    user=models.ForeignKey(Register, on_delete=models.DO_NOTHING)
    package=models.ForeignKey(Packages, on_delete=models.DO_NOTHING)
    person=models.TextField()
    current=models.DateField()


class Packagelocation(models.Model):
    package=models.ForeignKey(Packages, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete = models.CASCADE)


class Card(models.Model):
    image=models.ImageField(upload_to='card')
    description=models.TextField()
    title=models.TextField()