
def pares(carta_j1, carta_j2):
    quantidade_j1 = {}
    quantidade_j2 = {}

    for i in range(0, 5):
        x = carta_j1.count(carta_j1[i])
        quantidade_j1[carta_j1[i]] = x
        y = carta_j2.count(carta_j2[i])
        quantidade_j2[carta_j2[i]] = y

    print(quantidade_j1, quantidade_j2)
    return True

from random import sample, shuffle

# create a list
baralho = [
    2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8,
    8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13,
    13, 13, 13, 14, 14, 14, 14
]
shuffle(baralho)
print('baralho', baralho)

mesa = baralho[0:5]

print('mesa', mesa)

# remove 9 from the list
baralho.remove(9)

# Updated  List
print('Updated List: ', baralho)


if __name__ == "__main__":
    pares([5, 5, 6, 7, 13], [2, 3, 8, 8, 11])        