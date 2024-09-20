from django import forms

class CEP(forms.Form):
    cep = forms.CharField(label='Seu CEP', max_length=10)