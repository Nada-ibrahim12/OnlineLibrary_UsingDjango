from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile 
import re

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    accType = forms.ChoiceField(choices=[('Admin', 'Admin'), ('User', 'User')], required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "name", "accType")

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        password_strength = validate_password_strength(password)
        if password_strength != True:
            raise forms.ValidationError(password_strength)
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["name"]
        user.save()
        
        # Check if a profile already exists for the user
        if not hasattr(user, 'profile'):
            profile = Profile.objects.create(user=user, accType=self.cleaned_data["accType"])
        else:
            profile = user.profile
            profile.accType = self.cleaned_data["accType"]
            profile.save()
        
        return user

    
def validate_password_strength(value):
    reasons = []
    if len(value) < 8:
        reasons.append("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", value):
        reasons.append("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", value):
        reasons.append("Password must contain at least one lowercase letter")
    if not re.search(r"\d", value):
        reasons.append("Password must contain at least one number")
    if not re.search(r"[-_/!@#$%^&*(),.?\":{}|<>]", value):
        reasons.append("Password must contain at least one special character")
    return reasons if reasons else True
