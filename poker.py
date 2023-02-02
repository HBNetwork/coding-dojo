import pytest
from random import sample, shuffle
'''
DATA: 04/01/2023
DATA: 11/01/2023
DATA: 18/01/2023
DATA: 25/01/2023
DATA: 01/02/2023


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
- Greg
- Cassio
- Luiz Carlos
- Everton Matos
- Álisson



Combinados definidos:
- Não vamos considerar os naipes neste primeiro momento
- Valete(J) - 11 Dama(Q) - 12 Rei - 13 - Ás - 14.
-  Jogo com 2 jogadores
- 
'''


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


def quantitatiza_cartas(cartas):  # pares, trinca e quadra
    cartas_q = {}
    cartas.sort()
    for i in range(0, 5):
        qt = cartas.count(cartas[i])
        cartas_q[cartas[i]] = qt

    return cartas_q


# REGRAS DO POKER
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


def dois_pares(cartas):
    qt = quantitatiza_cartas(cartas)
    temp = [False, list()]
    for k, v in qt.items():
        if v == 2:
            temp[1].append(k)
    temp[0] = len(temp[1]) == 2

    return temp


def trinca(cartas):
    qt = quantitatiza_cartas(cartas)
    temp = [False, list()]
    for k, v in qt.items():
        if v == 3:
            temp[0] = True
            temp[1].append(k)
    return temp


def straight(cartas):
    cartas.sort()
    return [verifica_sequencial(cartas), cartas]


def flush(cartas):
    qt = quantitatiza_cartas(cartas)
    temp = [False, list()]
    for k, v in qt.items():
        if v == 1:
            temp[1].append(k)
    temp[0] = len(temp[1]) == 5
    temp[1] = [] if len(temp[1]) != 5 else temp[1]

    return temp


def full_house(cartas):
    par_ = par(cartas)
    trinca_ = trinca(cartas)
    if par_[0] and trinca_[0]:
        par_[1].extend(trinca_[1])
        return [True, par_[1]]
    return [False, []]


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
    return [verifica_sequencial(cartas), cartas]


def royal_flush(cartas):
    cartas.sort()
    return [True, cartas] if verifica_sequencial(cartas) and cartas[0] == 10 else [False, cartas]


# JOGO
def categoriza_mao(cartas):
    # estrutura_jogo = [Royal Flush, Straight Flush, Quadra, Full House, Flush, Straight, Trinca, Dois Pares, Par, Carta Alta]
    pass


def poker(mao1, mao2):
    for i in range(10):
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
    nomes_jogadas = {0: 'Royal Flush', 1: 'Straight', 2: 'Flush', 3: 'Quadra', 4: 'Full House', 5: 'Flush', 6: 'Straight', 7: 'Trinca', 8: 'Dois Pares', 9: 'Par', 10: 'Carta Alta'}
    return [vencedor, nomes_jogadas[i]]


def distribuir_cartas():
    baralho = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12,
        13, 13, 13, 13, 14, 14, 14, 14
    ]
    shuffle(baralho)
    print("\nBARALHO EMBARALHADO")
    print(baralho)
    mesa = baralho[0:5]
    print("\nMESA")
    print(mesa)
    baralho = baralho[5:]

    mao_jogador_1 = baralho[0:2]  #2 cartas
    baralho.remove(mao_jogador_1[0])
    baralho.remove(mao_jogador_1[1])
    print("\nJogador 1 ")
    print(mao_jogador_1)
    mao_jogador_2 = baralho[0:2]  #2 cartas
    baralho.remove(mao_jogador_2[0])
    baralho.remove(mao_jogador_2[1])
    print("\nJogador 2 ")
    print(mao_jogador_2)

    print("\nPILHA DO BARALHO")
    print(baralho)
    print("\nJogador 1 Final")
    mao_jogador_1.extend(mesa)
    print(mao_jogador_1)
    print("\nJogador 2 Final")
    mao_jogador_2.extend(mesa)
    print(mao_jogador_2)

    return mao_jogador_1, mao_jogador_2


def jogar():
    '''
    Gerar a lista dos True e False, invocando as funções desenvolvidas para análise da carta.
    E repassar para a função poker() a mão de cada jogador e informar o vencedor.    
    Possivelmente criar uma funçãr dar as cartas (retornar o baralho)
    
    '''

    jogador1, jogador2 = distribuir_cartas()

    lista_de_jogadas = [
        royal_flush, straight_flush, quadra, full_house, flush, straight,
        trinca, dois_pares, par, carta_alta
    ]

    lista_de_resultados_jogador_1 = list()
    lista_de_resultados_jogador_2 = list()

    for jogada in lista_de_jogadas:
        resultado_1, _ = jogada(jogador1)
        lista_de_resultados_jogador_1.append(resultado_1)
        resultado_2, _ = jogada(jogador2)
        lista_de_resultados_jogador_2.append(resultado_2)

    print('\n')
    print(lista_de_resultados_jogador_1)
    print(lista_de_resultados_jogador_2)
    print('\n')

    resultado = poker(lista_de_resultados_jogador_1, lista_de_resultados_jogador_2)
    print(resultado)


def test_verifica_sequencial():
    assert verifica_sequencial([6, 3, 4, 5, 2]) == True
    assert verifica_sequencial([2, 3, 4, 5, 6]) == True
    assert verifica_sequencial([8, 9, 10, 11, 12]) == True
    assert verifica_sequencial([8, 9, 10, 11, 14]) == False


def test_quantitatiza_cartas():
    assert quantitatiza_cartas([5, 5, 6, 7, 13]) == {5: 2, 6: 1, 7: 1, 13: 1}
    assert quantitatiza_cartas([5, 5, 5, 7, 13]) == {5: 3, 7: 1, 13: 1}
    assert quantitatiza_cartas([2, 5, 2, 7, 5]) == {5: 2, 2: 2, 7: 1}


def test_carta_alta():
    # Carta Alta
    assert carta_alta([3, 4, 5, 6, 13]) == [True, 13]
    assert carta_alta([2, 3, 4, 5, 10]) == [True, 10]
    assert carta_alta([8, 9, 15, 11, 12]) == [True, 15]


def test_par():
    assert par([5, 5, 6, 7, 13]) == [True, [5]]
    assert par([6, 6, 2, 2, 13]) == [True, [2, 6]]
    assert par([5, 5, 6, 6, 13]) == [True, [5, 6]]
    assert par([5, 2, 5, 3, 10]) == [True, [5]]
    assert par([4, 6, 8, 9, 11]) == [False, []]
    assert par([6, 6, 6, 2, 13]) == [False, []]


def test_dois_pares():
    assert dois_pares([5, 5, 3, 2, 2]) == [True, [2, 5]]
    assert dois_pares([7, 6, 3, 2, 2]) == [False, [2]]
    assert dois_pares([7, 6, 3, 8, 2]) == [False, []]


def test_trinca():
    assert trinca([5, 5, 6, 7, 13]) == [False, []]
    assert trinca([6, 6, 6, 2, 13]) == [True, [6]]
    assert trinca([5, 5, 4, 5, 13]) == [True, [5]]
    assert trinca([3, 2, 3, 3, 10]) == [True, [3]]
    assert trinca([4, 6, 8, 9, 11]) == [False, []]


def test_straight():
    cartas_1 = sample(range(2, 7), 5)
    cartas_1.sort()
    assert straight(cartas_1) == [True, cartas_1]
    cartas_2 = sample(range(2, 15), 5)
    cartas_2.sort()
    assert straight(cartas_2) == [False, cartas_2]


def test_flush():
    assert flush([6, 3, 4, 5, 11]) == [True, [3, 4, 5, 6, 11]]
    assert flush([6, 3, 4, 5, 3]) == [False, []]


def test_full_house():
    assert full_house([3, 3, 3, 2, 2]) == [True, [2, 3]]


def test_quadra():
    assert quadra([5, 5, 5, 5, 13]) == [True, [5]]
    assert quadra([6, 2, 2, 2, 2]) == [True, [2]]
    assert quadra([5, 5, 5, 6, 13]) == [False, []]
    assert quadra([5, 2, 5, 3, 10]) == [False, []]
    assert quadra([4, 6, 8, 9, 11]) == [False, []]


def test_straight_flush():
    cartas_1 = sample(range(2, 7), 5)
    cartas_1.sort()
    assert straight_flush(cartas_1) == [True, cartas_1]
    cartas_2 = sample(range(2, 15), 5)
    cartas_2.sort()
    assert straight_flush(cartas_2) == [False, cartas_2]


def test_royal_flush():
    cartas_1 = sample(range(10, 15), 5)
    cartas_1.sort()
    assert royal_flush(cartas_1) == [True, cartas_1]
    cartas_2 = sample(range(2, 15), 5)
    cartas_2.sort()
    assert royal_flush(cartas_2) == [False, cartas_2]


def test_poker():
    assert poker([False, True, True, False, False],
                 [True, False, False, False, False]) == ['Jogador 2', 'Royal Flush']
    assert poker([True, True, True, False, False],
                 [True, False, False, False, False]) == ['Empate', 'Royal Flush']
    assert poker([False, True, True, False, False],
                 [False, False, False, False, False]) == ['Jogador 1', 'Straight']


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
    jogar()
