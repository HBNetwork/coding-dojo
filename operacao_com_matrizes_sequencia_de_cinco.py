"""
31/05/2023 e 07/06/2023

Fonte: https://dojopuzzles.com/problems/sequencia-de-cinco/
Problema: Seqüência de Cinco
Enunciado:

Dado uma matriz de números inteiros positivos de dimensões n x n, onde n >= 5, encontre o maior produto de uma seqüência de 5 números consecutivos (a seqüência pode estar na vertical, na horizontal ou na diagonal).

Por exemplo, a matriz abaixo retorna 32:

2 1 1 1 1
1 2 1 1 1
1 1 2 1 1
1 1 1 2 1
1 1 1 1 2


Participantes:
- Leonardo Cotta
- Frederico Fávaro
- Márcio Conrado
- Luiz Carlos
- Álisson Holkem
- Everton Matos
- Samuel 
- Cássio Augusto
- Gregorio


"""

import pytest
import random
import numpy as np

matriz = [[2, 1, 3, 1, 1], [1, 2, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 2, 1],
          [1, 1, 1, 1, 2]]

matriz2 = [[2, 1, 3, 1, 1, 2], [1, 2, 1, 1, 1, 2], [1, 1, 2, 1, 1, 2],
           [1, 1, 1, 2, 1, 2], [1, 1, 1, 1, 2, 2]]

matriz3 = [[2, 1, 3, 1], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2]]

matriz4 = [[8, 7, 10, 4, 5, 9, 3, 2], [4, 7, 10, 3, 5, 8, 6, 1],
           [2, 1, 5, 6, 4, 7, 9, 10], [10, 5, 6, 1, 9, 8, 3, 2],
           [5, 4, 6, 2, 1, 9, 8, 7], [8, 7, 5, 2, 4, 9, 3, 10],
           [3, 7, 2, 4, 5, 1, 8, 6], [6, 4, 1, 5, 2, 7, 9, 10]]


def gerar_matriz(n):
    #solução usando o numpy: np.random.randint(1,99, (5,5))
    matriz = []
    itens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(n):
        matriz.append(random.sample(itens, k=n))
    return matriz


def printa_matriz(matriz):
    for linha in matriz:
        for item in linha:
            print(item, end=', ')
        print(end='\n')


def calcula_produto(linha):
    seq1 = 1
    for item in linha:
        seq1 *= item
    return seq1


def transposicao(matriz_original):
    matriz_transposta = []
    transp = []
    for i, linha in enumerate(matriz_original):
        for e, item in enumerate(linha):
            transp.append(matriz_original[e][i])
        matriz_transposta.append(transp.copy())
        transp.clear()
    return matriz_transposta


def produto_diagonal(diagonal):
    return calcula_produto(diagonal)


def extrator_diagonal(matriz):
    diagonal_1 = []
    diagonal_2 = []

    for i, linha in enumerate(matriz):
        diagonal_1.append(linha[i])
        diagonal_2.append(linha[::-1][i])
        continue

    return [diagonal_1, diagonal_2]


def maior_produto(matriz):
    diagonais = extrator_diagonal(matriz)
    diagonal = 0
    if produto_diagonal(diagonais[0]) >= produto_diagonal(diagonais[1]):
        diagonal = produto_diagonal(diagonais[0])
    else:
        diagonal = produto_diagonal(diagonais[1])

    vertical = 0
    trasposta = transposicao(matriz)
    for linha in trasposta:
        if vertical < calcula_produto(linha):
            vertical = calcula_produto(linha)

    horizontal = 0
    for linha in matriz:
        if horizontal < calcula_produto(linha):
            horizontal = calcula_produto(linha)

    maior = horizontal
    if vertical >= horizontal:
        maior = vertical
    if diagonal > maior:
        maior = diagonal

    return maior


def verifica_matriz_quadrada(matriz):
    tam_matriz = len(matriz)
    if tam_matriz < 5:
        return 'A matriz precisa ser maior ou igual a 5'

    quantidade_da_matriz = 0
    for _ in matriz:
        for _ in _:
            quantidade_da_matriz += 1

    if quantidade_da_matriz / tam_matriz == tam_matriz:
        return quantidade_da_matriz
    return 'Não é uma matriz quadrática'


def test_calcula_produto():
    assert calcula_produto(matriz[0]) == 6
    assert calcula_produto(matriz[1]) == 2
    assert calcula_produto(matriz[2]) == 2
    assert calcula_produto(matriz[3]) == 2
    assert calcula_produto(matriz[4]) == 2


def test_produto_coluna():
    trasposta = transposicao(matriz)
    assert calcula_produto(trasposta[0]) == 2
    assert calcula_produto(trasposta[1]) == 2
    assert calcula_produto(trasposta[2]) == 6
    assert calcula_produto(trasposta[3]) == 2
    assert calcula_produto(trasposta[4]) == 2


def test_transposicao():
    assert transposicao([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_produto_diagonal():
    assert produto_diagonal([2, 2, 2, 2, 2]) == 32


def test_extrator_diagonal():
    assert extrator_diagonal(matriz) == [[2, 2, 2, 2, 2], [1, 1, 2, 1, 1]]


def test_resultado_diagonal():
    resultado = extrator_diagonal(matriz)
    assert produto_diagonal(resultado[0]) == 32
    assert produto_diagonal(resultado[1]) == 2


def test_maior_produto():
    assert maior_produto(matriz) == 32
    assert maior_produto(matriz) == 32
    assert maior_produto(matriz4) == 2286144


def test_gerar_matriz():
    assert type(gerar_matriz(5)) == list


def test_verifica_matriz_quadrada():
    assert verifica_matriz_quadrada(matriz) == 25
    assert verifica_matriz_quadrada(matriz2) == 'Não é uma matriz quadrática'
    assert verifica_matriz_quadrada(
        matriz3) == 'A matriz precisa ser maior ou igual a 5'
    assert verifica_matriz_quadrada(gerar_matriz(8)) == 64
    assert verifica_matriz_quadrada(np.random.randint(1, 99, (5, 5))) == 25


if __name__ == "__main__":
    printa_matriz(gerar_matriz(8))
    print(np.random.randint(1, 99, (5, 5)))

    pytest.main(['-svv', __file__])
