"""
DATA: 15/03/2023
FONTE: https://leetcode.com/problems/pascals-triangle/

ENUNCIADO: Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 
Constraints:

1 <= numRows <= 30


PARTICIPANTES:
- Vitor Pestana
- Greg MASTER 
- João Moreno
- Conrado
- Álisson
- Luiz
- Everton
- Fred
- Tiago Chaves

"""

import pytest


def descobrindo_proxima_linha(array_entrada):
    tam_array = len(array_entrada)
    lista_saida = [1]
    
    if tam_array > 1:
        for indice_atual in range(tam_array):
            indice_proximo = indice_atual + 1
            if indice_proximo < tam_array:
                lista_saida.append(array_entrada[indice_atual] + array_entrada[indice_proximo])
    lista_saida.append(1)

    return lista_saida


def descobrindo_proxima_linha_2(array_entrada):
    tam_array = len(array_entrada)
    if tam_array == 1:
        array_retorno = [1, 1]
    else:
        array_retorno = []
        i = 0
        while i <= (tam_array - 1):
            if i != tam_array - 1:
                soma = array_entrada[i] + array_entrada[i + 1]
                array_retorno.append(soma)
            i += 1
    array_retorno.insert(0, 1)
    array_retorno.append(1) #array_retorno.insert(tam_array, 1)

    return array_retorno

def montando_triangulo_pascal(n):
    retorno = [[1],]
    for i in range(n - 1):
        saida = descobrindo_proxima_linha(retorno[i])
        retorno.append(saida)
    return retorno
    

def test_descobrindo_proxima_linha():
    assert descobrindo_proxima_linha([1]) == [1, 1]
    assert descobrindo_proxima_linha([1, 1]) == [1, 2, 1]
    assert descobrindo_proxima_linha([1, 2, 1]) == [1, 3, 3, 1]
    assert descobrindo_proxima_linha([1, 3, 3, 1]) == [1, 4, 6, 4, 1]
    assert descobrindo_proxima_linha_2([1, 1]) == [1, 2, 1]
    assert descobrindo_proxima_linha_2([1, 3, 3, 1]) == [1, 4, 6, 4, 1]
    assert montando_triangulo_pascal(1) == [[1]]
    assert montando_triangulo_pascal(2) == [[1],[1,1]]
    assert montando_triangulo_pascal(3) == [[1],[1,1],[1,2,1]]
    assert montando_triangulo_pascal(4) == [[1],[1,1],[1,2,1],[1,3,3,1]]
    assert montando_triangulo_pascal(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    

if __name__ == "__main__":
    pytest.main(['-svv', __file__])
