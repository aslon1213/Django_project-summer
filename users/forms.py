from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']

        labels = {
            'first_name':'Your First Name'
        }
        def __init__(self, *args, **kwargs):
            super(CustomUserCreation, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})



class updateProfileForm(ModelForm):
    class Meta:
        model = Profile
        """fields = [
            'first_name', 'username' , 'email', 'short_info',
            'bio', 'profile_image', 'social_twitter', 'social_linkedin','social_instagram','social_youtube','social_github','social_my_website',
        ]"""
        fields = '__all__'
        def __init__(self, *args, **kwargs):
            super(CustomUserCreation, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})


