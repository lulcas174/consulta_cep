import requests
import json



def consulta(cep):
    cep = cep.replace('-', '')
    url = f'https://viacep.com.br/ws/{cep}/json/'
    headers = {'Content-Type': 'application/json'}
    resposta = requests.request('GET',url)
    conteudo = resposta.content.decode('utf-8')
    resposta.close()
    endereco = json.loads(conteudo)

    return endereco

def cep_valido(cep):
    if len(cep) == 7 and 9:
        print('Cep inválido')
   
    return cep
  


def main():
    cep = ''
    
    while cep != 'sair':
        cep=input('CEP: ')

        if cep_valido(cep):
            endereco = consulta(cep)
            if not endereco.get('error'):
                print('Cidade:', endereco['localidade'])
                print('UF:', endereco['uf'])
                print('Bairro:', endereco['bairro'])
                print('Logradouro:', endereco['logradouro'])
                print('CEP:', endereco['cep'])
                print('\n\n')


if __name__ == '__main__':
    main()