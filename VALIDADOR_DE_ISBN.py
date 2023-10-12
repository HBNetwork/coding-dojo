'''
Fonte: https://www.codewars.com/kata/51fc12de24a9d8cb0e000001
Enunciado: 
VALIDADOR DE ISBN 

Os identificadores ISBN-10 têm dez dígitos. Os primeiros nove caracteres são dígitos de 0 a 9. O último dígito pode ser 0-9 ou X, para indicar um valor de 10.

Um número ISBN-10 é válido se a soma dos dígitos multiplicada pela sua posição módulo 11 for igual a zero.

Por exemplo:

ISBN: 1 1 1 2 2 2 3 3 3 9
posição: 1 2 3 4 5 6 7 8 9 10

Este é um ISBN válido porque:

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10)% 11 = 0

Exemplos

1112223339 --> verdadeiro
111222333 --> falso
1112223339X --> falso
1234554321 --> verdadeiro
1234512345 --> falso
048665088X --> verdadeiro
X123456788 --> falso


Participantes:
- Conrado
- Fred 
- João M. 
- Diogo
- Greg
- AVC
- Lucas
- Luciano
- Luiz Lins


'''

import pytest


def valida_isbn(isbn):
    if len(isbn) != 10:
        return False
    
    #if  'X' in isbn_str:
    #if isbn_str.index('X') != -1:
    #    return False
        
    if isbn[0:9].isdigit() == False:
        return False

    total_soma = 0

    for index, digito in enumerate(isbn):
        if (digito == 'X'):
            digito = 10
        total_soma += int(digito) * (index+1)
  
    
    return total_soma % 11 == 0 
  


def test_valida_isbn():
    assert valida_isbn('1112223339') == True
    assert valida_isbn('111222333') == False
    assert valida_isbn('1112223339X') == False
    assert valida_isbn('048665088X') == True
    assert valida_isbn('X123456788') == False
    assert valida_isbn('1234554321') == True
    assert valida_isbn('1234512345') == False
    assert valida_isbn('12X45X2345') == False
    assert valida_isbn('1245X2345X') == False
    assert valida_isbn('124eXd2345X') == False


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
