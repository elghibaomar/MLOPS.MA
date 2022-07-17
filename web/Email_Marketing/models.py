from django.db import models

# Create your models here.
class Email(models.Model):
    Customer_id = models.IntegerField()
    Product_id = models.CharField(max_length=50)
    Date = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Template = models.IntegerField()
    Countries = models.CharField(max_length=50)
    Purchase = models.CharField(max_length=10)
    Marital = models.CharField(max_length=50)
    Age = models.IntegerField()