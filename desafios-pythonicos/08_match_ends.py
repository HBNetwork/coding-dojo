"""
08. match_ends
Dada uma lista de strings, retorne a contagem do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.
PS: Python não possui o operador ++, porém += funciona.
"""
'''
Greg
Kelver
Mconrado
Álisson
Tiago
joão m.
Everton Matos
Cássio Augusto

'''
def match_ends_kelver(words):
  l = list(filter(lambda x: len(x) >= 2 and x[0] == x[-1], words))
  return len(l)

def match_ends_conrado(list_of_words):

    # +++ SEGUNDA SOLUÇÃO +++
    return sum( 1 for word in list_of_words if len(word) >= 2 and word[0] == word[-1] )

def match_ends_alisson(words):
    return len([1 for w in words if len(w) >= 2 and w[0] == w[-1]])

  
def match_ends(words):
   # +++ SUA SOLUÇÃO +++
 
    contador = 0
    for c in words:   
        if (len(c) >= 2 and c[0] == c[-1]):
            contador += 1
    return contador

    # +++ SUA SOLUÇÃO +++
    #return


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
    test(match_ends, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends, ['aaa', 'be', 'abc', 'hello'], 1)
