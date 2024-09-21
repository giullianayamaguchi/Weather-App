from django.shortcuts import render
from forms import CEP
from .api import api_chamar

def index(request):
    endereço = ''
    form = CEP(request.POST)
      
    if request.method == 'POST' and form.is_valid():
        
        cep = form.cleaned_data.get('cep')
        endereço = api_chamar(cep)

        if not endereço:
            endereço = 'Nenhum dado encontrado' 
            
    context = { 
        'form':form,
        'endereço':endereço
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )
