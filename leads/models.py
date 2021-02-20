from django.db import models


# Create your models here.

class Agent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


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

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)
