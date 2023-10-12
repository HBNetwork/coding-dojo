'''
DATA: 13/09/2023

FONTE: https://www.codewars.com/kata/62c93765cef6f10030dfa92b

ENUNCIADO: 
Um número infinito de prateleiras estão dispostas umas sobre as outras de forma escalonada.
O gato pode pular uma ou três prateleiras por vez: da prateleira i para a prateleira i+1 ou i+3 (o gato não pode subir na prateleira diretamente acima de sua cabeça), conforme ilustração:

                 ┌────────┐
                 │-6------│
                 └────────┘
┌────────┐       
│------5-│        
└────────┘  ┌─────► OK!
            │    ┌────────┐
            │    │-4------│
            │    └────────┘
┌────────┐  │
│------3-│  │     
BANG!────┘  ├─────► OK! 
  ▲  /|_/|  │    ┌────────┐
  │ ("^-^)  │    │-2------│
  │ )   (   │    └────────┘
┌─┴─┴───┴┬──┘
│------1-│
└────────┘


Entrada
Números de prateleira inicial e final (sempre números inteiros positivos, final não menor que o inicial)

Tarefa
Encontre o número mínimo de saltos para ir do início ao fim

Exemplo
Comece 1, termine 5 e a resposta é 2 (1 => 4 => 5 ou 1 => 2 => 5)


Participantes:
- GregMaster
- Frederico
- AVC
- Monstro do Codigo Onrado
- Lucas
- Everton
- Luis Lins
'''

import pytest


def pulo_do_gato(inicio, fim):
  pulos = []
  prateleira_atual = inicio

  while prateleira_atual != fim:
    maior_pulo_possivel = prateleira_atual + 3
    if maior_pulo_possivel <= fim:
      prateleira_atual = maior_pulo_possivel
    else:
      prateleira_atual += 1

    pulos.append(prateleira_atual)

  print(pulos)
  return len(pulos)


def test_pulo_do_gato():
  assert pulo_do_gato(1, 5) == 2
  assert pulo_do_gato(2, 5) == 1
  assert pulo_do_gato(3, 5) == 2
  assert pulo_do_gato(1, 10) == 3
  assert pulo_do_gato(2, 10) == 4


if __name__ == "__main__":
  pytest.main(['-svv', __file__])
