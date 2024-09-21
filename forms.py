from django import forms

class CEP(forms.Form):

    cep = forms.CharField(label='Seu CEP', max_length=10, error_messages={
            'required': 'Por favor, insira somente numeros'  })

    