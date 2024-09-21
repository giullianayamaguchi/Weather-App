def api_chamar(cep):
    import requests

    response  = requests.get(f'https://brasilapi.com.br/api/cep/v2/{cep}')
    
    if response.status_code == 200:
        dados = response.json()
        endereço = {
            'street' : dados.get('street', 'Não encontrado'), 
            'city' : dados.get('city', 'Não encontrado'), 
            'neighborhood' : dados.get('neighborhood', 'Não encontrado'), 
            'state' : dados.get('state', 'Não encontrado')
        }
        return endereço
    else: 
        erro = f'Erro {response.status_code} na api'
        return erro