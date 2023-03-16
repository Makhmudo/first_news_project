from django import forms
from .models import Contack

class ContackForm(forms.ModelForm):

    class Meta:
        model = Contack
        fields ='__all__'

class SubscriptionForm(forms.Form):
    subject = forms.CharField()