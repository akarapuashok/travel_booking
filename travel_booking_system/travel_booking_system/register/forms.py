from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Add any other fields you need

        # Optionally, customize widgets, if desired
        widgets = {
            'password': forms.PasswordInput(),
        }
