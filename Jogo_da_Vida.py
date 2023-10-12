"""
14/06/2023 - XX/06/2023

Fonte: https://dojopuzzles.com/problems/jogo-da-vida/
Problema: Jogo da Vida

Enunciado:
Desenvolva um algoritmo que execute 'um passo' do Jogo da Vida. As regras são bem simples:

* Qualquer célula viva com menos que duas células vivas vizinhas morre, por baixa população;
* Qualquer célula viva com mais que três células vivas vizinhas morre, por alta população;
* Qualquer célula viva com duas ou três células vivas vizinhas permanece viva para a próxima geração;
* Qualquer célula morta com exatamente três células vivas vizinhas se transforma em uma célula viva;

Você também terá que pensar em:
* Como representar a área do Jogo de uma maneira fácil de testar;
* Que 'valor' as células fora da área do Jogo terão. Ou o Jogo não terá limite de área?

https://pt.wikipedia.org/wiki/Jogo_da_vida

Participantes:
- Fred
- João moreno
- Greg
- Conrado
- Álisson
- Everton
- 

- Tabuleiro começa zerado.
- Pegar vizinha em diagonal.
- ver quantas opções ja vão começar no tabuleiro.

- http://cauequeiroz.com.br/game-of-life/  
- http://cauequeiroz.com.br/2017/jogo-da-vida/  

"""
import pytest
import numpy as np

matriz_1_geracao = [
    [0, 0, 1],
    [0, 1, 1],
    [0, 0, 0],
]


def gerar_matriz(n):
    return np.random.randint(0, 2, (n, n))


def printa_matriz(matriz):
    for linha in matriz:
        for item in linha:
            print(item, end=' ')
        print(end='\n')


def check_up_vivo():
    return ("abc")


def captura_adjacentes(matriz):
    for elemento in matriz:
        elemento = matriz[0][0]
        lista_elementos = []
        if elemento == 1:
            pass
            #testa os vizinhos
        else:
            pass

    elementos_vizinhos1 = matriz[0][1]
    elementos_vizinhos2 = matriz[1][0]
    elementos_vizinhos3 = matriz[1][1]
    return []


def test_vivo():
    assert check_up_vivo() == "abc"


def verificar_regras(estado_atual, vizinhos):
    # Conta quantos vizinhos estão vivos
    qnt_vizinhos_vivos = vizinhos.count(1)

    # Qualquer célula viva com menos que duas células vivas vizinhas morre, por baixa população;
    if estado_atual == 1 and qnt_vizinhos_vivos < 2:
        return 0

    # Qualquer célula viva com mais que três células vivas vizinhas morre, por alta população;
    if estado_atual == 1 and qnt_vizinhos_vivos > 3:
        return 0

    # Qualquer célula viva com duas ou três células vivas vizinhas permanece viva para a próxima geração;
    if estado_atual == 1 and (qnt_vizinhos_vivos == 2
                              or qnt_vizinhos_vivos == 3):
        return 1

    # Qualquer célula morta com exatamente três células vivas vizinhas se transforma em uma célula viva;
    if estado_atual == 0 and qnt_vizinhos_vivos == 3:
        return 1

    return 0


def test_regras():
    assert verificar_regras(1, [0, 1, 0, 1, 1, 0, 0, 1]) == 0
    assert verificar_regras(1, [0, 0, 0, 0, 1, 0, 0, 1]) == 1
    assert verificar_regras(0, [0, 0, 0, 0, 1]) == 0


if __name__ == "__main__":
    #printa_matriz(gerar_matriz(3))
    #print(gerar_matriz(3))
    #print(matriz_1_geracao)
    pytest.main(['-svv', __file__])
'''
for elemento in matriz:
    elemento = matriz[0][0]
    lista_elementos = []
    if elemento == 1:
        #testa os vizinhos
    else:
        pass

elementos_vizinhos1 = matrix[0][1]
elementos_vizinhos2 = matrix[1][0]
elementos_vizinhos3 = matrix[1][1]
'''
