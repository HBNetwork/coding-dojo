"""
Data: 15/02/2023

Fonte do Desafio: 

Enunciado:



Participantes:
1 -
2 - 
3 - 
4 - 
5 - 
6 - 
7 - 
8 - 
9 - 

"""

import pytest


def decodificador(frase):
    teclas = [
        "-", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"
    ]
    msg_decodificada = ""
    for letra in frase:
        for i, tecla in enumerate(teclas):
            if letra in tecla:
                msg_decodificada += str(i)

    return msg_decodificada.replace('0', '-')


def test_decodificador():
    assert decodificador('MY-LOVE') == '69-5683'
    assert decodificador('MY-MISERABLE-JOB') == '69-647372253-562'
    assert decodificador('HOME-SWEET-HOME') == '4663-79338-4663'


if __name__ == "__main__":
    pytest.main(["-s", __file__])
