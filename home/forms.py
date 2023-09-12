import datetime

from django import forms

from wagtail.users.models import UserProfile

from work.models import WorkPage

class CustomProfileSettingsForm(forms.ModelForm):
    bio = forms.CharField(help_text="Write a short description about yourself", required=False, widget=forms.Textarea(attrs={"rows":"5"}),)
    date_joined = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), initial=datetime.datetime.now)
    user_level = forms.CharField(max_length=20, required=False, help_text="Your level at work")

    @property
    def get_user_level(self):
        if WorkPage.objects.filter(user=request.user).count() >= 20:
            return self.user_level == 'Level 5'
        elif WorkPage.objects.filter(user=request.user).count() == 15:
            return self.user_level == 'Level 4'
        elif WorkPage.objects.filter(user=request.user).count() == 10:
            return self.user_level == 'Level 3'
        elif WorkPage.objects.filter(user=request.user).count() == 5:
            return self.user_level == 'Level 2'
        else:
            return self.user_level == 'Level 1'
    
    class Meta:
        model = UserProfile
        fields = ["bio","date_joined", "user_level"]
