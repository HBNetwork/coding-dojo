"""
26/06/2023
Fonte: Desafio Técnico - Márcio Conrado

Enunciado: Gaveta Mágica

Considere que vocé tem uma gaveta magica em que vocé pode guardar moedas por um
tempo. Essa é uma gaveta muito segura, não se preocupe que você nao vai perder suas,
moedas!

Uma vez guardadas, as moedas se multiplicam. Ao retira-las, algumas somem. Após
observar por algum tempo você acredita ter descoberto como a magica funciona:

- Uma moeda sozinha que ficar um dia guardada na gaveta gera uma moeda
adicional no dia seguinte

- Para cada moeda retirada, uma outra deve sumir

Como vocé é um programador, quer oferecer um aplicativo que permite que qualquer
pessoa saiba quantas moedas terá ao fim de um período de uso da gaveta magica.

Crie uma função que recebe como entrada um vetor de moedas que sãoo inseridas e
removidas da gaveta, e devolve o valor final de moedas resultante no dia seguinte ao dia final indicado no vetor.

Exemplo de entrada [1, -1, 2, 0, 4]
[{1,(2)}, {-1 (1)(0)},{2},{(4),0(8),4, 12(24),]

CAIXA = [1,2,1,0,2,4,8,12,24]

Significado
- Dia 0: uma moeda guardada
- Dia 1: uma moeda retirada
- Dia 2: duas moedas guardadas
- Dia 3: nenhuma moeda guardada ou retirada
- Dia 4: quatro moedas guardadas
- Dia 5 = dia final.

Considere que o maximo de moedas é retirado no último dia.

Participantes:
- Márcio Conrado
- Luiz Carlos
- Gregorio
- Álisson
- Cássio
- David


"""

import pytest




def saldo_gaveta_magica(operacoes):
    saldo = 0
    resultado = [operacoes[0]]
    for transacao in operacoes:
        if transacao < 0:
            saldo = transacao * 2 + saldo
        else:
            saldo += transacao
            saldo = saldo * 2
        resultado.append(saldo)

    return resultado[-1]


def test_saldo_gaveta_magica():
    assert saldo_gaveta_magica([1]) == 2
    assert saldo_gaveta_magica([1, 1]) == 6
    assert saldo_gaveta_magica([1, 1, 1]) == 14
    assert saldo_gaveta_magica([1, 2]) == 8
    assert saldo_gaveta_magica([1, 0]) == 4
    assert saldo_gaveta_magica([0, 1]) == 2
    assert saldo_gaveta_magica([1, 2, 3]) == 22
    assert saldo_gaveta_magica([3, 2, 1]) == 34
    assert saldo_gaveta_magica([1, -1]) == 0
    assert saldo_gaveta_magica([3,-1]) == 4
    assert saldo_gaveta_magica([1, -1, 2, 0, 4]) == 24
    assert saldo_gaveta_magica([-1,0]) == -4
    assert saldo_gaveta_magica([-1,0,4]) == 0



if __name__ == "__main__":
    pytest.main(['-svv', __file__])
