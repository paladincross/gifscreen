from django import forms

from .models import Post, Comment, UserProfile

from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'picture')
