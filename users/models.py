
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Profile (models.Model):
    """"""
    #User
    user = models.OneToOneField(User, blank = True, null = True, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100,blank = True, null = True )
    second_name = models.CharField(max_length = 100,blank = True, null = True )
    email = models.CharField(max_length = 500, blank = True, null = True)
    short_info = models.TextField(blank = True, null = True)
    bio = models.TextField(blank = True, null = True)
    profile_image = models.ImageField(blank = True, null = True, upload_to = 'images/profiles', default = 'sample-image.jpg' )

    #social websites
    social_twitter = models.CharField(max_length = 200, blank = True, null = True)
    social_linkedin = models.CharField(max_length = 200, blank = True, null = True)
    social_instagram = models.CharField(max_length = 200, blank = True, null = True)
    social_youtube = models.CharField(max_length = 200, blank = True, null = True)
    social_github = models.CharField(max_length = 200, blank = True, null = True)
    social_my_website = models.CharField(max_length = 200, blank = True, null = True)

    #timestamp
    created = models.DateTimeField(auto_now_add=True)
    #UUID
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    

    def __str__(self):
        return str(self.user.username)



class Skill(models.Model):
    """"""
    #setting relationship
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    #info
    name = models.CharField(max_length=150,blank=True, null=True )
    description = models.TextField(blank = True, null = True)
    
    #timestamp
    created = models.DateTimeField(auto_now_add=True)
    #UUID
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)