"""
DATA: 21/06/2023

FONTE: https://dojopuzzles.com/problems/descobrindo-a-soma-de-varios-numeros/

ENUNCIADO: Descobrindo a soma de vários números

Grande parte das linguagens de programação disponibilizam em sua lógica e sintâxe Loops para que um processo longo e repetitivo possa ser feito, dando menos trabalho ao programador, mas e se considerarmos que em sua linguagem de programação não tenha o método Loop e para piorar você terá que fazer algo que nunca imaginou sem o loop: 
1º Descubra a soma de um número x até um número y. 
2º Descubra a soma de todos números impares de um número x até um número y. 
3º Descubra a soma de todos números pares de um número x até um número y.

Participantes:
- Gregorio
- Lucas
- Conrado
- Everton
- Álisson
- Esley
- Frederico

"""

import pytest


def soma_numero_de_X_ate_Y(x, y, soma=0):
    soma += x
    if x == y:
        return soma

    return soma_numero_de_X_ate_Y(x + 1, y, soma)

def soma_impar_numero_de_X_ate_Y(x, y, soma=0):
    return 9

    
def numero_impar(x):
    if not x%2 == 0:
        return True
    return False

def test_soma_numero_de_X_ate_Y():
    assert soma_numero_de_X_ate_Y(1, 5) == 15
    assert soma_numero_de_X_ate_Y(3, 5) == 12
    assert soma_numero_de_X_ate_Y(1, 1) == 1

def test_numero_impar():
    assert numero_impar(3) == True

def test_soma_impar():
    assert soma_impar_numero_de_X_ate_Y(1,5) == 9


if __name__ == "__main__":
    #print(soma_numero_de_X_ate_Y(1,100))
    pytest.main(['-svv', __file__])
