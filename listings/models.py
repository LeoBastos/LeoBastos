from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, related_name='realtor')
    title = models.CharField(max_length=60, verbose_name='Title')
    address = models.CharField(max_length=60, verbose_name='Address')
    city = models.CharField(max_length=60, verbose_name='City')
    state = models.CharField(max_length=60, verbose_name='State')
    zipcode = models.CharField(max_length=8, verbose_name='ZipCode')
    description = models.CharField(max_length=200, verbose_name='Description', blank=True)
    price = models.IntegerField(verbose_name='Price')
    bedrooms = models.IntegerField(verbose_name='Bedrooms')
    bathrooms = models.DecimalField(max_digits=2 , decimal_places=1 ,verbose_name='Bathrooms')
    garage = models.IntegerField(verbose_name='Garage', default=0)
    sqft = models.IntegerField(verbose_name='Square')
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Lot Size')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title



