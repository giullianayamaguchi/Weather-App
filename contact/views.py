from django.shortcuts import render
from forms import CEP
from .api import api_chamar

def index(request):
    form = CEP(request.POST)
      
    if form.is_valid():
        cep = form.cleaned_data.get('cep')

        endereço = api_chamar(cep)
    
    context = { 
        'form':form,
        'endereço':endereço,
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )
