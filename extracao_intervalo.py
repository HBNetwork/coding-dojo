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
  ultima_posicao_da_lista = len(lista)-1
  #print(f'len da lista: {len(lista)}')
  lista_sequencia = []
  retorno = ''

  for k, n in enumerate(lista):
    #print(f'Posição: {k} - Número: {n}')
    if k == 0:
      lista_sequencia.append(n)
      if ultima_posicao_da_lista >= k+1:
        if lista[k+1] == n+1:
          continue
    elif lista[k-1] == n-1:
      lista_sequencia.append(n)
      if ultima_posicao_da_lista >= k+1:
        if lista[k+1] == n+1:
          continue
    else:
      lista_sequencia.append(n)
      if ultima_posicao_da_lista >= k+1:
        if lista[k+1] == n+1:
          continue
    
    #print(lista_sequencia)
    
    if len(lista_sequencia) >= 3:
      retorno += '[' + str(lista_sequencia[0]) + ' - ' + str(lista_sequencia[-1]) + '], '
    elif len(lista_sequencia) > 1:
      for numero in lista_sequencia:
        retorno += str(numero) + ', '
    else:
      retorno += str(lista_sequencia[0])+', '
    
    lista_sequencia = []
  
  print(f'\nLista: {lista}', end='')
  print(f' Retorno: {retorno[:-2]}')

  return retorno[:-2]


def test_intervalo():
  assert intervalo([1,2,3,5,6]) == "[1 - 3], 5, 6"
  assert intervalo([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5,7]) == "[-10 - -8], -6, [-3 - 1], [3 - 5], 7"
  assert intervalo([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 32, 33, 34]) == '[-10 - -8], -6, [-3 - 1], [3 - 5], 7, 8, [32 - 34]'

if __name__ == "__main__":
  pytest.main(['-svv', __file__])
