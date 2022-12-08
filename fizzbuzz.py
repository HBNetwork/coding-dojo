# Regras do fizzbuzz

# 1. Quando a posição é multipla de 3 fale fizz
# 2. Quando a posição é multipla de 5 : fale buzz
# 3. Quando a posicao for multipla de 3 e 5 fale fizzbuzz
# 4. Para qualquer outra posição fale o próprio número

# Entrada
# Entra um número inteiro
import pytest

def divisao(numero, divisor):
    return numero % divisor == 0
    

def fizz_buzz(numero):
    resp = numero
    fizz = 'fizz'
    buzz = 'buzz'

    if divisao(numero, 3) and divisao(numero, 5):
       resp = fizz+buzz
        
    elif divisao(numero, 3):
        resp = fizz

    elif divisao(numero, 5):
        resp = buzz
 
    return resp

    


def test_multiplo_tres():
    assert fizz_buzz(3) == 'fizz'
    assert fizz_buzz(6) == 'fizz'
    assert fizz_buzz(9) == 'fizz'
    
def test_multiplo_cinco():  
    assert fizz_buzz(5) == 'buzz'
    assert fizz_buzz(10) == 'buzz'

def teste_multiplo_tres_cinco():
    assert fizz_buzz(15) == 'fizzbuzz'

def test_fizz_buzz():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(4) == 4
    #fizz
# test_fizz_buzz()

if __name__ == "__main__":
    pytest.main(["-s", __file__])

    
"""
Dinâmica de 3 minutos
    
Lista de Participantes
1. Leonardo Perrella
2. Felipe
3. Luiz Arthur
4. Cássio Augusto
5. Breno Santana
6. Marcelo Schneider
7. Gregorio
8. Felipe
9.
10.
"""