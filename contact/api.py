def api_chamar(cep):
    import requests

    endereço = requests.get(f'https://brasilapi.com.br/api/cep/v2/{cep}').json()
    return endereço['street']