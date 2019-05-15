from django import forms
from django.contrib.auth.forms import UserCreationForm#, UserChangeForm

from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields
        fields = ('username', 'email', 'date_of_birth', 'full_name', 'user_role', 'phone_no', 'student_group')


class CustomUserChangeForm(forms.ModelForm):#UserChangeForm

    class Meta:
        model = CustomUser
        #fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'phone_no')


class CustomUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar',)
