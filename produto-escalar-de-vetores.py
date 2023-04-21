'''
Data: 19/04/2023
FONTE: https://dojopuzzles.com/problems/produto-escalar-de-vetores/
Enunciado: Produto Escalar de Vetores

Definimos dois vetores A e B de dimensão n em termos de componentes como:

A = (a1, a2, a3, ..., an) e B = (b1, b2, b3, ..., bn)

O produto escalar entre esses vetores é descrito como:

A . B = a1 * b1 + a2 * b2 + a3 * b3 + ... + an * bn

Desenvolva um programa que, dado dois vetores de dimensão n, retorne o produto escalar entre eles.

Participantes:
- Álisson
- joão moreno
- Conrado
- Frederico
- Greg
- Luiz 
- cassio

'''

import pytest

def produto_escalar_vetores(v1,v2):
  uniao = []
  
  if len(v1) > len(v2):
      diferenca = len(v1) - len(v2)
      v2.extend(diferenca*[1])
  elif len(v2) > len(v1):
      diferenca = len(v2) - len(v1)
      v1.extend(diferenca*[1])

  for n,v in enumerate(v1):
    
    uniao.append(v*v2[n])
   
  return  uniao

def test_produto_escalar_vetores():  
  assert produto_escalar_vetores([1],[2]) == [2]
  assert produto_escalar_vetores([15, 3, 23],[2, 2, 2]) == [30, 6, 46]
  assert produto_escalar_vetores([1, 2, 3],[2]) == [2, 2, 3]
  assert produto_escalar_vetores([1],[1,2,3]) == [1, 2, 3]    


if __name__ == "__main__":
    pytest.main(['-svv', __file__])

