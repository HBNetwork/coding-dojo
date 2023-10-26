'''
DATA: 25/10/2023

FONTE: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python

ORDENAR TIPO CARACOL

Dado um array n x n, retorne os elementos do array organizados dos elementos mais externos para o elemento do meio, 
viajando no sentido horário.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]


Para melhor compreensão, siga os números da próxima matriz consecutivamente:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTA: A ideia não é ordenar os elementos do valor mais baixo para o mais alto; a ideia é percorrer a matriz 2-d em um padrão 
de caracol no sentido horário.

NOTA 2: A 0x0 (matriz vazia) é representada como um array vazio dentro de um array [[]].

ENUNCIADO: 

PARTICIPANTES:
-
- Adailton
- MCOnrado
- Greg
- Lucas
- João M.
- Frederico
- Luiz Lins
- Gustavo

'''

import pytest


def frente(matriz, posicao):
  extracao = matriz[posicao]
  del matriz[posicao]
  return extracao


def baixo(matriz):
  extracao = []
  for i in matriz:
    extracao += [i[-1]]
    del i[-1]
  return extracao


def tras(matriz):
  extracao = []
  if len(matriz) > 0: 
    extracao = matriz[-1][::-1]
    del matriz[-1]
  return extracao


def cima(matriz):
  extracao = []
  for i in matriz:
    extracao += [i[0]]
    del i[0]
  return extracao[::-1]


def caracol(matriz):
  retorno = []

  while len(matriz) > 0:
    print(retorno)
    print(f'matriz inicial {matriz}')
    retorno.extend(frente(matriz, 0))
    retorno.extend(baixo(matriz))
    #print(f'matriz antes do tras {matriz}')
    retorno.extend(tras(matriz))
    retorno.extend(cima(matriz))

  return retorno


# def snail(matriz):
# results = []

# while len(matriz) > 0:

#     results += matriz[0]
#     del matriz[0]

#     if len(matriz) > 0:
#         for i in matriz:
#             results += [i[-1]]
#             del i[-1]

#         if matriz[-1]:
#             results += matriz[-1][::-1]
#             del matriz[-1]

#         for i in reversed(matriz):
#             results += [i[0]]
#             del i[0]

# return results


def test_caracol():
    assert caracol([[1, 2, 3], [4, 5, 6], [7, 8,
                                         9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    assert caracol([[1,2,3,1], [4,5,6,4], [7,8,9,7], [7,8,9,7]]) == [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8]


def test_frente():
  matriz_exemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  assert frente(matriz_exemplo, 0) == [1, 2, 3]
  assert matriz_exemplo == [[4, 5, 6], [7, 8, 9]]


def test_baixo():
  matriz_exemplo = [[4, 5, 6], [7, 8, 9]]
  assert baixo(matriz_exemplo) == [6, 9]
  assert matriz_exemplo == [[4, 5], [7, 8]]


def test_tras():
  matriz_exemplo = [[4, 5], [7, 8]]
  assert tras(matriz_exemplo) == [8, 7]
  assert matriz_exemplo == [[4, 5]]


def test_cima():
  matriz_exemplo = [[4, 5]]
  assert cima(matriz_exemplo) == [4]
  assert matriz_exemplo == [[5]]


if __name__ == "__main__":
  pytest.main(['-svv', __file__])
