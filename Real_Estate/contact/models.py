from django.db import models

from datetime import datetime

# Create your models here.
class Contact(models.Model):
    listing=models.CharField(max_length=150)
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    message=models.TextField(blank=True)
    listing_id=models.IntegerField()
    user_id=models.IntegerField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.name