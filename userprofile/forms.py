from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('cedula','activo','propietario','dob','codigo_externo','telefono','movil')

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email')
    