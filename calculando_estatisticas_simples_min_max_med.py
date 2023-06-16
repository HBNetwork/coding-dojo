'''
Data: 10/05/2023
Fonte: https://dojopuzzles.com/problems/calculando-estatisticas-simples/
Enunciado: Sua tarefa é processar uma seqüência de números inteiros para determinar as seguintes estatísticas:

Valor mínimo
Valor máximo
Número de elementos na seqüência
Valor médio
Por exemplo para uma seqüência de números "6, 9, 15, -2, 92, 11", temos como saída:

Valor mínimo: -2
Valor máximo: 92
Número de elementos na seqüência: 6
Valor médio: 21.833333333333332

Traduzido de: http://www.cyber-dojo.com/

Participantes:
- Márcio Conrado
- João Moreno
- Everton     
- Greg
- Fred
- Cassio
- David Silveira
- Luiz Carlos

'''

import pytest


def estatistica_basica(sequencia):
    mini = sequencia[0]
    maxi = sequencia[0]
    qtde = 0
    soma = 0
    for num in sequencia:
        if num < mini:
            mini = num
        if num > maxi:
            maxi = num
        qtde += 1
        soma += num
    media = soma / qtde
        
    return [mini, maxi, qtde, media]


def minimo(sequencia):
    minimo = sequencia[0]
    for num in sequencia:
        if num < minimo:
            minimo = num

    return minimo


def maximo(sequencia):
    maximo = sequencia[0]
    for num in sequencia:
        if num > maximo:
            maximo = num

    return maximo


def quantidade_sequencia(sequencia):
    quantidade = 0
    for num in sequencia:
        quantidade += 1
    return quantidade


def valor_medio(sequencia):
    qtde = quantidade_sequencia(sequencia)
    soma = 0

    for num in sequencia:
        soma += num

    return soma / qtde


def estatistica(sequencia):
    return [
        minimo(sequencia),
        maximo(sequencia),
        quantidade_sequencia(sequencia),
        valor_medio(sequencia)
    ]


#########################################


def test_minimo():
    assert minimo([3, 4, 6]) == 3
    assert minimo([-5, 10, 21, -10]) == -10


def test_maximo():
    assert maximo([3, 4, 6]) == 6
    assert maximo([-5, 10, 21, -10]) == 21


def test_quantidade_elementos():
    assert quantidade_sequencia([1, 2]) == 2
    assert quantidade_sequencia([-5, 10, 21, -10]) == 4


def test_media():
    assert valor_medio([1, 2]) == 1.5
    assert valor_medio([6, 9, 15, -2, 92, 11]) == 21.833333333333332


def test_estatistica():
    assert estatistica([1, 2]) == [1, 2, 2, 1.5]
    assert estatistica([6, 9, 15, -2, 92, 11]) == [-2, 92, 6, 21.833333333333332]


def test_estatistica_basica():
    assert estatistica_basica([6, 9, 15, -2, 92, 11]) == [-2, 92, 6, 21.833333333333332]


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
