
from django import forms

class RenewForm(forms.Form):
    renewal_data = forms.CharField(help_text="Enter new data.")


    def clean_renewal_discard(self):
        data = self.cleaned_data['renewal_data']

        return data

