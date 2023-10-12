'''
DATA: 28/06/2023 / 05/07/2023

FONTE: https://exercism.org/tracks/python/exercises/dnd-character

ENUNCIADO: D&D Character

Instruções
Para um jogo de Dungeons and Dragons, cada jogador começa gerando um personagem com o qual pode jogar um jogo importantisimo. Esse personagem tem, entre outras coisas, seis habilidades; força, destreza, constituição, inteligência, sabedoria e carisma. Essas seis habilidades têm pontuações determinadas aleatoriamente. Você faz isso rolando quatro dados de 6 lados e registra a soma dos três maiores dados. Você faz isso seis vezes, uma vez para cada habilidade.

Os pontos de acesso iniciais do seu personagem são 10 + modificador de constituição do seu personagem. Você encontra o modificador de constituição do seu personagem subtraindo 10 da constituição do seu personagem, divida por 2 e arredondar para baixo.

Escreva um gerador de caracteres aleatórios que siga as regras acima.

Por exemplo, os seis arremessos de quatro dados podem parecer:

5, 3, 1, 6: Você descarta o 1 e a soma 5 + 3 + 6 = 14, que você atribui à força.
3, 2, 5, 3: Você descarta o 2 e a soma 3 + 5 + 3 = 11, que atribui à destreza.
1, 1, 1, 1: Você descarta o 1 e a soma 1 + 1 + 1 = 3, que você atribui à constituição.
2, 1, 6, 6: Você descarta o 1 e a soma 2 + 6 + 6 = 14, que você atribui à inteligência.
3, 5, 3, 4: Você descarta os 3 e a soma 5 + 3 + 4 = 12, que você atribui à sabedoria.
6, 6, 6, 6: Você descarta os 6 e a soma 6 + 6 + 6 = 18, que atribui ao carisma.
Como a constituição é 3, o modificador da constituição é -4 e os pontos de acesso são 6.


PARTICIPANTES:
- João
- Diogo 
- Greg
- MCOnrado
- Fred
- Ton
- Leo
- 


'''

import pytest
import random
import math

numero_dados = [1, 2, 3, 4, 5, 6]


def gerar_dados():
    return random.choices(numero_dados, k=4)


def conta_dado(dados):
    quantidade = len(random.choices(numero_dados, k=4))

    return quantidade - 1


def soma_dado(dados):
    soma = 0

    for dado in dados:
        soma += dado
    return soma


def elimina_menor(dados):
    dados.remove(min(dados))
    return dados


def modificador(dados):
    dados_aux = dados.copy()
    soma = soma_dado(dados_aux)
    valor_modificador = (soma - 10) / 2
    return math.floor(valor_modificador)


def pontos_de_acesso(modificador_):
    return modificador_ + 10


def test_dados():
    assert conta_dado([1, 2, 3, 4]) == 3

    assert soma_dado([1, 2, 3, 4]) == 10
    assert soma_dado([1, 2, 1, 3]) == 7

    assert elimina_menor([1, 2, 3, 4]) == [2, 3, 4]
    assert elimina_menor([1, 2, 1, 3]) == [2, 1, 3]

    assert modificador([1, 2, 3, 4]) == -1

    assert pontos_de_acesso(-4) == 6


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
