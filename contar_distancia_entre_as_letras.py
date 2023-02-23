"""
22/02/2023

https://dojopuzzles.com/problems/entre-letras/

Faça um programa que receba duas letras, e diga quantas letras há entre elas. As letras passadas devem estar em ordem alfabética. Se não estiverem o programa deve avisar o usuário. Exemplo: 'a', 'b' = 0 'a', 'c' = 1 'a', 'z' = 24 'w', 'e' = Não está na ordem alfabética


"""
"""
Participantes:
 
 - joão m. 
 - Greg
 - luiz
 - Everton
 - Álisson
 

"""
import pytest


def contar_distancia_entre_letras(letra1, letra2):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    posicao_letra1 = alfabeto.index(letra1.lower())
    posicao_letra2 = alfabeto.index(letra2.lower())
    if posicao_letra1 > posicao_letra2:
        resp = 'Não está na ordem alfabética'
    elif posicao_letra1 == posicao_letra2:
        resp = 'Duas letras são iguais'
    else:
        resp = (posicao_letra2 - posicao_letra1) - 1
    return resp


def contar_distancia_entre_letras_v2(letra1, letra2):
    # Esta versão permite que as variáveis não estejam em ordem alfabética
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    posicao_letra1 = alfabeto.index(letra1.lower()) + 1
    posicao_letra2 = alfabeto.index(letra2.lower()) + 1

    if posicao_letra1 > posicao_letra2:
        calculando_ate_z = alfabeto.index('z') - posicao_letra1
        calculando_ate_a_ate_letra2 = posicao_letra2 - alfabeto.index('a')
        resp = (calculando_ate_z + calculando_ate_a_ate_letra2)
    elif posicao_letra1 == posicao_letra2:
        resp = 'Duas letras são iguais'
    else:
        resp = (posicao_letra2 - posicao_letra1) - 1

    return resp


def test_contar_distancia_entre_letras():
    assert contar_distancia_entre_letras("a", "b") == 0
    assert contar_distancia_entre_letras("a", "c") == 1
    assert contar_distancia_entre_letras("a", "z") == 24
    assert contar_distancia_entre_letras("b", "d") == 1
    assert contar_distancia_entre_letras("a", "a") == 'Duas letras são iguais'
    assert contar_distancia_entre_letras("A", "d") == 2
    assert contar_distancia_entre_letras("b", "a") == 'Não está na ordem alfabética'

    assert contar_distancia_entre_letras_v2("x", "b") == 3
    assert contar_distancia_entre_letras_v2("b", "a") == 24
    assert contar_distancia_entre_letras_v2("a", "a") == 'Duas letras são iguais'



if __name__ == "__main__":
    pytest.main(["-s", __file__])

# import string
# a = list(string.ascii_lowercase)

# print (a)
