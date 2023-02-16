"""
Data: 15/02/2023

Fonte do Desafio: https://dojopuzzles.com/problems/descobrindo-a-soma-de-varios-numeros/

Enunciado:
Grande parte das linguagens de programação disponibilizam em sua lógica e sintâxe Loops para que um processo longo e repetitivo possa ser feito, dando menos trabalho ao programador, mas e se considerarmos que em sua linguagem de programação não tenha o método Loop e para piorar você terá que fazer algo que nunca imaginou sem o loop: 1º Descubra a soma de um número x até um número y. 2º Descubra a soma de todos números impares de um número x até um número y. 3º Descubra a soma de todos números pares de um número x até um número y.


Participantes:
1 - Carlos Xavier
2 - Everton Matos
3 - Luiz Carlos
4 - Álisson Holkem
5 - Gregorio
6 - 
7 - 
8 - 
9 - 

"""

import pytest


def soma_com_recursao(x, y, resultado=0):
    soma_resultado = resultado + x
    #print(x, y, resultado, soma_resultado)
    if x == y:
        return soma_resultado
    else:
        return soma_com_recursao(x + 1, y, soma_resultado)


def soma_com_recursao_impar(x, y, resultado=0):
    soma_resultado = resultado

    if x % 2 != 0:
        soma_resultado = soma_resultado + x

    if x == y:
        return soma_resultado
    else:
        return soma_com_recursao_impar(x + 1, y, soma_resultado)


def soma_com_recursao_impar_v2(x, y, resultado=0):
    soma_resultado = resultado + x
    if x % 2 == 0:
        soma_resultado = soma_resultado - x

    if x == y:
        return soma_resultado
    else:
        return soma_com_recursao_impar_v2(x + 1, y, soma_resultado)

def soma_com_recursao_par(x, y, resultado=0):
    soma_resultado = resultado

    if x % 2 == 0:
        soma_resultado = soma_resultado + x

    if x == y:
        return soma_resultado
    else:
        return soma_com_recursao_par(x + 1, y, soma_resultado)


def soma_com_loop(x, y):
    resultado = 0
    while x <= y:
        resultado += x
        x += 1

    return resultado


def test_soma():
    assert soma_com_loop(1, 3) == 6
    assert soma_com_loop(3, 6) == 18
    assert soma_com_recursao(1, 3) == 6
    assert soma_com_recursao(3, 6) == 18
    assert soma_com_recursao_impar(1, 7) == 16
    assert soma_com_recursao_impar(1, 5) == 9
    assert soma_com_recursao_impar_v2(1, 7) == 16
    assert soma_com_recursao_impar_v2(1, 5) == 9
    assert soma_com_recursao_par(1, 5) == 6
    assert soma_com_recursao_par(1, 9) == 20


if __name__ == "__main__":
    pytest.main(["-s", __file__])
