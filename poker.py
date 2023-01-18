import pytest
from random import sample
'''
DATA: 04/01/2023
DATA: 11/01/2023

DESAFIO: Poker
FONTE: https://dojopuzzles.com/problems/poker/

Este problema foi utilizado em 245 Dojo(s).

No jogo de Poker, uma mão consiste em cinco cartas que podem ser comparadas, da mais baixa para a mais alta, da seguinte maneira:

Carta Alta: A carta de maior valor.
Um Par: Duas cartas do mesmo valor.
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
- 
'''
baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def carta_alta(carta_j1, carta_j2):
    if max(carta_j1) > max(carta_j2):
        return carta_j1
    return carta_j2


def quantitatiza_cartas(cartas):
    cartas_q = {}

    for i in range(0, 5):
        qt = cartas.count(cartas[i])
        cartas_q[cartas[i]] = qt
    
    return cartas_q

def categoriza_mao(carta_j1, carta_j2):
    quantidade_j1 = {}
    quantidade_j2 = {}

    # estrutura_jogo = [Royal Flush, Straight Flush, Quadra, Full House, Flush, Straight, Trinca, Pares, Carta Alta]
    mao1 = [False, True, True, False, False]
    mao2 = [True, False, False, False, False]


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

def straight_flush(cartas):
    cartas.sort()

    return verifica_sequencial(cartas)

      
def royal_flush(cartas):
    cartas.sort()
    
    return True if cartas == [10, 11, 12, 13, 14] else False

    
def test_carta_alta():
    # Carta Alta
    assert carta_alta([3, 4, 5, 6, 13], [2, 8, 9, 3, 11]) == [3, 4, 5, 6, 13]
    assert carta_alta([2, 3, 4, 5, 10],
                      [8, 9, 10, 11, 12]) == [8, 9, 10, 11, 12]

"""
REVER
def test_categoriza_mao():
    assert categoriza_mao([5, 5, 6, 7, 13],
                          [2, 3, 8, 8, 11]) == [2, 3, 8, 8, 11]
    assert categoriza_mao([2, 7, 7, 8, 11],
                          [5, 6, 6, 9, 13]) == [2, 7, 7, 8, 11]
    assert categoriza_mao([2, 2, 2, 2, 11],
    [4, 5, 6, 6, 13]) == [2, 2, 2, 2, 11]
"""

def test_royal_flush():
    assert royal_flush(sample(range(10, 15), 5)) == True
    assert royal_flush(sample(range(2, 15), 5)) == False 

def test_straight_flush():
    assert straight_flush(sample(range(2, 7), 5)) == True
    assert royal_flush(sample(range(2, 15), 5)) == False 

def test_verifica_sequencial():
    assert verifica_sequencial([6, 3,  4, 5, 2]) == True
    assert verifica_sequencial([2, 3,  4, 5, 6]) == True
    assert verifica_sequencial([8, 9, 10, 11, 12]) == True
    assert verifica_sequencial([8, 9, 10, 11, 14]) == False

def test_quantitatiza_cartas():
    assert quantitatiza_cartas([5,5,6,7,13]) == {5:2, 6:1, 7:1, 13:1}
    assert quantitatiza_cartas([5,5,5,7,13]) == {5:3, 7:1, 13:1}
    assert quantitatiza_cartas([2,5,2,7,5]) == {5:2, 2:2, 7:1}

if __name__ == "__main__":
    pytest.main(['-svv', __file__])
