"""
DATA: 12/07/2023

FONTE:  https://dojopuzzles.com/problems/problema-do-miojo/

ENUNCIADO: Problema do Miojo

João é um fanático por miojos; ele os adora, e, como era de se esperar, ele levou vários pacotes quando foi acampar com seus colegas (Luiz e Everton (kkk)). Como João só gosta de miojos feitos com o tempo exato, ele se desesperou ao perceber que havia esquecido seu relógio em casa.

Por sorte, ele conseguiu, no caminho, comprar duas ampulhetas de durações diferentes. Por exemplo, se o miojo precisa de 3 minutos para ficar pronto, e João tiver uma ampulheta de 5 minutos e outra de 7, uma possível forma de cozinhar o miojo é:

João começa virando as duas ampulhetas ao mesmo tempo.
Quando a areia da ampulheta de 5 minutos se esgotar, João torna a virá-la.
João começa a preparar o miojo quando a areia da ampulheta de 7 minutos acabar.
João tira o miojo do fogo quando a ampulheta de 5 minutos acabar novamente.
Dessa forma, o miojo ficará 3 minutos no fogo (do minuto 7 ao minuto 10). Assim, apesar do miojo levar apenas três minutos para ser cozido, ele precisa de 10 minutos para ficar pronto.

Faça um programa que, dado o tempo de preparo do miojo, e os tempos das duas ampulhetas (ambos maiores que o tempo do miojo), determina o tempo mínimo necessário para o miojo ficar pronto ou se não é possível cozinhar o miojo no tempo exato com as ampulhetas disponíveis.

Participantes:
- Alisson
- Greg
- Conrado
- Fred
- Everton
- Luiz Carloz
"""

import pytest


def menor_tempo_ampulheta(ampulheta_1, ampulheta_2):
    return min(ampulheta_1, ampulheta_2)


def tempo_preparo(tempo_miojo=3, tempo_ampulheta_1=5, tempo_ampulheta_2=7):
    tempo_calibragem_preparo = 0
    c = 0

    while (c < 50):
        c += 1
        print(c)
        tempo_intermediario = abs(tempo_ampulheta_2 - tempo_ampulheta_1)
        tempo_calibragem_preparo += menor_tempo_ampulheta(
            tempo_ampulheta_1, tempo_ampulheta_2)

        tempo_ampulheta_2 = tempo_intermediario

        if tempo_intermediario == tempo_miojo:
            tempo_calibragem_preparo += tempo_intermediario
            return tempo_calibragem_preparo

    return "não é possível cozinhar o miojo no tempo exato com as ampulhetas disponíveis"


def test_tempo_preparo():
       assert tempo_preparo(3, 5, 7) == 10
       assert tempo_preparo(13, 15, 17) == 30
       assert tempo_preparo(2, 3, 5) == 5
  
   # assert tempo_preparo(5, 4, 9) == 9
  #  O teste acima não conta pois ambas as ampulhetas precisam ser maiores
   # que o tempo do miojo

if __name__ == "__main__":
    pytest.main(['-svv', __file__])
