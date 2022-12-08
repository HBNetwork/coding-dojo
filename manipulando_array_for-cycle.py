import pytest
'''
1 - Vaccari
2 - Kelver
3 - Cassio
4 - Greg
5 - Diogo 
6 - David
7 - Álisson
8 - Juliano
9 - 

05/10/2022

'''

# Tarefa: Array
# Para o array de entrada fornecido, devemos produzir um novo array, implementando a lógica:
# se virmos 2, devemos ignorá-lo
# caso contrário, devemos multiplicar por 2
# Exemplo de entrada:
# [1, 2, 3]
# Exemplo de saída:
# [2, 6]

# Tarefas:
# - Implemente a função usando for-cycle - OK
# - Adicione as type annotations para a função
# - Comente o código anterior e implemente-o usando list comprehansion
# - Comente o código anterior e implemente-o usando os geradores python


def challenge_generators(values):
    resp = []

    for i in meugenerator(values):
        resp.append(i)
    return resp


def meugenerator(values):
    for value in values:
        if value != 2:
            yield value * 2

def outro_gen(values):
  vs = iter(values)
  resp = []

  while True:
    try:
      v = next(vs)
      if v == 2:
        continue
      resp.append(v * 2)
    except StopIteration:
      break
  return resp

def challenge_comprehansion(values: list) -> list:
    return [value * 2 for value in values if value != 2]


def challenge_for(values: list) -> list:
    resp = []
    for value in values:
        if value == 2:
            continue
        resp.append(value * 2)

    return resp


def test_challenge_for():
    assert challenge_for([1, 2, 3]) == [2, 6]
    assert challenge_for([2, 3, 4, 2, 5]) == [6, 8, 10]
    assert challenge_for([]) == []
    assert challenge_for([42]) == [84]
    #assert list_challenge(42) == [84]


def test_challenge_comprehansion():
    assert challenge_comprehansion([1, 2, 3]) == [2, 6]
    assert challenge_comprehansion([2, 3, 4, 2, 5]) == [6, 8, 10]
    assert challenge_comprehansion([]) == []
    assert challenge_comprehansion([42]) == [84]


def test_challenge_generators():
    assert outro_gen([1, 2, 3]) == [2, 6]
    assert challenge_generators([1, 2, 3]) == [2, 6]
    assert challenge_generators([1, 2, 3]) == [2, 6]
    assert challenge_generators([2, 3, 4, 2, 5]) == [6, 8, 10]
    assert challenge_generators([]) == []
    assert challenge_generators([42]) == [84]


if __name__ == "__main__":
    pytest.main(['-svv', __file__])

    list = meugenerator([1, 2, 3])

    print((list))
    print(next(list))
    print(next(list))
