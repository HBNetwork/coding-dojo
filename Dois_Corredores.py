"""
Data: 09/08/2023
FONTE: codewars.com
Enunciado: 


Dois Corredores

Evertinho e Leo estão se encontrando para sua corrida semanal. Ambos começam no mesmo local chamado "Start" e cada um corre uma volta diferente, que pode (ou não) variar de comprimento. Já que eles se conhecem há muito tempo, ambos correm na mesma velocidade.

Seu trabalho é completar a função nbrOfLaps(x, y) que, dado o comprimento das voltas de Evertinho e Leo, encontre o número de voltas que cada corredor tem que completar antes de se encontrarem novamente no ponto de partida.

A função recebe dois argumentos:

 O comprimento da volta de Evertinho (maior que 0)
 O comprimento da volta de Leo (maior que 0)

A função deve retornar uma tupla contendo exatamente dois números:

 O primeiro número é o número de voltas que Evertinho tem que correr
 O segundo número é o número de voltas que Leo tem que correr
 Até se encontrarem novamente.

Participantes:
- João Moreno      
- MConrado
- Greg
- Lucas
- Everton



"""
#
import pytest
import math
import time
"""def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True  """

lista_primos = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97
]


def numero_de_voltas(distancia_1, distancia_2):
    dividendo_1, dividendo_2 = distancia_1, distancia_2
    mmc = []
    while True:
        for primo in lista_primos:
            div_1, resto_1 = divmod(dividendo_1, primo)
            div_2, resto_2 = divmod(dividendo_2, primo)
            if resto_1 == 0 or resto_2 == 0:
                mmc.append(primo)
                if resto_1 == 0:
                    dividendo_1 = div_1
                if resto_2 == 0:
                    dividendo_2 = div_2
                break
        if dividendo_1 == 1 and dividendo_2 == 1:
            break
    mmc_produto = math.prod(mmc)
    return (int(mmc_produto / distancia_1), int(mmc_produto / distancia_2))


def numero_de_voltas_versao_2(dist1, dist2):
    if dist1 > dist2:
        maior = dist1
    else:
        maior = dist2

    while True:
        if maior % dist1 == 0 and maior % dist2 == 0:
            mmc = maior
            break
        else:
            maior += 1

    volta1 = int(mmc / dist1)
    volta2 = int(mmc / dist2)

    return (volta1, volta2)


def test_corrida():
    assert numero_de_voltas(100, 50) == (1, 2)
    assert numero_de_voltas(100, 25) == (1, 4)
    assert numero_de_voltas(50, 100) == (2, 1)
    assert numero_de_voltas(350, 100) == (2, 7)

    assert numero_de_voltas_versao_2(100, 50) == (1, 2)
    assert numero_de_voltas_versao_2(100, 25) == (1, 4)
    assert numero_de_voltas_versao_2(50, 100) == (2, 1)
    assert numero_de_voltas_versao_2(350, 100) == (2, 7)


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
