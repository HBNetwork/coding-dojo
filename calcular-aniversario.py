import pytest
from datetime import datetime
import pytz
from dateutil.relativedelta import relativedelta
# Receber ano, mes e dia de nascimento e retornar a idade em anos.
# Ex.: get_age(1988, 9, 12)
# Em que o ano é 1988, o mês é 9 e o dia é 12

# 08/02/2023
'''

- Cássio
- Luiz
- Greg
- Conrado
- Álisson
- Everton
- Carlos Xavier

'''


def get_age(ano, mes, dia):
    hoje = datetime.now(pytz.timezone('America/Argentina/Salta'))
    quantos_anos_tem = hoje.year - ano
    quantos_meses_tem = 0
    
    if hoje.month < mes:
        quantos_anos_tem = quantos_anos_tem - 1
        quantos_meses_tem = 12 + (hoje.month - mes)
    elif hoje.month == mes:
        if hoje.day <= dia:
            quantos_anos_tem = quantos_anos_tem - 1
    else:
        quantos_meses_tem = hoje.month - mes

    return [quantos_anos_tem, quantos_meses_tem]

def get_age_delta(ano, mes, dia):
    return relativedelta(datetime.now(), datetime(ano, mes, dia)).years
    
def test_aniversario():
    assert get_age(2000, 1, 8) == [23, 1]
    assert get_age(2000, 2, 7) == [23, 0]
    assert get_age(2000, 2, 9) == [22, 0]
    assert get_age(1988, 9, 12) == [34, 5]  # Luiz Carlos
    assert get_age(1991, 3, 17) == [31, 11] # Greg
    assert get_age(1983, 9, 26) == [39, 5]  # Conrado
    assert get_age(1988, 12, 19) == [34, 2] # Cassio
    assert get_age(1996, 6, 21) == [26, 8]  # Carlos Xavier
    assert get_age(1991, 8, 13) == [31, 6]  # Everton

    assert get_age_delta(1991, 8, 13) == 31


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
