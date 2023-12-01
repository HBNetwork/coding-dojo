'''
Fonte: https://exercism.org/tracks/python/exercises/dominoes
Problema: Domino
Enunciado:
Faça uma cadeia de dominós.

Calcule uma maneira de ordenar um determinado conjunto de dominós de tal forma que eles formem uma cadeia de dominós correta (os pontos na metade de uma pedra correspondem aos pontos na metade vizinha de uma pedra adjacente) e que os pontos nas metades da pedra adjacente pedras que não têm vizinha (a primeira e a última pedra) combinam entre si.

Por exemplo, dadas as pedras [2|1], [2|3] e [1|3] deve calcular algo como
[1|2] [2|3] [3|1] ou
[3|2] [2|1] [1|3] ou
[1|3] [3|2] [2|1] etc,
onde o primeiro e o último números são iguais.

Para pedras [1|2], [4|1] e [2|3] a cadeia resultante não é válida: [4|1] [1|2] [2|3] o primeiro e o último número de não são iguais 4! = 3

Alguns casos de teste podem usar pedras duplicadas em uma solução em cadeia, assumindo que vários conjuntos de Domino estão sendo usados.

Participantes:
- Adailton
- João Moreno
- Greg
- McOnrado
- Lucas
- Fred
'''

import pytest

def domino(pedras):
    i = 0
    respostas_validas = []

    while i < len(pedras):
        j = 0
        while j <= 2**len(pedras):

            pedra_inicial = pedras[0]
            pedras_restantes = pedras[1:]

            if pedra_inicial[0] > pedra_inicial[1]:
                pedra_inicial = pedra_inicial[::-1]

            ponta_esquerda = pedra_inicial[0]  #2
            ponta_direita = pedra_inicial[1]  #1

            resposta = []
            resposta.append(pedra_inicial)

            for pedra_atual in pedras_restantes:
                if pedra_atual[0] == ponta_esquerda:
                    ponta_esquerda = pedra_atual[1]
                    resposta.insert(0, pedra_atual[::-1])
                elif pedra_atual[0] == ponta_direita:
                    ponta_direita = pedra_atual[1]
                    resposta.append(pedra_atual)
                elif pedra_atual[1] == ponta_esquerda:
                    ponta_esquerda = pedra_atual[0]
                    resposta.insert(0, pedra_atual)
                elif pedra_atual[1] == ponta_direita:
                    ponta_direita = pedra_atual[0]
                    resposta.append(pedra_atual[::-1])

            if ponta_esquerda == ponta_direita and resposta not in respostas_validas:
                respostas_validas.append(resposta)

            print(f'\n{pedras}')
            j += 1
            pedras = inverte_pedras(pedras)

        pedras = permuta(pedras)
        i += 1

    print(f'\n{respostas_validas}')
    return respostas_validas


def permuta(pedras):
    pedra_inicial = pedras[0]
    retorno = pedras[1:]
    retorno.append(pedra_inicial)
    return retorno


def inverte_pedras(pedras):



def test_domino():
    assert domino([[2, 1], [2, 3], [1, 3]]) == [[[3, 1], [1, 2], [2, 3]], [[1, 2], [2, 3], [3, 1]], [[3, 2], [2, 1], [1, 3]]]
    
    #[[[1, 2], [2, 3], [3, 1]],[[3, 2], [2, 1], [1, 3]],[[3, 1], [1, 2], [2, 3]]]
    #assert domino([[2, 3], [1, 3], [2, 1]]) == [[1, 2], [2, 3], [3, 1]]
    #assert domino([[1, 2], [4, 1], [2, 3]]) == [[4, 1], [1, 2], [2, 3]]
    #assert domino([[1, 2], [4, 1], [2, 3], [4, 3]]) == [[[1, 2], [2, 3], [3, 4], [4, 1]], [[3, 4], [4, 1], [1, 2], [2, 3]]]
    #assert domino([[4,1], [2,3], [4,3], [1,2]]) == [[3,2], [2,1], [1,4], [4,3]]
    #assert domino([[2,3], [4,3], [1,2], [4,1]]) == [[3,2], [2,1], [1,4], [4,3]]
    #assert domino([[4,3], [1,2], [4,1], [2,3]]) == [[3,2], [2,1], [1,4], [4,3]]


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
