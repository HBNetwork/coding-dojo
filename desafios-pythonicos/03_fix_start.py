"""
03. fix_start
Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.
Exemplo: 'babble' retorna 'ba**le'
Assuma que a string tem tamanho 1 ou maior.
Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""
'''

'1 - Conrado'
'2 - Kelver'
'3 - Vinicius'
'4 - Álisson'
'5 - Greg'
'6 - Carlos'

  '''


def fix_start(s):
    # +++ SUA SOLUÇÃO +++
    return s[0] + (s[1:].replace(s[0],'*'))
     
    """primeiro_caracter = s[0]
    string_final = ""
    for c in s[1:]:
        if c == primeiro_caracter:
            string_final += '*'
        else:
            string_final += c

    return primeiro_caracter+string_final"""


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
    test(fix_start, 'babble', 'ba**le')
    test(fix_start, 'aardvark', 'a*rdv*rk')
    test(fix_start, 'google', 'goo*le')
    test(fix_start, 'donut', 'donut')
