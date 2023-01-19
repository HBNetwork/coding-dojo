import pytest
from random import sample
'''
DATA: 04/01/2023
DATA: 11/01/2023
DATA: 18/01/2023

DESAFIO: Poker
FONTE: https://dojopuzzles.com/problems/poker/

Este problema foi utilizado em 245 Dojo(s).

No jogo de Poker, uma mão consiste em cinco cartas que podem ser comparadas, da mais baixa para a mais alta, da seguinte maneira:

Carta Alta: A carta de maior valor.
Um Par: Duas cartas do mesmo vlor.
Dois Pares: Dois pares diferentes.
Trinca: Três cartas do mesmo valor e duas de valores diferentes.
Straight (seqüência): Todas as carta com valores consecutivos.
Flush: Todas as cartas do mesmo naipe.
Full House: Uma trinca e um par.
Quadra: Quatro cartas do mesmo valor.
Straight Flush: Todas as cartas são consecutivas e do mesmo naipe.
Royal Flush: A seqüência 10, Valete, Dama, Rei, Ás, do mesmo naipe.
As cartas são, em ordem crescente de valor: 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete(J), Dama(Q), Rei(K), Ás(A).
Os naipes são: Ouro (D), Copa (H), Espadas (S), Paus (C)
Se dois jogadores possuem a mesma mão, vence que tiver a mão formada pelas cartas de maior valor.


Alguns exemplos de mão e seus respectivos vencedores:
 	Jogador 1	 	Jogador 2	 	        Vencedor
 	5H 5C 6S 7S KD | 2C 3S 8S 8D JD          Jogador 2
Par de cinco       | Par de oito
 	
 	5D 8C 9S JS AC  | 2C 5C 7D 8S QH          Jogador 1
Carta mais alta: Ás | Carta mais alta: Dama
 	
 	2D 9C AS AH AC  | 3D 6D 7D TD QD          Jogador 2
Trinca de Ás        | Flush com Ouro    

 	4D 6S 9H QH QC  | 3D 6D 7H QD QS         Jogador 1
Par de Damas        | Par de Damas 
Carta mais alta: 9  | Carta mais alta: 7 
 	
 	2H 2D 4C 4D 4S  | 3C 3D 3S 9S 9D         Jogador 1
Full House          | Full House
Com três 4          | Com três 3

Desenvolva um programa que, de acordo com as mãos de dois jogadores, informe qual deles é o vencedor.


Participantes
- Conrado
- Álisson
- Greg
- Carlos Xavier
- Cassio
- joão moreno

Combinados definidos:
- Não vamos considerar os naipes neste primeiro momento
- Valete(J) - 11 Dama(Q) - 12 Rei - 13 - Ás - 14.
-  Jogo com 2 jogadores
- 
'''
baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Funções de apoio
def verifica_sequencial(mao):

    mao.sort()
    sequencial = False
    for i in range(0, 5):
        if i == 4:
            break
        if mao[i + 1] - mao[i] == 1:
            sequencial = True
            continue
        else:
            sequencial = False
            break
    return sequencial


def quantitatiza_cartas(cartas):  #pares, trinca e quadra
    cartas_q = {}
    cartas.sort()
    for i in range(0, 5):
        qt = cartas.count(cartas[i])
        cartas_q[cartas[i]] = qt

    return cartas_q



#REGRAS DO POKER
def carta_alta(cartas):
    return [True, max(cartas)]


def par(cartas):

    qt = quantitatiza_cartas(cartas)
    temp = [False, list()]
    for k, v in qt.items():
        if v == 2:
            temp[0] = True
            temp[1].append(k)
    return temp



def trinca(cartas):

    qt = quantitatiza_cartas(cartas)
    temp = [False, list()]
    for k, v in qt.items():
        if v == 3:
            temp[0] = True
            temp[1].append(k)
    return temp



def quadra(cartas):

    qt = quantitatiza_cartas(cartas)
    temp = [False, list()]
    for k, v in qt.items():
        if v == 4:
            temp[0] = True
            temp[1].append(k)
    return temp



def straight_flush(cartas):
    cartas.sort()
    return verifica_sequencial(cartas)


def royal_flush(cartas):
    cartas.sort()
    return True if verifica_sequencial(cartas) and cartas[0] == 10 else False


# JOGO
def categoriza_mao(cartas):
    # estrutura_jogo = [Royal Flush, Straight Flush, Quadra, Full House, Flush, Straight, Trinca, Pares, Carta Alta]
    pass


def poker(mao1, mao2):

    for i in range(5):
        if not mao1[i] and not mao2[i]:
            continue
        if mao1[i] and mao2[i]:
            vencedor = 'Empate'
            break
        if mao1[i]:
            vencedor = 'Jogador 1'
            break
        if mao2[i]:
            vencedor = 'Jogador 2'
            break

    return [vencedor, i]


def test_carta_alta():
    # Carta Alta
    assert carta_alta([3, 4, 5, 6, 13]) == [True, 13]
    assert carta_alta([2, 3, 4, 5, 10]) == [True, 10]
    assert carta_alta([8, 9, 15, 11, 12]) == [True, 15]


def test_royal_flush():
    assert royal_flush(sample(range(10, 15), 5)) == True
    assert royal_flush(sample(range(2, 15), 5)) == False


def test_straight_flush():
    assert straight_flush(sample(range(2, 7), 5)) == True
    assert straight_flush(sample(range(2, 15), 5)) == False


def test_verifica_sequencial():
    assert verifica_sequencial([6, 3, 4, 5, 2]) == True
    assert verifica_sequencial([2, 3, 4, 5, 6]) == True
    assert verifica_sequencial([8, 9, 10, 11, 12]) == True
    assert verifica_sequencial([8, 9, 10, 11, 14]) == False


def test_quantitatiza_cartas():
    assert quantitatiza_cartas([5, 5, 6, 7, 13]) == {5: 2, 6: 1, 7: 1, 13: 1}
    assert quantitatiza_cartas([5, 5, 5, 7, 13]) == {5: 3, 7: 1, 13: 1}
    assert quantitatiza_cartas([2, 5, 2, 7, 5]) == {5: 2, 2: 2, 7: 1}


def test_par():
    assert par([5, 5, 6, 7, 13]) == [True, [5]]
    assert par([6, 6, 2, 2, 13]) == [True, [2, 6]]
    assert par([5, 5, 6, 6, 13]) == [True, [5, 6]]
    assert par([5, 2, 5, 3, 10]) == [True, [5]]
    assert par([4, 6, 8, 9, 11]) == [False, []]


def test_trinca():
    assert trinca([5, 5, 6, 7, 13]) == [False, []]
    assert trinca([6, 6, 6, 2, 13]) == [True, [6]]
    assert trinca([5, 5, 4, 5, 13]) == [True, [5]]
    assert trinca([3, 2, 3, 3, 10]) == [True, [3]]
    assert trinca([4, 6, 8, 9, 11]) == [False, []]


def test_quadra():
    assert quadra([5, 5, 5, 5, 13]) == [True, [5]]
    assert quadra([6, 2, 2, 2, 2]) == [True, [2]]
    assert quadra([5, 5, 5, 6, 13]) == [False, []]
    assert quadra([5, 2, 5, 3, 10]) == [False, []]
    assert quadra([4, 6, 8, 9, 11]) == [False, []]


def test_poker():
    assert poker([False, True, True, False, False],
                 [True, False, False, False, False]) == ['Jogador 2', 0]
    assert poker([True, True, True, False, False],
                 [True, False, False, False, False]) == ['Empate', 0]
    assert poker([False, True, True, False, False],
                 [False, False, False, False, False]) == ['Jogador 1', 1]


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
