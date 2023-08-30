import datetime

from django import forms
from wagtail.users.models import UserProfile

class CustomProfileSettingsForm(forms.ModelForm):
    bio = forms.CharField(help_text="Write a short description about yourself", required=False, widget=forms.Textarea(attrs={"rows":"5"}),)
    date_joined = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), initial=datetime.datetime.now)
    
    class Meta:
        model = UserProfile
        fields = ["bio","date_joined",]
