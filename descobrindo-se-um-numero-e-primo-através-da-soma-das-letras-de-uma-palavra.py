"""
DATA: 07/03/2023
FONTE: https://dojopuzzles.com/problems/palavras-primas/

ENUNCIADO: 
Um número primo é definido se ele possuir exatamente dois divisores: o número um e ele próprio. São exemplos de números primos: 2, 3, 5, 101, 367 e 523.

Neste problema, você deve ler uma palavra composta somente por letras [a-zA-Z]. Cada letra possui um valor específico, a vale 1, b vale 2 e assim por diante, até a letra z que vale 26. Do mesmo modo A vale 27, B vale 28, até a letra Z que vale 52.

Você precisa definir se cada palavra em um conjunto de palavras é prima ou não. Para ela ser prima, a soma dos valores de suas letras deve ser um número primo.

PARTICIPANTES:
- Greg
- Frederico
- Alisson
- Leonardo Oliveira
- Luiz
- 

"""
import pytest
from unidecode import unidecode
'''
Valores correspondentes na tabela ascii para as letras
A - 65 Z -  90  (-38)
a - 97 z - 122 (-96)

-----
Indice desejado pelo descritivo do enunciado para cada letra
a -1 
z-26
A-27
...

'''


def palavras_primas(palavra):
    palavra = unidecode(palavra)  #remove os caracteres com acentos
    soma_letras_palavras = 0
    i = 0
    while i < len(palavra):
        valor_letra = ord(palavra[i])  # valor correspondente da tabela ascii

        if palavra[i].isupper():
            valor_letra = valor_letra - 38  # se for maíuscula aplica o fator de ajuste -38
        else:
            valor_letra = valor_letra - 96  # se for maíuscula aplica o fator de ajuste -96
        soma_letras_palavras += valor_letra
        i += 1

    #print(soma_letras_palavras)

    return eh_primo(soma_letras_palavras)


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


def test_palavras_primas():
    assert (palavras_primas("Á") == False)
    assert (palavras_primas("AaBb") == False)
    assert (palavras_primas("Codigo") == True)
    assert (palavras_primas("Gregorio") == False)
    assert (palavras_primas("gregorio") == False)
    assert (palavras_primas("GREGORIO") == False)
    assert (palavras_primas("Álisson") == False)
    assert (palavras_primas("Frederico") == True)
    assert (palavras_primas("Luiz") == False)


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
