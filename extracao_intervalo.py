'''
Fonte: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

Exercicio: 
Um formato para expressar uma lista ordenada de números inteiros é usar uma lista separada por vírgulas de qualquer um dos seguintes:

    números inteiros individuais
    ou um intervalo de números inteiros indicado pelo número inicial separado do número final no intervalo por um traço, '-'. O intervalo inclui todos os números inteiros no intervalo, incluindo ambos os pontos de extremidade. Não é considerado um intervalo a menos que abranja pelo menos 3 números. Por exemplo, "12,13,15-17"

Complete a solução para que ela receba uma lista de números inteiros em ordem crescente e retorne uma string formatada corretamente no formato de intervalo.
Exemplo:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
retorna "-10--8,-6,-3-1,3-5,7-11,14,15,17-20" 

Participantes:
- Lucas
- Alisson
- João
- MConrado
- AVC
- Luiz Lins
'''

import pytest


def intervalo(lista):
  retorno = ""
  lista_intervalo = []

  for k, n in enumerate(lista):  # 1, 2
    #print(f'{k} e {n}')
    #print(lista_intervalo)

    if k == 0:  #primeiro elemento da lista
      lista_intervalo.append(n)  #adiciona a nova lista
      if n + 1 == lista[k + 1]:  #verifica o próximo elemento para identificar uma possível sequencia
        continue  # se for uma sequencia pula para o próximo elemento da lista
    elif n - 1 == lista[k - 1]:  #verif
      lista_intervalo.append(n)
      if len(lista) - 1 > k + 1:
        if n + 1 == lista[k + 1]:
          continue
    else:
      lista_intervalo.append(n)
      if len(lista) - 1 > k + 1:
        if n + 1 == lista[k + 1]:
          continue

    if len(lista_intervalo) >= 3:
      retorno += str(lista_intervalo[0]) + "-" + str(lista_intervalo[-1]) + ','
      lista_intervalo = []
    else:
      retorno += str(lista_intervalo[0]) + ','
      lista_intervalo = []

  return retorno[:-1]


def test_intervalo():
  assert intervalo([1,2,3,5,6]) == "1-3,5,6"
  assert intervalo([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5,
                    7]) == "-10--8,-6,-3-1,3-5,7"


if __name__ == "__main__":
  pytest.main(['-svv', __file__])

