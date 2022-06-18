from email.policy import default
from enum import unique
from tarfile import BLKTYPE
from uuid import UUID
import uuid
from django.db import models
from users.models import Profile


class Project(models.Model):
    """"""
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    models.CharField(max_length=150, blank=True, null=True)
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

    class Meta:
        ordering = ['created']

    def update_votes(self):
        self.vote_total = self.review_set.count()
        upvotes = self.review_set.filter(value = 'Up').count()
        self.vote_ratio = int(upvotes / self.vote_total * 100)
        self.save()

    def get_reviewers(self):
        reviewers = self.review_set.all().values_list('owner__id', flat=True)
        return reviewers
class Review(models.Model):
    """"""
    VOTE_TYPE = (
        ('Up','Up Vote'),
        ('Down', 'Down Vote')
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True) # relationship with Profile
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #realtionship with Project
    body = models.TextField(null=True, blank=True)           
    value = models.CharField(max_length=200, choices=VOTE_TYPE)  

    #timestamp
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    class Meta:
        unique_together = [['owner', 'project']]

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