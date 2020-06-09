from onlineOrderSystem.models import DataSheet
from django import forms

class RenewForm(forms.ModelForm):

    class Meta:
        model = DataSheet
        fields = ['progress']

