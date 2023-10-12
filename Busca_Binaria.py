'''
DATA: 06/09/2023

FONTE: https://exercism.org/tracks/python/exercises/binary-search

ENUNCIADO: Busca Binária

Introdução
Você encontrou um grupo de matemáticos que também são cantores e compositores. Eles escreveram uma música para cada um de seus números favoritos e, como você pode imaginar, eles têm muitos números favoritos ( 0 ou 73 ou 6174).

Você está curioso para ouvir a música para o seu número favorito, mas com tantas músicas para percorrer, encontrar a música certa pode demorar um pouco. Felizmente, eles organizaram suas músicas em uma lista de reprodução classificada pelo título —, que é simplesmente o número da música.

Você percebe que pode usar um algoritmo de pesquisa binária para encontrar rapidamente uma música com o título.
Instruções
Sua tarefa é implementar um algoritmo de pesquisa binária.

Um algoritmo de pesquisa binária encontra um item em uma lista dividindo-o repetidamente ao meio, mantendo apenas a metade que contém o item que estamos procurando. Isso nos permite restringir rapidamente os locais possíveis do nosso item até encontrá-lo ou até eliminarmos todos os locais possíveis

O algoritmo se parece com isso:

Encontre o elemento do meio de um classificado liste e compare com o item que estamos procurando.
Se o elemento do meio é o nosso item, terminamos!
Se o elemento do meio for maior que o nosso item, podemos eliminar esse elemento e todos os elementos depois isto.
Se o elemento do meio for menor que o nosso item, podemos eliminar esse elemento e todos os elementos antes isto.
Se todos os elementos da lista foram eliminados, o item não está na lista.
Caso contrário, repita o processo por parte da lista que não foi eliminada.
Aqui está um exemplo:

Digamos que estamos procurando o número 23 na seguinte lista classificada: [4, 8, 12, 16, 23, 28, 32].

Começamos comparando 23 com o elemento do meio, 16.
Como 23 é maior que 16, podemos eliminar a metade esquerda da lista, deixando-nos com [23, 28, 32].
Em seguida, comparamos 23 com o novo elemento do meio, 28.
Como 23 é menor que 28, podemos eliminar a metade certa da lista: [23].
Encontramos nosso item.

Participantes:

- João M. 
- Mestre de Cerimônia Onrado
- Frederico
- Greg master
- AVC
- Lucas
- Everton
- 

'''


import pytest
import math


def numero_do_meio(lista_base):
    indice_metade = indice_da_metade(lista_base) #len(lista_base)//2 
    return lista_base[indice_metade]


def indice_da_metade(lista_base):
    tamanho_da_lista = len(lista_base) 
    
    if tamanho_da_lista % 2 == 0:
        metade = int(tamanho_da_lista/2)
    else:
        metade = int(math.ceil(tamanho_da_lista/2))
    return int(metade - 1)


def busca_binaria(lista_base, num):
    if len(lista_base) == 0:
        return False
    
    if len(lista_base) == 1:
        if num == lista_base[0]:
            return True
        
    num_meio = numero_do_meio(lista_base)
    indice = indice_da_metade(lista_base)
    if num > num_meio:
        return busca_binaria(lista_base[indice+1:], num)
    else:
        return busca_binaria(lista_base[:indice], num)

def busca_binaria2(lista_base, num):
    inicio = 0
    fim = len(lista_base) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista_base[meio] == num:
            return lista_base[meio]
        elif lista_base[meio] < num:
            inicio = meio + 1
        else:
            fim = meio - 1



    

def test_busca_binaria():
    assert indice_da_metade([6]) == 0
    assert indice_da_metade([8,19]) == 0
    assert indice_da_metade([5,9,11]) == 1
    assert indice_da_metade([5,7,9,11,13,15]) == 2
    assert indice_da_metade([39,50,63,88,102,123,135,158]) == 3
    assert indice_da_metade([39,50,63,88,102,123,135,158,167]) == 4

    assert numero_do_meio([6]) == 6
    assert numero_do_meio([8,19]) == 8
    assert numero_do_meio([5,7,9,11]) == 7
    assert numero_do_meio([5,7,11]) == 7
    assert numero_do_meio([39,50,63,88,102,123,135,158]) == 88
    assert numero_do_meio([39,50,63,88,102,123,135,158,167]) == 102
    
    #assert acha_numero([1,2,3], 3) == True
    assert busca_binaria([5,9,14,28,36,61], 28) == True
    assert busca_binaria([5,9,14,20,28,36,61], 28) == True
    assert busca_binaria([5,9,14,20,28,36,61], 40) == False

    assert busca_binaria2([5,9,14,20,28,36,61], 28) == 28
    assert busca_binaria2([5,9,14,20,28,36,61], 40) == None

if __name__ == "__main__":
    pytest.main(['-svv', __file__])
