"""
Data: 14/09/2022

Participantes:
1 - Diogo Bueno
2 - Tiago Chaves
3 - Welington Carlos
4 - David Silveira
5 - Rogério
6 - Wilkne Maia 
7 - Cássio
8 - Whanderley -> Piloto
9 - Eli Junior -> Copiloto 



A definição do FizzBuzz é a seguinte:

Se n é divisível por 3 e 5, substitua por “FizzBuzz”.
Se n é divisível por 3, substitua por “Fizz”.
Se n é divisível por 5, substitua por “Buzz”.
Se n não é divisível nem por 3 nem por 5, apenas é dito n.
"""

import pytest


############## ÁREA DE CÓDIGO #############
def solution(input_):
    output = ''
    fizz = "Fizz"
    buzz = "Buzz"

    if not input_ % 3:
        output += fizz

    if input_ % 5 == 0:
        output += buzz

    return output or input_


    
############## ÁREA DE CÓDIGO #############

@pytest.mark.parametrize(
    "input_, output",
    [
        (1, 1),
        (2, 2),
        (3, "Fizz"),
        (4, 4),
        (5, "Buzz"),
        (6, "Fizz"),
        (7, 7),
        (8, 8),
        (9, "Fizz"),
        (10, "Buzz"),
        (11, 11),
        (12, "Fizz"),
        (13, 13),
        (14, 14),
        (15, "FizzBuzz"),
        (16, 16),
        (17, 17),
        (18, "Fizz"),
        (19, 19),
        (20, "Buzz"),
        (30, "FizzBuzz"),
    ]
)
def test_true_solution(input_, output):
    assert solution(input_) == output





if __name__ == "__main__":
    pytest.main(["-svv", __file__])