from django.db import models
from django.contrib.auth.models import User



class user(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    password = models.CharField(max_length=200)
   
    def __str__(self) -> str:
        return f'{self.username}'


class Vendor(models.Model):
    company_name = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def _str_(self):
        return f'self.company_name' + 'self.vendor'

class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    ref = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_now_add=True)

   
def __str__(self):
        return str(self.vendor)

  