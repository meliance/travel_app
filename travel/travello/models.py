from django.db import models

# Create your models here.

class Destination(models.Model):
  name = models.CharField(max_length=80)
  img = models.ImageField(upload_to='pics')
  desc = models.TextField()
  price = models.IntegerField()
  offer = models.BooleanField(default=False)

class Trip(models.Model):
    city = models.CharField(max_length=100, default='')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()