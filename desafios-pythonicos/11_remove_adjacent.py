"""
11. remove_adjacent
Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.
Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""
"""
Colocar nome aqui

- Kelver
- Álisson
- Andre Lucas
- Conrado
- joão m.
- Greg
- Luiz Carlos 
- Everton
- Carlos
- cassio

"""


def remove_adjacent_joão(nums):
    # +++ SUA SOLUÇÃO +++
    if nums == []:
        resposta = nums
    else:
        itens = [a for a, b in zip(nums, nums[1:] + [not nums[-1]]) if a != b]
        resposta = itens
    return resposta


def remove_adjacent_kelver(nums):
    # +++ SUA SOLUÇÃO +++
    repeatedNums = []
    for index, elem in enumerate(nums):
        if index == 0:
            repeatedNums.append(elem)
        elif elem != nums[index - 1]:
            repeatedNums.append(elem)
    return repeatedNums


def remove_adjacent_greg(nums):
    lista_nums = []
    for i, num in enumerate(nums):
        print(i, num)
        if i == 0:
            lista_nums.append(num)
        else:
            if nums[i - 1] != num:
                lista_nums.append(num)
    return lista_nums


def remove_adjacent(nums):
    # +++ SUA SOLUÇÃO +++
    lista_numeros = []
    for i in nums:
        if len(lista_numeros) == 0 or lista_numeros[-1] != i:
            lista_numeros.append(i)
    return lista_numeros


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
