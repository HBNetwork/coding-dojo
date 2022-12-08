import pytest
'''
Decompondo números
Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 digitos, 
onde cada um seja menor ou igual a <maxDigit>, 
e a soma dos digitos de cada número gerado seja 21.

Exemplos com maxDigit=6: 3666,4566

Ordem: 
- Gregorio
- Márcio
- Cassio Augusto
- Everton
- Leonardo
- 
'''
'''
Constraints:
-> Número máximo do parametro é 9
-> Número mínimo do parâmentro é 6
-> O parâmetro passado precisa estar contido na saída

'''


def calculator(n, target):
    return target - n


def decomposing_numbers(n):
    resp = ''
    sobrou = 21
    soma = 0
    if n <= 5:
        resp = '0000'
    while len(resp) < 4:
        if sobrou > 0:
            sobrou = calculator(n, sobrou)  #3
            if sobrou >= 0:
                resp += str(n)
                soma = soma + n
        else:
            sobrou = 21 - soma
            n = n - 1

        if soma == 21 and len(resp) < 4:
            resp += '0'
        if soma == 21:
            break

    return resp[::-1]


def decomposing_numbers2(n):
    if n <= 5:
        return ['0000']

    values = []

    for value in range(0, 10000):
        value_as_str = str(value).zfill(4)
        fir = int(value_as_str[0])
        sec = int(value_as_str[1])
        thi = int(value_as_str[2])
        fou = int(value_as_str[3])
        if fir + sec + thi + fou == 21 and (fir <= n and sec <= n and thi <= n
                                            and fou <= n):                                           
            if n in [fir, sec, thi, fou]:
                if fir <= sec and sec <= thi and thi <= fou:
                    values.append(str(str(fir) + str(sec) + str(thi) + str(fou)))
    return values


def test_asdf():
    assert decomposing_numbers(5) == '0000'
    assert decomposing_numbers(6) == '3666'
    assert decomposing_numbers(7) == '0777'
    assert decomposing_numbers(8) == '0588'
    assert decomposing_numbers(9) == '0399'

    assert decomposing_numbers2(5) == ['0000']
    assert decomposing_numbers2(6) == ['3666', '4566','5556']
    assert decomposing_numbers2(7) == ['0777', '1677', '2577', '2667', '3477', '3567', '4467', '4557']
    assert decomposing_numbers2(8) == ['0588', '0678', '1488', '1578', '1668', '2388', '2478', '2568', '3378', '3468', '3558', '4458']
    assert decomposing_numbers2(9) == ['0399', '0489', '0579', '0669', '1299', '1389', '1479', '1569', '2289', '2379', '2469', '2559', '3369', '3459', '4449']



if __name__ == "__main__":
    pytest.main(['-svv', __file__])
