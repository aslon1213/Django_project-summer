from email.policy import default
from tarfile import BLKTYPE
from uuid import UUID
from django.db import models
import uuid


class Project(models.Model):
    """"""
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    featured_image = models.ImageField(null=True, blank = True, default='morde.png')
    #setting relationship with 'TAG'
    tags = models.ManyToManyField('Tag', blank=True)

    # to get numbers about voting
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)

    #fields for links
    demo_link = models.CharField(max_length=2000,null=True, blank = True)
    source_link = models.CharField(max_length=2000,null=True, blank = True)

    #timestamp
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title


class Review(models.Model):
    """"""
    VOTE_TYPE = (
        ('Up','Up Vote'),
        ('Down', 'Down Vote')
    )

    #owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #realtionship with Project
    body = models.TextField(null=True, blank=True)           
    value = models.CharField(max_length=200, choices=VOTE_TYPE)  

    #timestamp
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.value


class Tag(models.Model):
    """"""
    name = models.CharField(max_length=200, )   

    #timestamp
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.name