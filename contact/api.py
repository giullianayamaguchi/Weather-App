def api_chamar(cep):
    import requests

    response  = requests.get(f'https://brasilapi.com.br/api/cep/v2/{cep}')
    
    if response.status_code == 200:
        endereço = response.json()
        return endereço['street']
    else: 
        erro = f'Erro {response.status_code} na api'
        return erro