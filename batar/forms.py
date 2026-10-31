from django import forms
from .models import BatarFyrirspurn, Batar

class BatarfyrirspurnForm(forms.ModelForm):
    boat_name = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.HiddenInput()
    )
    class Meta:
        model = BatarFyrirspurn
        fields = ['tengil_nafn', 
                  'tengil_tp', 
                  'tengil_simi', 
                  'fyrirspurn'
                  ]
        labels = {'tengil_nafn':'Tengiliður', 
                  'tengil_tp':'Tölvupóstur', 
                  'tengil_simi':'Sími', 
                  'fyrirspurn':'Skráðu fyrirspurn hér'
                  }

    def __init__(self, *args, **kwargs):
        boat = kwargs.pop('boat', None)
        super().__init__(*args, **kwargs)
        if boat:
            self.fields['boat_name'].initial = boat.nafn

class BatarskraningForm(forms.ModelForm):
    class Meta:
        model = Batar
        fields = ['nr', 
                  'nafn', 
                  'lys_vel_selj', 
                  'lys_taeki_selj', 
                  'lys_fylgi_selj', 
                 'lys_annad_selj', 
                 'tengil_nafn', 
                 'tengil_tp', 
                 'tengil_simi', 
                 'mynd1', 
                 'mynd2', 
                 'mynd3', 
                 'mynd4', 
                 'mynd5', 
                 'mynd6',
                 'mynd7', 
                 'mynd8', 
                 'mynd9', 
                 'mynd10', 
                 'mynd11', 
                 'mynd12', 
                 'mynd13', 
                 'mynd14', 
                 'mynd15', 
                 'mynd16', 
                 'mynd17', 
                 'mynd18', 
                 'mynd19', 
                 'mynd20'
                 ]
        labels = {
            'nr':'Nr. báts', 
            'nafn':'Nafn og umdæmisnúmer báts', 
            'lys_vel_selj':'Vélbúnaður',
            'lys_taeki_selj':'Tækjabúnaður (já/nei/gerð)',
            'lys_fylgi_selj':'Hvað fylgir bátnum?',
            'lys_annad_selj':'Annað',
            'tengil_nafn':'Nafn tengiliðs',
            'tengil_tp':'Tölvupóstur tengiliðs',
            'tengil_simi':'Sími tengiliðs',
            'mynd1':'Tengdu mynd nr. 1',
            'mynd2':'Tengdu mynd nr. 2',
            'mynd3':'Tengdu mynd nr. 3',
            'mynd4':'Tengdu mynd nr. 4',
            'mynd5':'Tengdu mynd nr. 5',
            'mynd6':'Tengdu mynd nr. 6',
            'mynd7':'Tengdu mynd nr. 7',
            'mynd8':'Tengdu mynd nr. 8',
            'mynd9':'Tengdu mynd nr. 9',
            'mynd10':'Tengdu mynd nr. 10',
            'mynd11':'Tengdu mynd nr. 11',
            'mynd12':'Tengdu mynd nr. 12',
            'mynd13':'Tengdu mynd nr. 13',
            'mynd14':'Tengdu mynd nr. 14',
            'mynd15':'Tengdu mynd nr. 15',
            'mynd16':'Tengdu mynd nr. 16',
            'mynd17':'Tengdu mynd nr. 17',
            'mynd18':'Tengdu mynd nr. 18',
            'mynd19':'Tengdu mynd nr. 19',
            'mynd20':'Tengdu mynd nr. 20',
            }
