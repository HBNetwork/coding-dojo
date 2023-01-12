
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

if __name__ == "__main__":
    pares([5, 5, 6, 7, 13], [2, 3, 8, 8, 11])        