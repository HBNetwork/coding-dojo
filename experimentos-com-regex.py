import pytest
import re
import datetime
'''
DESAFIOS DE REGEX
verificador de cpf - feito
placa de carro (funcionar para os dois padrões - antigo e mercosul) - feito
e-mail - feito

data e horário
06/02/2023 20:30:00
dia =  06
mes =  02
ano = 2023
hora = 20
minuto = 30
segundo = 00
- extrair preço e produto de tabloide de supermercado
- parametros url especifica
- pegar a  exceção do erro ()


'''

'''
- Greg
- Conrado
- Álisson
- Everton Matos
- joão moreno
- André Lucas
- Cássio

'''


def cpf(numero):
    encontrado = bool(
        re.match(r'[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}$', numero))
    return encontrado


def test_cpf():
    assert (cpf("123.456.789-10")) == True
    assert (cpf("12345678910")) == True
    assert (cpf("123.554.444-435")) == False
    assert (cpf("123.456.789-AB")) == False
    assert (cpf("1-23.456.789-10")) == False
    assert (cpf("123..456.789-10")) == False


def placa(informacao_placa):
    placa_antiga = '([a-z]{3}-?[0-9]{4}$)'
    placa_mercosul = '([a-z]{3}[0-9]{1}[a-z]{1}[0-9]{2}$)'
    encontrado = bool(
        re.match(rf'{placa_antiga}|{placa_mercosul}', informacao_placa,
                 re.IGNORECASE))
    return encontrado


def test_placa():
    assert (placa("ABC-1234")) == True
    assert (placa("ABC-12345")) == False
    assert (placa("ABC1234")) == True
    assert (placa("1234-ABC")) == False
    assert (placa("ABC1D23")) == True
    assert (placa("ABC7-D23")) == False


def email(endereco):
    encontrado = bool(
        re.match(r'[^0-9]\w*(\+\w*)?@\w*\.{1}\w*\.?\w*$', endereco))
    return encontrado


def test_email():
    assert (email('email@hbnetwork.com')) == True
    assert (email('email+tag@hbnetwork.com')) == True
    assert (email('email@hbnet@work.com')) == False
    assert (email('email@hbnetworkcom')) == False
    assert (email('email@hbnetwork.com.br')) == True
    assert (email('123email@hbnetwork.com.br')) == False
    assert (email('email123@hbnetwork.com.br')) == True


def datahora(horario):
    dia = r'(?P<dia>\d{2})'
    mes = r'(?P<mes>\d{2})'
    ano = r'(?P<ano>\d{4})'
    hora = r'(?P<hora>\d{2})'
    minuto = r'(?P<minuto>\d{2})'
    segundo = r'(?P<segundo>\d{2})'

    pattern = fr'{dia}/{mes}/{ano} {hora}:{minuto}:{segundo}'

    grupo_data = re.match(pattern, horario)
    try:
        datetime.datetime(day=int(grupo_data.group('dia')),
                          month=int(grupo_data.group('mes')),
                          year=int(grupo_data.group('ano')),
                          hour=int(grupo_data.group('hora')),
                          minute=int(grupo_data.group('minuto')),
                          second=int(grupo_data.group('segundo')))
        return True

    except Exception:
         return False


def test_datahora():

    assert (datahora('06/02/2023 20:36:05')) == True
    assert (datahora('99/02/2023 20:36:05')) == False
    assert (datahora('12/13/2023 20:36:05')) == False
    assert (datahora('12/12/2023 25:36:05')) == False
    assert (datahora('29/02/2023 20:36:05')) == False


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
