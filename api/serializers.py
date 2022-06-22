from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    owner = ProfilesSerializer(many = False)
    tags = TagsSerializer(many = True)
    class Meta:
        model = Project
        fields = '__all__'
    

