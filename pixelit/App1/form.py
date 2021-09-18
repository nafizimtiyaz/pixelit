from django import forms
from .models import user_profile


class ProfileUpdate(forms.ModelForm):

    class Meta:
        model=user_profile
        fields = ['education','location','bio','image']
