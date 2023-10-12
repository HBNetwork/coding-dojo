"""
### Print Errors

Em uma fábrica, uma impressora imprime etiquetas para caixas. Para um tipo de caixa, a impressora deve usar cores que, para simplificar, são nomeadas com letras de a a m.

As cores usadas pela impressora são registradas em uma string de controle. Por exemplo, uma string de controle "boa" seria aaabbbbhaijjjm, o que significa que a impressora usou três vezes a cor a, quatro vezes a cor b, uma vez a cor h e uma vez a cor a...

Às vezes, há problemas: falta de cores, mau funcionamento técnico e uma sequência de controle "ruim" é produzida, por exemplo. aaaxbbbbyyhwawiwjjjwwm com letras que não vão de a até m.

Você tem que escrever uma função printer_error que, dada uma string, retornará a taxa de erro da impressora como uma string representando um racional cujo numerador é o número de erros e o denominador o comprimento da string de controle. Não reduza esta fração a uma expressão mais simples.

A string tem um comprimento maior ou igual a um e contém apenas letras de a a z.

### Exemplo: 


```
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
`printer_error(s) => "8/22"

Participante:
- João Moreno
- MConrado
- Fred
- Àlisson


"""

import pytest

def printerror(etiqueta):
    count = 0
    total = len(etiqueta)
    for caracter in etiqueta:
        if caracter > 'm':
            count += 1
    return f"{count}/{total}"
            

def test_printerror():
  assert printerror("aaabbbbhaijjjm") == "0/14"
  assert printerror("aaaxbbbbyyhwawiwjjjwwm")== "8/22"

if __name__ == "__main__":
  pytest.main(['-svv', __file__])
    

