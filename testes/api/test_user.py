# Done: 1 - criar um teste que adicione um usuário
# done: 2 - realizar o login e extrair o toke da resposta

import requests

from testes.api.test_pet import headers

url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
token = ''



def teste_incluir_user():
    # Configura
    # Dados de Entrada
    # Virão do arquivo user1.json

    # Resultados Esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '9500128'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\dell\\PycharmProjects\\pythonProject134inicial1\\vendors\\json\\user1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


def teste_login_positivo():
    # Configura
    # Dados de Entrada
    username = 'lucas'
    password = 'lucy'

    # Resultados Esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session:'

    # Executa
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])

    # Extrai
    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'A mensagem = {mensagem_extraida}')
    token = mensagem_extraida[23:] # [inicio:fim]
    print(f'O token = {token}')

    # [inicio : fim : passos
