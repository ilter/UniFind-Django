from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cellphone_number = models.CharField(max_length=13)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YT', 'YouTube'),  # first value to store db second value for view
        ('Google', 'Google'),
        ('News', 'News'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)
    # if u want on_delete makes it null have to declare null=True

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'
