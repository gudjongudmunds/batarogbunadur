from django import forms

from .models import Review

#class ReviewForm(forms.Form):
#    user_name= forms.CharField(label='Nafnið þitt', max_length='100', error_messages={
#        'required':'Nafnið þitt verður að vera skráð.', 
#        'max_length': 'Þetta er of langt nafn.'
#    })
#    review_text= forms.CharField(label='Skráðu umsögn þína', widget=forms.Textarea, max_length=200)
#    rating= forms.IntegerField(label='Gefðu einkun', min_value=1, max_value=6)

# forms.py

class ReviewForm(forms.ModelForm):
    boat_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Review
        fields = ['boat_name', 'rating', 'comment']

    def __init__(self, *args, **kwargs):
        boat = kwargs.pop('boat', None)
        super().__init__(*args, **kwargs)
        if boat:
            self.fields['boat_name'].initial = boat.name
