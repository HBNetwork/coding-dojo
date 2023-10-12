"""
fonte: https://www.codewars.com/kata/55983863da40caa2c900004e

Crie uma função que receba um inteiro positivo e retorne o próximo número maior que pode ser formado pela reorganização de seus dígitos. Por exemplo:

   12 ==> 21
  513 ==> 531
2017 ==> 2071

Se os dígitos não puderem ser reorganizados para formar um número maior, retorne None

  9 ==> None
111 ==> None
531 ==> None


Participantes:
1 - Conrado
2 - Lins
3 - Everton
4 - Lucas
5 - Fred


"""


import pytest

from itertools import permutations

def permutacoes(numero):
    digitos = list(str(numero))
    permutacoes = permutations(digitos)
    numeros_permutados = [int(''.join(p)) for p in permutacoes if int(''.join(p)) > numero]
    print(numeros_permutados)
    if len(numeros_permutados) == 0:
        return None
    return min(numeros_permutados)



def invertido(num):
    num = list(str(num))
    tamanho_numero = len(num) - 1
    indice_final = tamanho_numero
    indice_inicial = tamanho_numero - 1
    while True:
        if num[indice_inicial] < num[indice_final]:
            num[indice_inicial], num[indice_final] = num[indice_final], num[indice_inicial]
            return int(''.join(num))
        else:
            indice_inicial -= 1
            indice_final -= 1
            if indice_inicial == -1 or indice_final == -1:
                return None


#  ## -- CÓDIGO GERADO PELO CHATGPT 
# def next_greater_permutation(n):
#     # Convertendo o número para uma lista de dígitos
#     digits = list(str(n))
    
#     # Encontrando o índice do primeiro dígito que é menor que o próximo dígito
#     i = len(digits) - 2
#     while i >= 0 and digits[i] >= digits[i + 1]:
#         i -= 1
    
#     # Se todos os dígitos estão em ordem decrescente, não é possível reorganizar para um número maior
#     if i == -1:
#         return None
    
#     # Encontrando o índice do próximo dígito maior que digits[i]
#     j = len(digits) - 1
#     while digits[j] <= digits[i]:
#         j -= 1
    
#     # Trocando os dígitos em positions i e j
#     digits[i], digits[j] = digits[j], digits[i]
    
#     # Revertendo os dígitos após a posição i para obter a menor permutação maior possível
#     digits[i + 1:] = reversed(digits[i + 1:])
    
#     # Convertendo a lista de dígitos de volta para um número inteiro
#     result = int(''.join(digits))
    
#     return result

def test_invertido():  
    assert invertido(12) == 21
    assert invertido(513) == 531
    assert invertido(2017) == 2071
    assert invertido(2033) == 2303
    assert invertido(1030) == 1300
    assert invertido(17333) == 31337
    # assert invertido(9) == None
    # assert invertido(111) == None
    # assert invertido(531) == None
    # assert invertido(53) == None

    assert permutacoes(12) == 21
    assert permutacoes(513) == 531
    assert permutacoes(2017) == 2071
    assert permutacoes(2033) == 2303
    assert permutacoes(1030) == 1300
    assert permutacoes(17333) == 31337
    assert permutacoes(9) == None
    assert permutacoes(111) == None
    assert permutacoes(531) == None


if __name__ == "__main__":
    pytest.main(['-svv', __file__])

