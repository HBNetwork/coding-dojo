'''
DATA: 27/09/2023 

FONTE: https://www.codewars.com/kata/57acc8c3e298a7ae4e0007e3

ENUNCIADO: 
Antecedentes - a Conjectura de Collatz:
Imagine que você receba um número inteiro positivo, n, então:

se n for par, calcule: n/2
se n for ímpar, calcule: 3 * n + 1
Repita até que sua resposta seja 1. A conjectura de Collatz afirma que realizando esta operação repetidamente, você sempre chegará a 1.

Você pode tentar criar sequências Collatz com este kata. Para mais informações, consulte a página wiki.

Agora! Sua tarefa:
Dada uma matriz de inteiros positivos, retorne o inteiro cuja sequência Collatz é a mais longa.

Exemplo:

mais longoCollatz([2, 4, 3])===3;
Explicação: A sequência de Collatz para 2 tem comprimento de 1, a sequência de 4 tem comprimento de 2 e a sequência de 3 tem comprimento de 7. Portanto, de nossa matriz, o inteiro 3 é aquele com a sequência de Collatz mais longa .

Portanto, sua função deve retornar 3.

Observação:
Pode haver mais de uma resposta, ou seja, dois ou mais inteiros produzem a sequência de Collatz mais longa, porque possuem sequências do mesmo comprimento. Neste caso, sua função deve retornar o número inteiro que aparece primeiro no array.

Exemplo: Dado um array: [2, 5, 32], tanto 5 quanto 32 têm sequências Collatz de comprimento 5. Essas também são as sequências mais longas de nosso array.

Nesse caso, nossa função retorna 5, porque 5 vem antes de 32 em nosso array.

https://www.youtube.com/watch?v=094y1Z2wpJg


PARTICIPANTES:
- Greg
- João
- MCOnrado
- Fred
- AVC 
- Luiz
- 
'''

import pytest


def longestCollatz(nums):
    pulos = []
    #count = 0
    if len(nums) == 0:  #verifica se existem elementos na lista
        return 0
    for n in nums:
        pulo = 0
        if n == 0:  #se algum elemento da lista for zero, desconsidera e segue para o próximo
            pulos.append(0)
            continue
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
            pulo += 1
            #count += 1
            #print(pulo)
        pulos.append(pulo)

    #print(pulos)
    maior = max(pulos)
    #print(maior)
    index_maior = pulos.index(maior)
    #print(f'Rodou {count} vezes')
    return nums[index_maior]


def test_longestCollatz():
    assert longestCollatz([2]) == 2
    assert longestCollatz([3]) == 3
    assert longestCollatz([2, 3]) == 3
    assert longestCollatz([2, 4, 3]) == 3
    assert longestCollatz([2, 5, 32]) == 5
    assert longestCollatz([2, 32, 5]) == 32
    assert longestCollatz([]) == 0
    assert longestCollatz([0]) == 0

    #codewars
    assert longestCollatz([4, 71, 7413, 62, 8045, 661, 22, 7558]) == 7413
    assert longestCollatz([6, 6196, 4, 3, 3660, 84, 14, 179, 3153,
                           9878]) == 9878
    assert longestCollatz([2801, 6365, 346, 6589, 7, 86, 5, 316, 62,
                           9]) == 6589


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
