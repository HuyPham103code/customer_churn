from django.db import models

# Create your models here.

class Customers(models.Model):
    creditScore = models.IntegerField()
    age = models.IntegerField()
    tenure = models.IntegerField()
    hasCrCard = models.BooleanField()
    isActiveMember = models.BooleanField()
    estimatedSalary = models.FloatField()
    geography = models.CharField(max_length=100)
    gender =  models.CharField(max_length=50)
    totalProducts = models.IntegerField()
    accountBalance = models.FloatField()


