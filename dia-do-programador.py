'''
14/09/2022
'''
import pytest
import datetime


def que_dia_eh_hoje(data):
    """
        Função para verificar se é o dia do programador.
    """
    hoje = datetime.datetime.now()

    if (data.strftime("%x") < hoje.strftime("%x")):
        print('Hey programador, estamos quase chegando no seu dia =D')
        return False
    if (data.strftime("%x") > hoje.strftime("%x")):
        print('Hey programador, já passou o seu dia =(')
        return False
    else:
        print("Hey, chegou o seu dia , feliz dia do programador!")
        return True


def test_dia_programador_passou():
    assert que_dia_eh_hoje(datetime.datetime(2022, 9, 14)) == False


def test_dia_programador_hoje():
    assert que_dia_eh_hoje(datetime.datetime(2022, 9, 13)) == True


def test_dia_programador_vai_chegar():
    assert que_dia_eh_hoje(datetime.datetime(2022, 9, 12)) == False


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
