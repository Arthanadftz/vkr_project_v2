from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile

# Register your models here



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'date_of_birth']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
