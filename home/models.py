from django.db import models

# Create your models here.

class Rent(models.Model):

    car_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    car_no = models. IntegerField()
    mileage = models.IntegerField()
    seats = models.IntegerField()
    luggage = models.IntegerField()
    fuel = models.CharField(max_length=50)

class Contact(models.Model):
    c_name = models.CharField(max_length=100,null=False,blank=False)
    c_email = models.EmailField(max_length=100)
    c_subject = models.CharField(max_length=100,null=False,blank=False)
    c_message = models.CharField(max_length=1000,null=False,blank=False)
    c_datesend = models.DateTimeField(auto_now_add=True,verbose_name="date send")

    def __str__(self):
        return self.c_name

class Order(models.Model):
    items_json = models.CharField(max_length=5000)
    o_amount = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    o_name = models.CharField(max_length=100)
    o_num = models.CharField(max_length=15)
    o_email = models.EmailField(max_length=100)
    o_address = models.TextField()
    o_from_date = models.DateTimeField()
    o_to_date = models.DateTimeField()