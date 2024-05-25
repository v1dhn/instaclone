from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255,unique=True,null=False)
#     phone_number = models.CharField(max_length=10)
#     is_active = models.BooleanField(default=False)

#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)

class TimeStamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(TimeStamp):
    DEFAULT_PROFILE_PIC_URL = "https://mywebsite.com/placeholder.png"

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    profile_pic_url = models.CharField(max_length=255, default=DEFAULT_PROFILE_PIC_URL)
    bio = models.CharField(max_length=255,blank=True)
    is_verified = models.BooleanField(default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

