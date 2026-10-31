from django import forms
from .models import AflaheimFyrirspurn, Aflaheim

class AflaheimfyrirspurnForm(forms.ModelForm):
    boat_name = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.HiddenInput()
        )
    class Meta:
        model = AflaheimFyrirspurn
        fields = [
            'tengil_nafn', 
            'tengil_tp', 
            'tengil_simi', 
            'fyrirspurn'
        ]
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

class AflaheimskraningForm(forms.ModelForm):
    class Meta:
        model = Aflaheim
        fields = ['tegundaflah', 
                  'bat_nr', 
                  'tegsjavaraf', 
                  'ktaflah',
                  'lys_selj',
                  'tengil_nafn', 
                  'tengil_tp', 
                  'tengil_simi', 
                  ]
        labels = {
            'tegundaflah':'Veldu aflaheimild', 
            'bat_nr':'Tengt bát', 
            'tegsjavaraf':'Tegund veiðiheimild',
            'ktaflah':'Kennitala eiganda aflaheimilda',
            'lys_selj':'Lýsing',
            'tengil_nafn':'Nafn tengiliðs',
            'tengil_tp':'Tölvupóstur tengiliðs',
            'tengil_simi':'Sími tengiliðs',
            }