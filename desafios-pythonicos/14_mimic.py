"""
14. mimic
Neste desafio você vai fazer um gerador de lero-lero.
É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.
Para isso você precisa:
A. Abrir o arquivo especificado via linha de comando.
B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.
C. Criar um dicionário de "imitação".
Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.
Por exemplo, suponha um arquivo com o conteúdo: A B C B A  

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B
Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.
Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.
Use a string vazia como a primeira palavra do texto para preparar as coisas.
Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""
"""

09/01/2023
16/01/2023

1 - Álisson
2 - Greg
3 - Luiz Carlos 
4 - joão m
6 - Conrado
7 - Everton
8 - Andre


"""

import random
import sys


def mimic_dict(filename):
  """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes."""
  dict_palavras = {}

  with open(filename, 'r') as arquivo:
    palavras = arquivo.read().upper().split()

  dict_palavras[''] = [palavras[0]]

  for i, palavra in enumerate(palavras):
    #print(i, palavra, len(palavras))
    temp = []
    if len(palavras) - 1 != i:
      if palavra in dict_palavras.keys():
        temp = dict_palavras[palavra]
        if palavras[i + 1] not in temp:
          temp.append(palavras[i + 1])
          dict_palavras[palavra] = temp
      else:
        temp = []
        temp.append(palavras[i + 1])
        dict_palavras[palavra] = temp

  if palavras[-1] in dict_palavras:
    dict_palavras[palavras[-1]].append('')
  else:
    dict_palavras[palavras[-1]] = ['']
  #print(dict_palavras)
  return dict_palavras


def print_mimic(mimic_dict, word, qnt_palavras=200):
  """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
  texto_lerolero = list()

  for _ in range(qnt_palavras):
    palavra_sorteada = random.choice(mimic_dict[word])
    texto_lerolero.append(palavra_sorteada)
    word = palavra_sorteada
  print(' '.join(texto_lerolero))


# Chama mimic_dict() e print_mimic()
def main():
  if len(sys.argv) not in [2, 3]:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])

  print((sys.argv))
  qnt_palavras = int(sys.argv[2]) if len(sys.argv) == 3 else 200
  print_mimic(dict, '', qnt_palavras)


if __name__ == '__main__':
  main()
