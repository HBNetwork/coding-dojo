"""
Escreva um programa que gere todos os anagramas potenciais de uma string.

Por exmplo, os anagramas potenciais de "biro" são:

biro bior brio broi boir bori
ibro ibor irbo irob iobr iorb
rbio rboi ribo riob roib robi
obir obri oibr oirb orbi orib

12-06-2023
- mconrado
- joão moreno
- alisson 
- everton
- luiz carlos

"""
import pytest
import random
from math import factorial


def anagrama(palavra):
  resultado = []
  tam = len(palavra)
  total_anagramas = factorial(tam)
  
  while len(resultado) < total_anagramas:
      palavra_list = list(palavra)
      random.shuffle(palavra_list)
      palavra_str = "".join(palavra_list)
      if palavra_str not in resultado:
          resultado.append(palavra_str)
  return resultado.sort()

def test_anagrama():
  assert anagrama('pai') == ['pai', 'pia', 'api', 'aip', 'ipa', 'iap'].sort()
  assert anagrama('biro') == ['biro', 'bior', 'brio', 'broi', 'boir', 'bori',
                              'ibro', 'ibor', 'irbo', 'irob', 'iobr', 'iorb',
                              'rbio', 'rboi', 'ribo', 'riob', 'roib', 'robi',
                              'obir', 'obri', 'oibr', 'oirb', 'orbi', 'orib',].sort()


if __name__ == "__main__":
    pytest.main(['-svv', __file__])

