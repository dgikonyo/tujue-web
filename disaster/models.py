from django.db import models
import uuid
from .country import countryList
from django.urls import reverse


# Create your models here.
class User(models.Model):
    userID=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    firstName=models.CharField(max_length=30,help_text='First name')
    lastName=models.CharField(max_length=30,help_text='Last name')
    emailAddress=models.EmailField(max_length=254,)
    phoneNumber=models.IntegerField(help_text='Phone Number')
    address=models.IntegerField(help_text='Address')
    country=models.CharField(max_length=20,choices=countryList)
    city=models.CharField(max_length=20,help_text='City')
    dateCreated=models.DateTimeField(auto_now_add=True)#will add the user record upon account creation


    def __str__(self):
        return self.emailAddress
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this 
          User."""
        return reverse('user', args=[str(self.userID)])

class Disaster(models.Model):
    disasterID=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)#This ley can't be edited
    minTemp=models.IntegerField('Minimum Temperature')
    maxTemp=models.IntegerField('Maximum Temperature')
    rainfall=models.IntegerField('Rainfall')
    evaporation=models.IntegerField('Evaporation')
    sunshine=models.IntegerField('Sunshine')
    windGustDir=models.IntegerField('Wind Gust')
    windGustSpeed=models.IntegerField('WindGustSpeed')
    windDirEarly=models.IntegerField('Wind Direction 9 AM')
    windDirLate=models.IntegerField('Wind Direction 3 PM')
    windSpeedEarly=models.IntegerField('Wind Speed 9 AM')
    windSpeedLate=models.IntegerField('Wind Speed 3 PM')
    humidityEarly=models.IntegerField('Humidity 9 AM')
    humidityLate=models.IntegerField('Humidity 3 PM')
    pressureEarly=models.IntegerField('Pressure 9 AM')
    pressureLate=models.IntegerField('Pressure 3 PM')
    cloudEarly=models.IntegerField('Cloud 9 AM')
    cloudLate=models.IntegerField('Cloud 3 PM')
    rainToday=models.IntegerField('Rain Today')

    
    def __str__(self):
        return self.rainToday

    def get_absolute_url(self):
        """Returns the url to access a detail record for this 
          Disaster."""
        return reverse('disaster', args=[str(self.disasterID)])

    
class DisasterReport(models.Model):
    #Fields
    reportID=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    reportSubject=models.CharField('Report Title',max_length=20,help_text='What are you reporting about?',default='')
    disasterChoices=(
        ('F','Flood'),
        ('E','EarthQuake'),
        ('L','Land slide'),
        ('W','Wild/Forest Fires')
    )
    disasterName=models.CharField(
        'Disaster Name',
        max_length=20,
        choices=disasterChoices
        )


    dateCreated=models.DateTimeField('Date',auto_now=False,auto_now_add=True)#will automatically enter the current date and can't be edited
    costOfDamages=models.DecimalField('Damage Cost',max_digits=20,decimal_places=0)
    country=models.CharField('Country',max_length=20,choices=countryList)
    description=models.TextField('Description')
    casualties=models.IntegerField('Casualties')
    #userID=models.ForeignKey(User, on_delete=models.CASCADE,editable=False)#this is foreignKey relation to the User
    validated=models.BooleanField(default=False)

    """"def get_absolute_url(self):
        #Returns the url to access a detail record for a specific disaster report.
        return reverse('alerts', args=[str(self.reportID)])"""
    
    def __str__(self):
        return self.reportSubject

    #This class will control the default ordering of records returned when you query the model type
    '''So the order of occurrence will be reversed and the newest record will appear first because of the (-)'''
    class Meta:
        ordering=['-dateCreated','disasterName']
