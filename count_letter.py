"""
14/12/2022
Quem trouxe: João Holand
Local: Python na Prática vol 2 (Fernando Feltrin)

Desafio: 
Na frase (a radiologia é a ciência que estuda a anatomia por meio de exames de imagem).realize a contagem dos caracteres de sua composição, retornando quais os caracteres mais recorrentes, e quantas vezes os mesmos aparecem na frase acima.

"""
'''
Greg
Kelver
Mconrado
joão m.
Everton Matos
Cássio Augusto
Luiz Carlos 
Álisson
'''


def count_letter(letter, phrase='a radiologia é a ciência que estuda a anatomia por meio de exames de imagem'):
    count_w = phrase.count(letter)
    return count_w

def count_top_letters(phrase, top=5):
  
  contador = dict()  
  for letter in phrase.replace(" ", ""):
    if letter not in contador:
      contador[letter] = count_letter(letter, phrase)
    
  for id, val in enumerate(sorted(contador, key=contador.get, reverse=True)):
    if id > top - 1:
      del contador[val]
  return contador
    

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(count_letter, 'a', 12)
    test(count_letter, 'e', 8)    
    test(count_letter, 'i', 7)
    test(count_letter, 'o', 5)
    test(count_letter, 'm', 5)
    test(count_top_letters, 'a radiologia é a ciência que estuda a anatomia por meio de exames de imagem', {'a': 12, 'e': 8, 'i': 7, 'o': 5, 'm': 5})
