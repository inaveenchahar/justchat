from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileModel(models.Model):
    GENDER = (
        ('--', '--'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    AGE = [('--', '--')] + [(i, i) for i in range(18, 101)]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    gender = models.CharField(choices=GENDER, null=True, max_length=8)
    age = models.IntegerField(choices=AGE, null=True)
    bio = models.CharField(max_length=100, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


