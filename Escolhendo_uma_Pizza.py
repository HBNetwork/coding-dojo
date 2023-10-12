"""
DATA: 19/07/2023
FONTE: https://dojopuzzles.com/problems/escolhendo-uma-pizza/

ENUNCIADO: Escolhendo uma pizza

Em algumas empresas de desenvolvimento de software é comum, quando o prazo de entrega de uma aplicação está próximo, a equipe passar algumas noites trabalhando. E como todo desenvolvedor também precisa se alimentar, eles sempre pedem pizza nessas ocasiões. Só que sempre é uma briga para conseguir escolher os sabores das pizza de sabores que todos gostam.

Um dos membros da equipe, incomodado com as intermináveis discussões sobre o sabor a ser escolhido, resolveu desenvolver um programa para facilitar essa escolha.

Para cada sabor de pizza disponível, cada um deve indicar uma nota para ele (nota 1, se a pessoa detesta o sabor e nota 5 se a pessoa adora o sabor). Depois de processar esses dados, cada pessoa vai saber quais as pessoas que tem o gosto mais parecido que o seu (e que provavelmente irá dividir uma pizza com você).

Por exemplo, para os dados a seguir, o Everton gostaria de saber quem ele deve convidar para dividir uma pizza com ele:

Lucas = { Marguerita : 5, Quatro queijos : 3, Escarola : 1, Portuguesa : 2, Frango+Catupiry : 4, Napolitana : 4 }

Fred = { Marguerita : 2, Quatro queijos : 2, Escarola : 1, Portuguesa : 3, Frango+Catupiry : 5, Napolitana : 2 }

João = { Marguerita : 4, Quatro queijos : 5, Escarola : 2, Portuguesa : 1, Frango+Catupiry : 1, Napolitana : 3 }

Conrado = { Marguerita : 4, Quatro queijos : 5, Escarola : 1, Portuguesa : 1, Frango+Catupiry : 3, Napolitana : 4 }

Alisson = { Marguerita : 1, Quatro queijos : 1, Escarola : 2, Portuguesa : 3, Frango+Catupiry : 4, Napolitana : 3 }

Luiz Carlos = { Marguerita : 1, Quatro queijos : 5, Escarola : 1, Portuguesa : 4, Frango+Catupiry : 3, Napolitana : 2 }

Everton = { Marguerita : 5, Quatro queijos : 4, Escarola : 3, Portuguesa : 4, Frango+Catupiry : 3, Napolitana : 2 }

Participantes:
- EvertonIA
- João Moreno
- Frederico
- Greg
- Lucas
- M Conrado
- Luiz Carlos
- Álisson
- Thiago
"""
import pytest
"""cada um compra uma pizza
por Frederico Favaro"""

escolhas = {
'Lucas': {
        'Marguerita': 5,
        'Quatro queijos': 3,
        'Escarola': 1,
        'Portuguesa': 2,
        'Frango+Catupiry': 4,
        'Napolitana': 4
    },
'Fred': {
        'Marguerita': 2,
        'Quatro queijos': 2,
        'Escarola': 1,
        'Portuguesa': 3,
        'Frango+Catupiry': 5,
        'Napolitana': 2
    },
'Joao': {
        'Marguerita': 4,
        'Quatro queijos': 5,
        'Escarola': 2,
        'Portuguesa': 1,
        'Frango+Catupiry': 1,
        'Napolitana': 3
    },
'Conrado': {
        'Marguerita': 4,
        'Quatro queijos': 5,
        'Escarola': 1,
        'Portuguesa': 1,
        'Frango+Catupiry': 3,
        'Napolitana': 4
    },
'Alisson': {
        'Marguerita': 1,
        'Quatro queijos': 1,
        'Escarola': 2,
        'Portuguesa': 3,
        'Frango+Catupiry': 4,
        'Napolitana': 3
    },
'LuizCarlos': {
        'Marguerita': 1,
        'Quatro queijos': 5,
        'Escarola': 1,
        'Portuguesa': 4,
        'Frango+Catupiry': 3,
        'Napolitana': 2
    },
'Everton': {
        'Marguerita': 5,
        'Quatro queijos': 4,
        'Escarola': 3,
        'Portuguesa': 4,
        'Frango+Catupiry': 3,
        'Napolitana': 2
    }
}



def melhores_pizzas():
    ruim = (0, 1)
    mediano = (2, 3)
    boa = (4, 5)
    return True


def rank_pizza(sabor, nota):
    match = []
    for pessoas, sabores in escolhas.items():
        for pizza, nota_dada in sabores.items():
            if pizza == sabor and nota_dada == nota:
                match.append(pessoas)
    return match


def test_gosto_pizza():
    assert rank_pizza("Marguerita", 1) == ["Alisson", "LuizCarlos"]
    assert rank_pizza("Marguerita", 2) == ["Fred",]
    assert rank_pizza("Marguerita", 3) == []
    assert rank_pizza("Marguerita", 4) == ["Joao", "Conrado"]
    assert rank_pizza("Marguerita", 5) == ["Lucas", "Everton"]


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
