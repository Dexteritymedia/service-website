from django import forms

from .models import FeedBack

class FeedBackForm(forms.ModelForm):
    
    class Meta:
        model = FeedBack
        fields = ["name","message", "picture", "ratings",]

class CalendarForm(forms.Form):
    MONTHS = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )
    month = forms.ChoiceField(choices=MONTHS, help_text='Select the month') 
    year = forms.CharField(widget=forms.widgets.NumberInput(attrs={'minlength': 4, 'maxlength': 4, 'required': True, 'type': 'number',}),
                           max_length=4, help_text='Enter the year')

    class Meta:
        fields = '__all__'
