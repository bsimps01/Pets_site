from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
# Create your models here.

class Pet(models.Model):
    pet_name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    weight_in_pounds = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_name

    def get_absolute_url(self):
        return reverse('pets-list-page')

class Appointment(models.Model):
    date_of_appointment = models.DateField(default=datetime.now)
    duration_minutes = models.IntegerField()
    special_instructions = models.CharField(max_length=1000)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet.pet_name

    def get_absolute_url(self):
        return reverse('calendar-list')
