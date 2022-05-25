# done: 3 - criar uma venda de um pet para um usuário
# ToDo: 4 - consultar os dados do pet que foi vendido
import json
import os

import requests

url = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}


def teste_vender_pet():
    # Configura
    # Dados de entrada
    # Virao do arquivo pedido1.json

    # Resultados esperados
    status_code_esperado = 200
    pedido_id_esperado = 9817381217
    pet_id_esperado = 1280950
    status_pedido_esperado = 'placed'

    # Executa
    caminho = os.path.abspath(__file__ + "/../../../") + os.sep + 'vendors' + os.sep + 'json' + os.sep

    resultado_obtido = requests.post(
        url=url + 'store/order',
        headers=headers,
        data=open(caminho + 'order1.json')
    )

    # Validação
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pedido_id_esperado
    assert corpo_do_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    # Extração

    pet_id_extraido = corpo_do_resultado_obtido.get('petId')
    status_code_esperado = 200

    # Configura
    # Dados de entrada
    # Realizar a 2 Transação

    # Configura
    # Dados de entrada
    # Realizar a 1 Transação acima

    # Resultado Esperado
    pet_name_esperado = 'Thanos'

    # Executa

    resultado_obtido = requests.get(
        url=url + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))
    assert corpo_do_resultado_obtido['name'] == pet_name_esperado
