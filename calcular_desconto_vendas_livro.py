"""
01/13/2023

Fonte: https://dojopuzzles.com/problems/livraria-do-harry-potter/

Desafio: 

Uma livraria contém 7 títulos distintos e possui um esquema de descontos que leva em consideração se é o mesmo título ou não. O problema consiste em calcular o melhor desconto para o cliente.

Preço de um título qualquer: R$ 42,00

Descontos:
        2 livros - 5%
        3 livros - 10%
        4 livros - 15%
        5 livros - 20%

Quanto custa?
        2 cópias do primeiro livro (A)
        2 cópias do segundo livro (B)
        2 cópias do terceiro livro (C)
        1 cópia do quarto livro (D)
        1 cópia do quinto livro (E)

Resposta: R$ 281,40
        Note que o preço deve ser o menor valor obtido combinando os livros.

"""
'''
Participantes
Greg
João Moreno
Cássio Augusto
Everton Matos
Vitor Pestana
Marcio Conrado
'''

import pytest


def calcula_desconto(*vendas):
    quantidade_livros = 0
    valor_livro = 42
    desconto = 0

    for quantidade, livro in vendas:
        quantidade_livros += quantidade

    if quantidade_livros == 2:
        desconto = 5
    elif quantidade_livros == 3:
        desconto = 10
    elif quantidade_livros == 4:
        desconto = 15
    elif quantidade_livros >= 5:
        desconto = 20

    valor_com_desconto = valor_livro * quantidade_livros * (100 - desconto) / 100

    return '{:.2f}'.format(valor_com_desconto)


def test_calcula_desconto():
    assert calcula_desconto((2, 'A'), (2, 'B'), (2, 'C'), (1, 'D'),
                            (1, 'E')) == "268.80"

    assert calcula_desconto((3, 'A'), (2, 'B'), (3, 'C'), (2, 'D'),
                            (1, 'E')) == "369.60"


def test_calcula_conjunto_unico():
    assert calcula_desconto((1, 'A')) == "42.00"
    assert calcula_desconto((1, 'A'), (1, 'B')) == "79.80"
    assert calcula_desconto((1, 'A'), (1, 'B'), (1, 'C')) == "113.40"
    assert calcula_desconto((1, 'A'), (1, 'B'), (1, 'C'), (1, 'D')) == "142.80"
    assert calcula_desconto((1, 'A'), (1, 'B'), (1, 'C'), (1, 'D'),
                            (1, 'E')) == "168.00"
    assert calcula_desconto((1, 'A'), (1, 'B'), (1, 'C'), (1, 'D'), (1, 'E'),
                            (1, 'F')) == "201.60"
    assert calcula_desconto((1, 'A'), (1, 'B'), (1, 'C'), (1, 'D'), (1, 'E'),
                            (1, 'F'), (1, 'G')) == "235.20"


if __name__ == "__main__":
    pytest.main(["-s", __file__])
