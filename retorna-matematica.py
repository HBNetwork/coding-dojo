"""
Escreva uma função que adiciona como entrada um vetor de strings contendo um inteiro N, seguido por N elementos de frases como entrada. Como saída, ele retorna uma string onde cada frase, é a sequência das palavras invertidas, a não ser que nessa frase uma das palavras seja um número. Nesse caso, você retorna “MATEMATICA” ( sem acento). Cada frase é separada nessa string de retorno com um separador de ponto e virgula (;).

Nota: As linhas de saída não devem ter nenhum espaço em branco sobrando antes do depois da frase.

Perceba que o primeiro elemento é um número que serve para falar quantas frases virá em seguida. Esse número não aparece na saída e nem conta para falar “MATEMATICA”.

Clicando em "Run Code" na barra de ferramentas você roda o código atual e clicando em "Run Test Cases" já vê como ele saiu para o conjunto de teste =).

No final desse desafio não se esqueça de continuar até o botão " Submit Assessment ".

Não se preocupe caso apareca Cópia detectada. Isso aparece ao fazer Ctrl + V e não significa nada.

Restrições:

0 < Número máximo de entradas <= 100
0 < Número máximo de palavras em uma frase < 100
0 < Tamanho máximo de uma palavra < 30

Entrada:
["4","Olá Mundo", "Tchau Mundo", "1 mundo", "Primeiro mundo"]

Saída:
Mundo Olá;Mundo Tchau;MATEMATICA;mundo Primeiro

Entrada: ["5", "negociar com razão", "0 raposa marrom rápida", "esta é uma frase aleatória", "esta não é uma frase tão aleatória", "ok tchau"]

Saída: razão com negociar;MATEMATICA ;sentença aleatória a é essa;sentença aleatória então não é isso;tchau ok

"""



"""
- Álisson
- Cássio
- David
- Igor
- Filipe (se ainda ter como)
"""
import pytest

def invert_phrase(lista):
  retorno = ''
  
  for i in range(1, int(lista[0])+1):
    for char in lista[i]:
      mat = False
      if char.isnumeric():
        retorno += "MATEMATICA"
        mat = True
        break
      else:
        continue
    
    if mat:
      lista2 = ''
    else:
      lista2 = lista[i].split()[::-1]
      
    lista_temp = []
    for i in lista2:
      lista_temp.append(i)
    retorno += " ".join(lista_temp) + ';'
    
  return retorno[:-1]
  

def test_invert_phrase():
    assert invert_phrase(['1', 'CALCULADORA']) == 'CALCULADORA'
    assert invert_phrase(['1', 'texto 22']) == 'MATEMATICA'
    assert invert_phrase(['1', 'mundo 42']) == 'MATEMATICA'
    assert invert_phrase(['1', 'CALCULO']) == 'CALCULO'
    assert invert_phrase(['1', 'PRIMERO MUNDO']) == 'MUNDO PRIMERO'
    assert invert_phrase(['2', 'PRIMERO MUNDO', 'OLA MUNDO']) == 'MUNDO PRIMERO;MUNDO OLA'
    
    assert invert_phrase(["3", "negociar com razão", "2 raposa rápida", "esta frase alea"]) == "razão com negociar;MATEMATICA;alea frase esta"


if __name__ == "__main__":
    pytest.main(['-svv', __file__])