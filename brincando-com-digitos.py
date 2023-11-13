"""
08/11/2023
Fonte: https://www.codewars.com/kata/5552101f47fc5178b1000050/python

Enunciado: 

Alguns números têm propriedades engraçadas. Por exemplo:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Dado um inteiro positivo n escrito como abcd... (a, b, c, d... sendo dígitos) e um inteiro positivo p

queremos encontrar um inteiro positivo k, se existir, tal que a soma dos dígitos de n elevados às potências sucessivas de p seja igual a k * n.
Em outras palavras:

Existe um inteiro k como: (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

Se for o caso retornaremos k, caso contrário retornaremos -1.

Nota: n e p serão sempre dados como números inteiros estritamente positivos.

dig_pow(89, 1) deve retornar 1 já que 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) deve retornar -1, pois não existe k, como 9¹ + 2² é igual a 92 * k
dig_pow(695, 2) deve retornar 2 já que 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) deve retornar 51 já que 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ =   2360688 = 46288 * 51

Participantes:
- Adailton
- Gregorio
- Fred
- Conrado
- João Moreno
- Lucas
- Alisson
- Everton


"""
import pytest


def calcula_potencia(numero, potencia):
    numeros_potencia = []

    for numero in str(numero):
        #print(numero, potencia)
        numeros_potencia.append(int(numero)**potencia)
        potencia += 1
    soma_potencias = sum(numeros_potencia)
    print(soma_potencias)
    #89 = [8, 9]
    return soma_potencias


def retorna_resultado(original, sum_potencia):
    resultado_final = int(sum_potencia/original)
    if resultado_final * original == sum_potencia:
        return resultado_final    
    else:
        return -1 
      
# OUTRA SOLUÇÃO:
# def dig_pow(n, p):
#   result = 0
#   n_str = str(n)
#   for num in n_str:
#       result += int(num)**p
#       p = p + 1

#   result_2 = int(result/n)
#   if result_2 * n == result:
#       return result_2
#   else:
#       return -1

def test_calcula_potencia():
    assert calcula_potencia(89, 1) == 89
    assert calcula_potencia(695, 2) == 1390
    assert calcula_potencia(46288, 3) == 2360688

def test_retorna_resultado():
    assert retorna_resultado(89, calcula_potencia(89, 1)) == 1
    assert retorna_resultado(695, calcula_potencia(695, 2)) == 2
    assert retorna_resultado(46288, calcula_potencia(46288, 3)) == 51
    

if __name__ == "__main__":
    pytest.main(['-svv', __file__])

