from django.db import models

from account.models import User


class Timeline(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    time = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='images/icons')

    def __str__(self):
        return f'{self.title} - {self.time}'


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    additional_message = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.full_name} - {self.phone_number}'
