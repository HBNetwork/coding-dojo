'''
DATA: 04/10/2023

FONTE: https://www.codewars.com/kata/56c30ad8585d9ab99b000c54

ENUNCIADO: Combinar duas strings

Instruções

Sua tarefa é combinar duas strings. Mas considere a regra...

A propósito, você não precisa verificar erros ou valores de entrada incorretos, está tudo bem sem truques ruins, apenas duas strings de entrada e como resultado uma string de saída ;-)...

E aqui está a regra:
Strings de entrada A e B: 
* Para cada caractere na string A troque a caixa de cada ocorrência do mesmo caractere na string B. 
* Em seguida, faça a mesma troca correspondente com as entradas invertidas. 
* Retorna uma única string que consiste na versão alterada de A seguida pela versão alterada de B. 
* Um caractere de A está em B, independentemente de estar em letras maiúsculas ou minúsculas - veja também os casos de teste.
Eu acho que isso é tudo;-)...

Alguns exemplos fáceis:

Entrada: "abc" e "cde" => Saída: "abCCde"
Entrada: "ab" e "aba" => Saída: "aBABA"
Entrada: "abab" e "bababa" => Saída: "ABABbababa"

Mais uma vez para o último exemplo - descrição de KenKamau, veja discurso;-):

a) troque a caixa dos caracteres na string b para cada ocorrência desse caractere na string a
char 'a' ocorre duas vezes na string a, então trocamos todos os 'a' na string b duas vezes. Isso significa que começamos com "bababa" e depois "bAbAbA" => "bababa"
char 'b' ocorre duas vezes na string a e então a string b se move da seguinte forma: comece com "bababa" e depois "BaBaBa" => "bababa"

b) então, troque a caixa dos caracteres na string a para cada ocorrência na string b
char 'a' ocorre 3 vezes na string b. Então, encadeie os casos de troca da seguinte maneira: comece com "abab" então => "AbAb" => "abab" => "AbAb"
char 'b' ocorre 3 vezes na string b. Portanto, faça uma troca da seguinte maneira: comece com "AbAb" e depois => "ABAB" => "AbAb" => "ABAB".

c) mesclar novas strings a e b
retornar "ABABbababa"

Existem alguns testes estáticos no início e muitos testes aleatórios se você enviar sua solução.


PARTICIPANTES:
- MCOnrado
- Greg
- João M.
- Adailtu
- Lucas
- Luciano
- Álisson
- Frederico

'''
import pytest


def verifica_string(str1, str2):
    aux = ''

    for letra1 in str1:
        if letra1 in str2:
            for letra2 in str2:
                if letra1 == letra2:
                    aux += letra2.upper()
                else:
                    aux += letra2.lower()

    return (aux)


'''
def combina_str(str_a, str_b):
    str_processada2 = verifica_string(str_a, str_b)
    str_processada1 = verifica_string(str_b, str_a)
    return str_processada1 + str_processada2
'''

#def test_junta_tudo():
#assert junta_tudo("abc", "cde") == "abCCde"
#assert junta_tudo("ab", "aba") == "aBABA"
#assert junta_tudo("bababa", "abab") == "BABABAabab"

#assert testando_isso("ab", "aba") == "ABA"

# assert verifica_string("abc", "cde") == "Cde"
# assert verifica_string("abab", "bababa") == "bababa"


#SOLUÇÃO ADAILTON
def verifica_string2(str_modelo, str_processar):
    str_processada = ''
    letras_modelo = {}
    print(f'{str_processar} - {str_modelo}', end="\n")

    for letra in str_modelo:
        if letra not in letras_modelo:
            letras_modelo[letra] = str_modelo.count(letra)

    for letra_processar in str_processar:
        if letra_processar in letras_modelo:
            letra_chave = letra_processar
            letra_processada = letra_processar
            i = 1
            while i <= letras_modelo.get(letra_chave):
                if letra_processada.isupper():
                    letra_processada = letra_processada.lower()
                else:
                    letra_processada = letra_processada.upper()
                i += 1

            str_processada += letra_processada

        else:
            str_processada += letra_processar

        print(f'{letra_processar} - {str_processada}')

    print(f'string processada:{str_processada}', end="\n")
    return str_processada


def combina_str(str1, str2):
    str_processada2 = verifica_string2(str1.lower(), str2.lower())
    str_processada1 = verifica_string2(str2.lower(), str1.lower())
    return str_processada1 + str_processada2


#SOLUÇÃO FREDERICO
def modifica_string(str1, str2):
    aux_pass = []
    for letra in str1:
        if letra.lower() not in aux_pass:
            aux_pass.append(letra.lower())
            if letra in str2:
                contagem = str1.count(letra)
                if contagem % 2 == 0:
                    str2 = str2.replace(letra, letra.lower())
                else:
                    str2 = str2.replace(letra, letra.upper())
    return (str2)


def unindo_strings(str1, str2):
    str2_modificada = modifica_string(str1, str2)
    str1_modificada = modifica_string(str2, str1)
    return (str1_modificada + str2_modificada)
##############


def test_combina_str():
    assert combina_str("abc", "cde") == "abCCde"
    assert combina_str("ab", "aba") == "aBABA"
    assert combina_str("abab", "bababa") == "ABABbababa"
    assert combina_str("bab", "abbaba") == "BABAbbAbA"
    assert combina_str("bbacde", "aabbccd") == "bbacDeAAbbCCD"
    assert unindo_strings("abc", "cde") == "abCCde"
    assert unindo_strings("ab", "aba") == "aBABA"
    assert unindo_strings("abab", "bababa") == "ABABbababa"
    assert unindo_strings("bab", "abbaba") == "BABAbbAbA"
    assert unindo_strings("bbacde", "aabbccd") == "bbacDeAAbbCCD"


if __name__ == "__main__":
    pytest.main(['-svv', __file__])

# abc , cde
#    abCCde

# * Para cada caractere na string 1 troque a caixa de cada ocorrência do mesmo caractere na string 2.
# 1     2
# ab,  aba
#      AbA
# -->     ABA
# -----
# ANalisar a segunda string
# 1     2
# ab,  aba
# Ab
# ab
# -->    aB
# ---
# aBABA
