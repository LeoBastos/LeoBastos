from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=60, verbose_name='Name')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True, verbose_name='Description')
    phone = models.CharField(max_length=11, verbose_name='Phone')
    email = models.CharField(max_length=40, verbose_name='Email')
    is_mvp = models.BooleanField(default=False, verbose_name='MVP')
    hire_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Hire Date')

    def __str__(self):
        return self.name
