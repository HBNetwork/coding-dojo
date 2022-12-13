"""
07. front_back
Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.
Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.
Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
'''
- Greg
- Álisson
- Everton
- Conrado
- Tiago
- Kelver
- joão m.

'''
import math


def pega_metade(string):
    return math.ceil(len(string) / 2)


def separa_front_back(s):
    tam = pega_metade(s)
    return s[:tam], s[tam:]


def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    metade_a_1, metade_a_2 = separa_front_back(a)
    metade_b_1, metade_b_2 = separa_front_back(b)
    return ''.join([metade_a_1, metade_b_1, metade_a_2, metade_b_2])


def front_back_1(a, b):
    tamA = len(a)
    tamB = len(b)

    if (tamA % 2 == 0):
        metade_a_1 = a[:tamA // 2]
        metade_a_2 = a[tamA // 2:]
    else:
        metade_a_1 = a[:(tamA // 2) + 1]
        metade_a_2 = a[(tamA // 2) + 1:]

    if (tamB % 2 == 0):
        metade_b_1 = b[:tamB // 2]
        metade_b_2 = b[tamB // 2:]
    else:
        metade_b_1 = b[:(tamB // 2) + 1]
        metade_b_2 = b[(tamB // 2) + 1:]

    return metade_a_1 + metade_b_1 + metade_a_2 + metade_b_2


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
