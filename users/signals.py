import profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile

# @reciever(post_save, sender = Profile)

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
        )


def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.first_name
        user.email = profile.email
        user.save()

def deleteProfile(sender, instance, created, **kwargs):
    pass

post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_save.connect(deleteProfile, sender=Profile)