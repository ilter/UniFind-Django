from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cellphone_number = models.CharField(max_length=13)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class University(models.Model):
    university_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)
    # if u want on_delete makes it null have to declare null=True
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    admission_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.university_name} {self.city} {self.age}'
