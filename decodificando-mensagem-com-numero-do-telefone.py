"""
Data: 15/02/2023

Fonte do Desafio: https://dojopuzzles.com/problems/encontre-o-telefone/

Enunciado:

Em alguns lugares é comum lembrar um número do telefone associando seus dígitos a letras. Dessa maneira a expressão MY LOVE significa 69 5683. Claro que existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra ou uma frase e os dígitos 1 e 0 não estão associados a nenhuma letra.

Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado na tabela abaixo. Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.

Letras  ->  Número 
ABC     ->  2 
DEF     ->  3 
GHI     ->  4 
JKL     ->  5 
MNO     ->  6 
PQRS    ->  7 
TUV     ->  8 
WXYZ    ->  9 


Entrada

A entrada consiste de um conjunto de expressões. Cada expressão está sozinha em uma linha e possui C caracteres, onde 1 ≤ C ≤ 30. A entrada é terminada por fim de arquivo (EOF).


Saída

Para cada expressão você deve imprimir o número de telefone correspondente.


Exemplo de entrada:
1-HOME-SWEET-HOME 
MY-MISERABLE-JOB

Saída correspondente:
1-4663-79338-4663 
69-647372253-562


Curiosidades

A frase "The quick brown fox jumps over the lazy dog" é um pangrama (frase com sentido em que são usadas todas as letras do alfabeto de determinada língua) da língua inglesa.


Participantes:
1 - Carlos Xavier
2 - Everton Matos
3 - Cássio
4 - Gregorio
5 - HB
6 - Luiz Carlos


"""

import pytest


def expressao(text):
    output = ''

    for x in text:
        if x in "ABC":
            output += "2"
        elif x in "DEF":
            output += "3"
        elif x in "GHI":
            output += "4"
        elif x in 'JKL':
            output += '5'
        elif x in 'MNO':
            output += '6'
        elif x in 'PQRS':
            output += '7'
        elif x in 'TUV':
            output += '8'
        elif x in 'WXYZ':
            output += '9'
        else:
            output += x

    return output


#
# teclas = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


def expressao_com_dicionario(text):
    output = ''
    num = {
        'A': '2',
        'B': '2',
        'C': '2',
        'D': '3',
        'E': '3',
        'F': '3',
        'G': '4',
        'H': '4',
        'I': '4',
        'J': '5',
        'K': '5',
        'L': '5',
        'M': '6',
        'N': '6',
        'O': '6',
        'P': '7',
        'Q': '7',
        'R': '7',
        'S': '7',
        'T': '8',
        'U': '8',
        'V': '8',
        'W': '9',
        'X': '9',
        'Y': '9',
        'Z': '9',
    }

    for x in text:
        if x in num:
            output += num[x]
        else:
            output += x

    return output


def test_expressao():
    assert expressao('M') == '6'
    assert expressao('Y') == '9'
    assert expressao('-') == '-'
    assert expressao('N') == '6'
    assert expressao('MY') == '69'
    assert expressao('MY-LOVE') == '69-5683'
    assert expressao('HOME-SWEET-HOME') == '4663-79338-4663'
    assert expressao('MY-MISERABLE-JOB') == '69-647372253-562'
    assert expressao_com_dicionario('A') == '2'
    assert expressao_com_dicionario('AD') == '23'
    assert expressao_com_dicionario('AD-E') == '23-3'
    assert expressao_com_dicionario('MY-LOVE') == '69-5683'
    assert expressao_com_dicionario('HOME-SWEET-HOME') == '4663-79338-4663'



if __name__ == "__main__":
    pytest.main(["-s", __file__])
