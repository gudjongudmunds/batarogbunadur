from django import forms
from .models import BunadurFyrirspurn, Bunadur

from django import forms
from .models import BunadurFyrirspurn

from django import forms
from .models import BunadurFyrirspurn

class BunadurfyrirspurnForm(forms.ModelForm):
    boat_name = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.HiddenInput() 
    )
    
    class Meta:
        model = BunadurFyrirspurn
        fields = ['tengil_nafn', 
                  'tengil_tp', 
                  'tengil_simi', 
                  'fyrirspurn']
        labels = {
            'tengil_nafn': 'Tengiliður',
            'tengil_tp': 'Tölvupóstur',
            'tengil_simi': 'Sími',
            'fyrirspurn': 'Skráðu fyrirspurn hér'
        }

    def __init__(self, *args, **kwargs):
        boat = kwargs.pop('boat', None)
        super().__init__(*args, **kwargs)
        if boat:
            self.fields['boat_name'].initial = boat.nafn



class BunadurskraningForm(forms.ModelForm):
    class Meta:
        model = Bunadur
        fields = ['nafn', 
                  'tegundbun',
                  'lys_selj', 
                  'tengil_nafn', 
                  'tengil_tp', 
                  'tengil_simi', 
                  'mynd1',
                  'mynd2',
                  'mynd3',
                  'mynd4',
                  'mynd5',
                  'mynd6'
                  ]
        labels = { 
            'nafn':'Nafn á búnaði',
            'tegundbun':'Tegund',
            'lys_selj':'Lýsing á búnaði',
            'tengil_nafn':'Nafn tengiliðs',
            'tengil_tp':'Tölvupóstur tengiliðs',
            'tengil_simi':'Sími tengiliðs',
            'mynd1':'Tengdu mynd nr. 1',
            'mynd2':'Tengdu mynd nr. 2',
            'mynd3':'Tengdu mynd nr. 3',
            'mynd4':'Tengdu mynd nr. 4',
            'mynd5':'Tengdu mynd nr. 5',
            'mynd6':'Tengdu mynd nr. 6'
            }