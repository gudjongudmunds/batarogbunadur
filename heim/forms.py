from django import forms
from .models import Fyrirspurn

class FyrirspurnForm(forms.ModelForm):
    class Meta:
        model = Fyrirspurn
        fields = ['nafn', 'tp', 'titill', 'fyrirspurn']
        labels = {'nafn':'Nafn', 'tp':'Tölvupóstur', 'titill':'Titill', 'fyrirspurn':'Fyrirspurn'}
