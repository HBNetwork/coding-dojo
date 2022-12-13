"""
06. not_bad
Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.
Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'

1 - Conrado
2 - Everton
3 - Luiz Carlos 
4 - Cássio Augusto
5 - Greg
6 - Leonardo
7 - Aldemir
"""

import re


def not_bad(s):
  first_not = s.find('not')
  first_bad = s[first_not:].find('bad') + first_not

  if first_bad > first_not:
    s = s.replace(s[first_not:first_bad + 3], 'good', 1)
  return s


def not_bad_with_sorted(s: str) -> str:
  if 'bad' not in s:
    return s
  final_not = None
  final_bad = None
  all_not = sorted([i for i in range(len(s)) if s.startswith('not', i)])
  all_bad = sorted([i for i in range(len(s)) if s.startswith('bad', i)])
  for bad in all_bad:
    for x in range(len(all_not)):
      if all_not[x] < bad:
        final_not = all_not[x]
        final_bad = bad
        continue
      else:
        if final_bad:
          break
  if not final_bad:
    for notv in all_not:
      for x in range(len(all_bad)):
        if all_bad[x] < notv:
          final_not = notv
          final_bad = all_bad[x]
          continue

  if final_bad > final_not:
    s = s.replace(s[final_not:final_bad + 3], 'good', 1)
  return s


def not_bad_with_regex(s):
  # return re.sub(pattern=('not .* bad'), repl='good', string=s, count=1)
  #(?!bad not)
  pattern = 'not.*?bad'
  repl = 'good'

  return re.sub(pattern, repl, s, 1)


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
  test(not_bad, 'This movie is not so bad', 'This movie is good')
  test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
  test(not_bad, 'This tea is not hot', 'This tea is not hot')
  test(not_bad, "It's bad yet not", "It's bad yet not")

  test(not_bad, "not bad not bad", "good not bad")
  test(
    not_bad,
    "Your car is not bad, your house is not bad, but your bank account is terrible",
    "Your car is good, your house is not bad, but your bank account is terrible"
  )

  test(not_bad, "bad not bad", "bad good")
  test(not_bad, "I am a bad boy, but I am not a bad son",
       "I am a bad boy, but I am good son")

  test(not_bad, "not not bad", "good")
  test(not_bad,
       "The magazine said that the game was not great, but it was not bad",
       "The magazine said that the game was good")
  test(not_bad_with_regex, 'This movie is not so bad', 'This movie is good')
  test(not_bad_with_regex, 'This dinner is not that bad!',
       'This dinner is good!')
  test(not_bad_with_regex, 'This tea is not hot', 'This tea is not hot')
  test(not_bad_with_regex, "It's bad yet not", "It's bad yet not")

  test(not_bad_with_regex, "not bad not bad", "good not bad")
  test(
    not_bad_with_regex,
    "Your car is not bad, your house is not bad, but your bank account is terrible",
    "Your car is good, your house is not bad, but your bank account is terrible"
  )

  test(not_bad_with_regex, "bad not bad", "bad good")
  test(not_bad_with_regex, "I am a bad boy, but I am not a bad son",
       "I am a bad boy, but I am good son")

  test(not_bad_with_regex, "not not bad", "good")
  test(not_bad_with_regex,
       "The magazine said that the game was not great, but it was not bad",
       "The magazine said that the game was good")
  test(not_bad_with_regex, 'This movie is not so bad', 'This movie is good')
  test(not_bad_with_regex,
       "The magazine said that the game was not great, but it was not bad",
       "The magazine said that the game was good")

  test(not_bad_with_sorted,
       "The magazine said that the game was not great, but it was not bad",
       "The magazine said that the game was not great, but it was good")
