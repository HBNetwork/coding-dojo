"""
DATA: 17/05/2023
FONTE: https://dojopuzzles.com/problems/geracao-de-fatores-primos/
ENUNCIADO: Descobrindo os fatores primos de um número

Todo número inteiro positivo pode ser representado pelo produto de potências de números primos (os chamados fatores primos).

Por exemplo o número 6 pode ser representado pelo produto do números primos 2 x 3.

Outros exemplos:

5 = 5 (números primos só tem um fator primo - ele mesmo)

100 = 2 x 2 x 5 x 5
198 = 2 x 3 x 3 x 11
276 = 2 x 2 x 3 x 23

Desenvolva um programa que dado um número inteiro positivo, retorne os seus fatores primos

https://github.com/HBNetwork/coding-dojo/blob/main/descobrindo-se-um-numero-e-primo-atrav%C3%A9s-da-soma-das-letras-de-uma-palavra.py

Participantes:
- Greg
- Conrado
- João.M
- Frederico
- David
- Luiz
- 


"""
import pytest
import numpy


def eh_primo(numero):
    e_primo = False
    if numero % 2 == 0:
        if numero == 2:
            e_primo = True
    else:
        for divisor in range(2, numero):
            if (numero % divisor == 0):
                e_primo = False
                break
            else:
                e_primo = True
    return e_primo


def decompor_ate_fatores_primos(numero):
    divisor = 2
    fatores_primos = []
    numero_de_entrada = numero
    
    if numero == 1:
        return  [1]
    
    while True:
        if eh_primo(divisor):
            if (numero % divisor  == 0):
                fatores_primos.append(divisor)
                numero = numero / divisor
            else:
                divisor += 1
        else:
            divisor += 1
        if numero_de_entrada == numpy.prod(fatores_primos):
            break
            
    return fatores_primos

def test_decompor_ate_fatores_primos():  
    assert decompor_ate_fatores_primos(1) == [1]
    assert decompor_ate_fatores_primos(11) == [11]
    assert decompor_ate_fatores_primos(100) == [2, 2, 5, 5]
    assert decompor_ate_fatores_primos(198) == [2,3,3,11] 
    assert decompor_ate_fatores_primos(276) == [2,2,3,23] 
    assert decompor_ate_fatores_primos(987) == [3,7,47]     
    assert decompor_ate_fatores_primos(9875) == [5,5,5,79]
    #assert decompor_ate_fatores_primos(98675849) == [2,2,3,23] 
    
    
def test_eh_primo():    
    assert eh_primo(100) == False
    assert eh_primo(5) == True

if __name__ == "__main__":
    pytest.main(['-svv', __file__])