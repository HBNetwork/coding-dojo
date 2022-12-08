import pytest
from random import randint
'''
Data:  21/09/2022

Jokenpo


Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:

Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra

https://dojopuzzles.com/problems/jokenpo/

'''

# Ordem
'''
1 - Greg
2 - David
3 - Diogo Bueno
4 - Glau
5 - Marcelo
6 - Kelver
7 - Alisson
8 - Marcio
9 - Luiz Carlos
'''

# Pedra - 1
# Papel - 2
# Tesoura - 3


def jokenpo(j1, j2):
    if j2 == 2 and j1 == 1 or j1 == 2 and j2 == 1:
        return "Papel"
    elif j2 == 3 and j1 == 1 or j1 == 3 and j2 == 1:
        return 'Pedra'
    elif j2 == 2 and j1 == 3 or j1 == 2 and j2 == 3:
        return 'Tesoura'
    else:
        return 'Empate'


def test_Duelos():
    assert jokenpo(1, 2) == "Papel"
    assert jokenpo(2, 1) == "Papel"
    assert jokenpo(1, 3) == "Pedra"
    assert jokenpo(3, 1) == "Pedra"
    assert jokenpo(3, 2) == "Tesoura"
    assert jokenpo(2, 3) == "Tesoura"


def test_Empates():
    assert jokenpo(1, 1) == 'Empate'
    assert jokenpo(2, 2) == "Empate"
    assert jokenpo(3, 3) == "Empate"


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
    j1 = randint(1, 3)
    j2 = randint(1, 3)

    jogadas = ['Pedra', 'Papel', 'Tesoura']

    print(
        f'O jogador 1  escolheu {jogadas[j1 -1]} e o jogador 2 escolheu {jogadas[j2 -1]}. O resultado foi o {jokenpo(j1,j2)}.'
    )
