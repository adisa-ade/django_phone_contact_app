from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']

    def get_absolute_url(self):
        return reverse('home')
