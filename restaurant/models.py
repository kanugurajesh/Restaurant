from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200,default=None)    
   last_name = models.CharField(max_length=200,default=None)
   guest_number = models.IntegerField()
   gmail = models.EmailField(max_length=254,default=None)
   comment = models.CharField(max_length=1000,default=None)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length = 200,default=None)
   category = models.CharField(max_length=50,default=None)
   image_url = models.URLField(max_length=200,default=None)
   price = models.IntegerField()
   def __str__(self):
      return self.name
