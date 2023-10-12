"""
Instruções

Um trigêmeo pitagórico é um conjunto de três números naturais, {a, b, c}, para os quais,

a² b² = c²

e tal que,

a < b < c

Por exemplo,

3² 4² = 5².

Dado um inteiro de entrada N, encontre todas as trincas pitagóricas para as quais a b c = N.

Por exemplo, com N = 1000, existe exatamente um trio pitagórico para o qual a b c = 1000: {200, 375, 425}.

1 - João Moreno
2 - Conrado
3 - Luiz Carlos 
4 - Orlando Saraiva
5 - Everton Matos
6 - Álisson
7 - Lucas
 
"""


import pytest

def soma_triangulo(num1, num2, num3, soma):
    return num1 + num2 + num3 == soma

def pitagoras(num1, num2, num3):
    return num1**2 + num2**2 == num3**2 

def ordenado(num1, num2, num3):
    return num1 < num2 and num2 < num3

def soma_final(soma):
    resultado = []
    for a in range(1, soma // 3):
      for b in range(a, soma):
        c = soma - a - b
        if pitagoras(a, b, c) and ordenado(a, b, c) and soma_triangulo(a, b, c, soma):
          resultado.append([a, b, c])
          
    return resultado
      
def test_soma_triangulo():
    assert soma_triangulo(3, 4, 5, 12) == True
    assert soma_triangulo(3, 4, 6, 12) == False
    assert soma_triangulo(200, 375, 425, 1000) == True

def test_pitagoras():
    assert pitagoras(3, 4, 5) == True
    assert pitagoras(3, 4, 6) == False
    assert pitagoras(200, 375, 425) == True
    assert pitagoras(200, 375, 426) == False

def test_ordenado():
    assert ordenado(3, 4, 5) == True
    assert ordenado(3, 4, 6) == True
    assert ordenado(3, 4, 2) == False
    assert ordenado(200, 375, 425) == True

def test_soma_final():
    assert soma_final(12) == [[3, 4, 5]]
    assert soma_final(1000) == [[200, 375, 425]]
    assert soma_final(10000) == [[2000, 3750, 4250]]
    assert soma_final(24) == [[6, 8, 10]]

if __name__ == "__main__":
    pytest.main(['-svv', __file__])

