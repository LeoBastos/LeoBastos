from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=200, verbose_name='Listing')
    listing_id = models.IntegerField()
    name = models.CharField(max_length=100, verbose_name='Contact Name')
    email = models.CharField(max_length=100, verbose_name='Contact Email')
    phone = models.CharField(max_length=100, verbose_name='Contact Phone')
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True ,verbose_name='Contact Date')
    user_id = models.IntegerField(blank=True, verbose_name='Contact User ID')
    
    def __str__(self):
        return self.name