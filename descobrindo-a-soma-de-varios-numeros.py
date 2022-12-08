"https://dojopuzzles.com/problems/descobrindo-a-soma-de-varios-numeros/"
"""
.DATA: 07/11/2022 

 Este problema ainda não foi utilizado em nenhum Dojo.
Grande parte das linguagens de programação disponibilizam em sua lógica e sintâxe Loops para que um processo longo e repetitivo possa ser feito, dando menos trabalho ao programador, mas e se considerarmos que em sua linguagem de programação não tenha o método Loop e para piorar você terá que fazer algo que nunca imaginou sem o loop: 

1º Descubra a soma de um número x até um número y. 
2º Descubra a soma de todos números impares de um número x até um número y. 
3º Descubra a soma de todos números pares de um número x até um número y. 
"""
"""

- Greg
- Márcio
- David
- Cássio
-
-

"""
import pytest


def soma_intervalo(x, y, soma=0):

    soma += x
    if y - x == 0:
        return soma
    return soma_intervalo(x + 1, y, soma)


def soma_intervalo_impares(x, y, impares=[]):
    print(impares)
    if x % 2 == 1:
        impares.append(x)
  
    if y - x == 0:
        return sum(impares)
    
    return soma_intervalo_impares(x + 1, y, impares)


def test_soma_intervalo():
    assert soma_intervalo(1, 2) == 3
    assert soma_intervalo(1, 3) == 6
    assert soma_intervalo(1, 4) == 10
    assert soma_intervalo(1, 5) == 15
    assert soma_intervalo(3, 6) == 18


def test_soma_intervalo_impares():
    assert soma_intervalo_impares(1, 3) == 4
    assert soma_intervalo_impares(2, 5, []) == 8
    assert soma_intervalo_impares(3, 5, []) == 8


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
