"""
12. linear_merge
Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.
A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""
"""
- Conrado
- Tiago
- Kelver
- Álisson
- Greg
- 

"""
import heapq


#Precisou criar uma cópia das listas devido a lista ser esvaziada em cada ciclo do loop. Como a lista é representada dinamicamente (id/endereço de memória) precisou recriar. No python tudo é referência.
def linear_merge(list1, list2):
    lista_aux = []
    list1Aux = list1.copy()
    list2Aux = list2.copy()
    while len(list1Aux) + len(list2Aux) > 0:
        if list1Aux[-1:] > list2Aux[-1:]:
            lista_aux.append(list1Aux[-1])
            list1Aux.pop()
        else:
            lista_aux.append(list2Aux[-1])
            list2Aux.pop()

    return lista_aux[::-1]


def linear_merge_3(list1, list2):
    return sorted(list1.copy() + list2.copy())


def linear_merge_2(list1, list2):
    return list(heapq.merge(list1, list2))


def linear_merge_1(list1, list2):
    #lista_final = list1 + list2
    return sorted(list1 + list2)


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
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
