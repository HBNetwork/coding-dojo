"""
DATA: 28/06/2023 / 05/07/2023
FONTE: https://dojopuzzles.com/problems/descubra-o-assassino/

O empresário Luiz Carlos foi assassinado e o corpo dele foi deixado na frente da delegacia de polícia. O detetive Frederico Fávaro foi escolhido para investigar este caso. Após uma série de investigações, ele organizou uma lista com prováveis assassinos, os locais do crime e quais armas poderiam ter sido utilizadas.

Suspeitos:
- Gregorio
- MC Onrado
- Evertinho I.A.
- joão moreno.
- Lucas Paim
- Dêvid Teófilo
- Luiz Carlos 

Locais:
- Sorocaba/SP
- Rio de Janeiro/RJ
- Mogi das Cruzes/SP
- Recife/PE
- Restaurante no Fim do Universo
- São João do Sul
- Olho D'água/PB
- Teresópolis/RJ
- Ilha de Java
- Avaré/SP

Armas:
- Espada justiceira.
- Estilingue
- Shuriken do Naruto
- Besta
- Bazuca
- Katana

Uma testemunha foi encontrada, mas ela só consegue responder se Fred fornecer uma teoria. Para cada teoria ele "chuta" um assassino, um local e uma arma. A testemunha então responde com um número. Se a teoria estiver correta (assassino, local e arma corretos), ela responde 0. Se a teoria está errada, um valor 1,2 ou 3 é retornado. 
1 indica que o assassino está incorreto;
2 indica que o local está incorreto;
3 indica que a arma está incorreta.

Se mais de uma suposição está incorreta, ela retorna um valor arbitrário entre as que estão incorretos (isso é totalmente aleatório).

Por exemplo, se o assassino for MC Onrado usando a Shuriken do Naruto
 em Recife/PE:

Teoria: 1, 1, 1
Retorno: 1, ou 2, ou 3 (todos estão incorretos) 

Teoria: 3, 1, 3
Retorno: 1, ou 3 (somente o local está correto)

Teoria: 5, 3, 4
Retorno: 1 (somente o assassino está incorreto)

Teoria: 2, 3, 4
Retorno: 0 (todos corretos, você solucionou o caso)

Você precisa desenvolver um programa que tente resolver o problema. Inicialmente não se preocupe no número de tentativas necessário para encontrar a solução. Depois tente melhorar a maneira com que as teorias são testadas para que Fred encontre a solução do problema no menor número de tentativas.

ENUNCIADO: Descubra o assassino

Participantes:
- João Moreno
- Greg
- Lucas
- M Conrado
- Everton 
- Dêvid

TO-DO: 05/07/23
#1 Retornar os números do checa_palpite para dar a dica para o jogador se está tudo correto ou algo errado
#2 Tornar jogavel via input para o jogador humano





"""
import pytest
from functools import partial
from random import choice

assassinos = [
    'Gregorio', 'MC Onrado', 'Evertinho I.A.', 'João moreno', 'Lucas Paim',
    'Dêvid Teófilo', 'Arnaldinho'
]

locais = [
    'Sorocaba/SP', 'Rio de Janeiro/RJ', 'Mogi das Cruzes/SP', 'Recife/PE',
    'Restaurante no Fim do Universo', 'São João do Sul', 'Olho D\'água/PB',
    'Teresópolis/RJ', 'Ilha de Java', 'Avaré/SP'
]

armas = [
    'Espada justiceira', 'Estilingue', 'Shuriken do Naruto', 'Besta', 'Bazuca',
    'Katana'
]

# def comparacao(posicao, indice_fato):
#     return fato[indice_fato] == posicao

#def acha_assasino(posicao_assassino):
#return comparacao(posicao_assassino, 0)

#def acha_local(posicao_local):
#return comparacao(posicao_local, 1)

#def acha_arma(posicao_arma):
#return comparacao(posicao_arma, 2)

assassino = 5
local = 3
arma = 2
fato = [assassino, local, arma]

comparacao = lambda indice_fato, posicao, fato_: fato_[indice_fato] == posicao
acha_assasino = partial(comparacao, 0)
acha_local = partial(comparacao, 1)
acha_arma = partial(comparacao, 2)


def checa_palpite(palpite):
    lista_incorretos = []
    if not acha_assasino(palpite[0], fato):
        lista_incorretos.append(1)
    if not acha_local(palpite[1], fato):
        lista_incorretos.append(2)
    if not acha_arma(palpite[2], fato):
        lista_incorretos.append(3)
    if len(lista_incorretos) == 0:
        lista_incorretos.append(0)
    return choice(lista_incorretos)


def contar_atributos_fato(fatos):
    return len(fatos)


def test_acha_assasino():
    assert acha_assasino(1, fato) == False
    assert acha_assasino(2, fato) == False
    assert acha_assasino(3, fato) == False
    assert acha_assasino(5, fato) == True


def test_acha_local():
    assert acha_local(1, fato) == False
    assert acha_local(2, fato) == False
    assert acha_local(4, fato) == False
    assert acha_local(3, fato) == True


def test_acha_arma():
    assert acha_arma(1, fato) == False
    assert acha_arma(2, fato) == True
    assert acha_arma(4, fato) == False
    assert acha_arma(3, fato) == False


def test_checa_palpite():
    assert checa_palpite([5, 3, 2]) == 0
    assert checa_palpite([2, 2, 1]) in [1, 2, 3]
    assert checa_palpite([5, 2, 1]) in [2, 3]
    assert checa_palpite([5, 3, 4]) in [3]


'''
assassino = 5
local = 3
arma = 2
fato = [assassino, local, arma]
fato[1] == 'MC Orando' in Assassino
'''


def gerador_de_fatos():
    return [choice(assassinos), choice(locais), choice(armas)]


def mostra_index_dos_fatos(aux):
    return [
        assassinos.index(aux[0]),
        locais.index(aux[1]),
        armas.index(aux[2])
    ]


def test_gerador_de_fatos():
    assert contar_atributos_fato(fato) == 3
    assert type(gerador_de_fatos()) is list
    assert isinstance(gerador_de_fatos(), list) == True

    fatos = gerador_de_fatos()
    indices_fatos = mostra_index_dos_fatos(fatos)
    #print(fatos)
    #print(indices_fatos)

    _assassino = fatos[0]
    _local = fatos[1]
    _arma = fatos[2]
    assert _assassino in assassinos
    assert _local not in assassinos
    assert _local in locais
    assert _arma in armas

    #assert assassinos[gerador_de_fatos()[1]] == assassinos


def jogar_detetive(fatos):
    i = 0
    achou = False
    while (i < 1000):
        i += 1
        if fatos == gerador_de_fatos():
            achou = True
            break
    return [i, achou]


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
    fato = gerador_de_fatos()
    print(fato)
    jogo = jogar_detetive(fato)
    if jogo[1]:
        print(
            f'O detetive Frederico achou o assassino {fato[0]} que matou o Luiz na {jogo[0]} vez '
        )
    else:
        print(f'O detetive Frederico não achou o assassino {fato[0]} que matou o Luiz')
        
    #print(jogar_detetive(fato))

    #fato = gerador_de_fatos()
    #fatos_gerados = gerador_de_fatos()
    #print(fatos_gerados)
    #print(mostra_index_dos_fatos(fatos_gerados))
