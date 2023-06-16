"""
03/05/2023

Fonte: https://dojopuzzles.com/problems/interseccao-de-segmentos-de-reta/

Enunciado: Intersecção de segmentos de reta

Em geometria, um problema comum é determinar se duas linhas definidas do ponto A ao B e do C ao D respectivamente, se cruzam.

Desenvolva uma classe Linha2D com as seguintes funcionalidades:

Uma linha é construída fornecendo-se dois pontos A=(x1,y1) e B=(x2,y2);
Uma linha L1 deve ser capaz de responder a questão "Eu me cruzo com a linha L2?".
Este problema ilustra alguns problemas associados com algoritmos geométricos e com algoritmos de ponto-flutuante/numéricos; o que devemos fazer com problemas de arredondamento?

Participantes:
- Everton Matos
- Álisson S. Holkem
- João Moreno
- Gregorio
- Luiz Carlos
- Márcio Conrado
- Fred
- 
"""

import pytest


def ponto(x, y):
    return (x, y)


def linha(ponto_a, ponto_b):
    return [ponto_a, ponto_b]


def interseccao(linha_1, linha_2):
    xdiff = (linha_1[0][0] - linha_1[1][0], linha_2[0][0] - linha_2[1][0])
    ydiff = (linha_1[0][1] - linha_1[1][1], linha_2[0][1] - linha_2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    if div == 0:
        raise Exception('não há intersecção')

    d = (det(*linha_1), det(*linha_2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def interseccao2(linha_1, linha_2):
    kx, ky = linha_1[0][0], linha_1[1][0]
    lx, ly = linha_2[0][0], linha_2[1][0]
    nx, ny = linha_1[0][1], linha_1[1][1]
    mx, my = linha_2[0][1], linha_2[1][1]
    det = (nx - mx) * (ly - ky) - (ny - my) * (lx - kx)
    print(det)

    if (det == 0.0):
        return 0
        # não há intersecção

    s = ((nx - mx) * (my - ky) - (ny - my) * (mx - kx)) / det
    # t = ((lx - kx) * (my - ky) - (ly - ky) * (mx - kx)) / det

    Pix = kx + (lx - kx) * s
    Piy = ky + (ly - ky) * s

    # Pix = mx + (nx - mx) * t
    # Piy = my + (ny - my) * t

    return Pix, Piy


"""
/* k : ponto inicial da reta 1                                            */
/* l : ponto final da reta 1                                              */
/* m : ponto inicial da reta 2                                            */
/* n : ponto final da reta 2   
"""


def test_ponto():
    assert ponto(x=6, y=7) == (6, 7)


def test_linha():
    ponto_a = ponto(x=2, y=4)
    ponto_b = ponto(x=4, y=4)
    assert linha(ponto_a, ponto_b) == [(2, 4), (4, 4)]


def test_intercessao():
    ponto_a = ponto(x=6, y=7)
    ponto_b = ponto(x=2, y=3)
    linha_1 = linha(ponto_a, ponto_b)

    ponto_c = ponto(x=2, y=4)
    ponto_d = ponto(x=8, y=4)
    linha_2 = linha(ponto_c, ponto_d)

    assert interseccao(linha_1, linha_2) == (3, 4)

    #assert interseccao2(linha_1, linha_2) == (3, 4)


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
"""
ENTRADA
a = (6,7)
b = (2,3)
c = (2,4)
d = (8,4)

SAIDA: 
e = (3,4)
"""
"""
  1 2 3 4 5 6
-1*
-2   *
-3
-4

https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
"""
