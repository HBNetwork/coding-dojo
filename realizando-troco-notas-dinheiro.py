"""
    Funcionários de empresas comerciais que trabalham como caixa tem uma grande responsabilidade em suas mãos. A maior parte do tempo de seu expediente de trabalho é gasto recebendo valores de clientes e, em alguns casos, fornecendo troco.
    
    Seu desafio é fazer um programa que leia o valor total a ser pago e o valor efetivamente pago, informando o menor número de cédulas e moedas que devem ser fornecidas como troco.
    
    Deve-se considerar que há:
    
    cédulas de R$100,00, R$50,00, R$10,00, R$5,00 e R$1,00;
    moedas de R$0,50, R$0,10, R$0,05 e R$0,01.
    
    1 - Marcio
    2 - Alisson
    3 - Kelver
    4 - David
    5 - Gregorio
    6 - Luiz 
    """

import pytest


def dinheiro(valor_total, valor_pago):

    caixa = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]

    total_cedulas = []

    troco = valor_pago - valor_total
   
    while (troco != 0):
        for c in caixa:
            if c <= troco:
                total_cedulas.append(c)
                troco = troco - c
                break
            else:
                continue
    return total_cedulas

def test_dinheiro():
    assert dinheiro(100, 100) == []
    assert dinheiro(50, 100) == [50]
    assert dinheiro(2, 2.50) == [0.50]
    assert dinheiro(70, 100) == [20, 10]
    assert dinheiro(80, 100) == [20]
    assert dinheiro(75, 100) == [20, 5]
    assert dinheiro(500, 1000) == [200, 200, 100]
    assert dinheiro(611.75, 3000) == [200,200,200, 200,200, 200,200, 200,200, 200,200, 100,50,20,10,5,2,1,0.25]


if __name__ == "__main__":
    pytest.main(['-svv', __file__])