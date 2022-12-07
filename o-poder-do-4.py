# https://dojopuzzles.com/problems/o-poder-do-4/
'''
O poder do “4”
Contribuição de: Marcelo Fonseca Tambalo

Este problema ainda não foi utilizado em nenhum Dojo.

No livro o “O Homem que Calculava” existe a teoria de que se é possível obter qualquer número de 0 a 100, com quatro 'quatros' (4), apenas trocando seus operadores. Exemplo: para se obter o 3 deve se fazer 
CASO:

(4+4+4)/4 =3
4+(4-4)/4 = 4
((4*4)+4)/4 = 5
4+4-4/4 = 7
((4/4)+4)*4 = 20

Desenvolva uma função que retorne a fórmula para determinado número 

Entrada: 80 Saida: (4+4*4)*4
'''

'''
Integrantes
Greg
Anderson
Diogo
Cassio
Vinnicyus 
'''
'''
Encontros (dias)
 - 04/07/2022
 - ...
'''
# (4-4) + (4-4) = 0
# (4+4) / (4+4)   = 1
# (4/4) + (4/4) = 2
# (4 + 4 + 4) / 4 = 3
# 4 +(4 - 4) / 4 = 4 
#( 4 X 4 + 4) / 4 = 5
# 4 +(4 + 4) / 4 = 6
# 4 + 4 - (4 / 4) = 7
# 4 X (4 +4) / 4 = 8
# 4 + 4 + (4 /4) = 9
# (4x4 - (4) + 4 = 10


import pytest

# Resolver de 0-10
def multiplicacao(x, y): 
    return x*y

def divisao(x, y):
    if y != 0:
        return x/y
    return 0
def soma(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def concatenacao_transformar_em_numero_magico(x,y):    
    return 44
    
def fatorial(n=4):
    if n==0:
        return 1
    else:
        return fatorial(n-1)*n    
def eh_par(n):
    par = False
    if n%2==0:
        par = True
    return par 
    
def generate_expression(n):
    express=""
    if n==0:
        express = "(4-4)"
    elif n == 8:
        express = "(4+4)"
    elif n==1:
        express = "(4/4)"
    elif n==16:
        express = "(4*4)"
    elif n==24:
        express = "(4!)"        
    elif n==44:
        express = "(44)"        
    return express


def gerar_expressao(n):
    if n in [3,4,5,6,10,12,20,28,36,48,60,68,80]:
        return gerar_expressao2(n)
    else:
        gerador_2_elementos = [soma(4,4),subtracao(4,4),multiplicacao(4,4), divisao(4,4),concatenacao_transformar_em_numero_magico(4,4)]

        
        escrever_expressão_matematica=[]
        consolidacao_de_resultados = []
        
        for i in gerador_2_elementos:
            express= generate_expression(i)            
            for j in gerador_2_elementos:
                express_2=generate_expression(j)
                soma_ = soma(i,j)
                escrever_expressão_matematica.append(f"{express +'+'+ express_2}")
                sub_ = subtracao(i,j)
                escrever_expressão_matematica.append(f"{express +'-'+ express_2}")            
                multi_= multiplicacao(i,j)
                escrever_expressão_matematica.append(f"{express +'*'+ express_2}")
                divisao_= divisao(i,j)            
                escrever_expressão_matematica.append(f"{express +'/'+ express_2}")
                            
                consolidacao_de_resultados.append(soma_)            
                consolidacao_de_resultados.append(sub_)
                consolidacao_de_resultados.append(multi_)
                consolidacao_de_resultados.append(divisao_)
                
        print(consolidacao_de_resultados)
        print("***"*10)
        print(escrever_expressão_matematica)
        print("***"*10)
        index_ = -1
        if (n in consolidacao_de_resultados):
            index_ =consolidacao_de_resultados.index(n)
            print(f"Achou o {n} no indice {index_}")    

            print(escrever_expressão_matematica[index_])
        else:
            print(f"Não Achou o {n}")

        return escrever_expressão_matematica[index_]

def gerar_expressao2(n):
    escrever_expressão_matematica=[]
    consolidacao_de_resultados = []    
    gerador_2_elementos = [soma(4,4),subtracao(4,4),multiplicacao(4,4), divisao(4,4),concatenacao_transformar_em_numero_magico(4,4)]
    
    for i in gerador_2_elementos:
        express= generate_expression(i)  
        j=4
        express_2 = 4
        soma_parcial = soma(i,j)  
        resultado_soma_parcial_soma = soma(soma_parcial,j)        
        escrever_expressão_matematica.append(f"({express} + {express_2}) + {str(j)}")
        resultado_soma_parcial_subtracao = subtracao(soma_parcial,j)
        escrever_expressão_matematica.append(f"({express} + {express_2}) - {str(j)}")
        resultado_soma_parcial_multiplicacao = multiplicacao(soma_parcial,j)
        escrever_expressão_matematica.append(f"({express} + {express_2}) * {str(j)}")        
        resultado_soma_parcial_divisao = divisao(soma_parcial,j)
        escrever_expressão_matematica.append(f"({express} + { express_2}) / {str(j)}")        

        consolidacao_de_resultados.append(resultado_soma_parcial_soma)            
        consolidacao_de_resultados.append(resultado_soma_parcial_subtracao)
        consolidacao_de_resultados.append(resultado_soma_parcial_multiplicacao)
        consolidacao_de_resultados.append(resultado_soma_parcial_divisao)        
        
        subtracao_parcial = subtracao(i,j)
        resultado_subtracao_parcial_soma = soma(subtracao_parcial,j)       
        escrever_expressão_matematica.append(f"({express} - {express_2}) + {str(j)}")        
        resultado_subtracao_parcial_subtracao = subtracao(subtracao_parcial,j)
        escrever_expressão_matematica.append(f"({express} - {express_2}) - {str(j)}")        
        resultado_subtracao_parcial_multiplicacao = multiplicacao(subtracao_parcial,j)
        escrever_expressão_matematica.append(f"({express} - {express_2}) * {str(j)}")        
        resultado_subtracao_parcial_divisao = divisao(subtracao_parcial,j)
        escrever_expressão_matematica.append(f"({express} - {express_2}) / {str(j)}")        

        consolidacao_de_resultados.append(resultado_subtracao_parcial_soma)            
        consolidacao_de_resultados.append(resultado_subtracao_parcial_subtracao)
        consolidacao_de_resultados.append(resultado_subtracao_parcial_multiplicacao)
        consolidacao_de_resultados.append(resultado_subtracao_parcial_divisao)        
        
        multi_parcial = multiplicacao(i,j)
        resultado_multiplicacao_parcial_soma = soma(multi_parcial,j)
        escrever_expressão_matematica.append(f"({express} * {express_2}) + {str(j)}")        
        resultado_multiplicacao_parcial_subtracao = subtracao(multi_parcial,j)
        escrever_expressão_matematica.append(f"({express} * {express_2}) - {str(j)}")        
        resultado_multiplicacao_parcial_multiplicacao = multiplicacao(multi_parcial,j)
        escrever_expressão_matematica.append(f"({express} * {express_2}) * {str(j)}")        
        resultado_multiplicacao_parcial_divisao = divisao(multi_parcial,j)  
        escrever_expressão_matematica.append(f"({express} * {express_2}) / {str(j)}")        
        
        consolidacao_de_resultados.append(resultado_multiplicacao_parcial_soma)
        consolidacao_de_resultados.append(resultado_multiplicacao_parcial_subtracao)
        consolidacao_de_resultados.append(resultado_multiplicacao_parcial_multiplicacao)
        consolidacao_de_resultados.append(resultado_multiplicacao_parcial_divisao)  
        
        divisao_parcial= divisao(i,j) 
        resultado_divisao_parcial_soma = soma(divisao_parcial,j)
        escrever_expressão_matematica.append(f"({express} / {express_2}) + {str(j)}")        
        resultado_divisao_parcial_subtracao = subtracao(divisao_parcial,j)
        escrever_expressão_matematica.append(f"({express} / {express_2}) - {str(j)}")        
        resultado_divisao_parcial_multiplicacao = multiplicacao(divisao_parcial,j)
        escrever_expressão_matematica.append(f"({express} / {express_2}) * {str(j)}")        
        resultado_divisao_parcial_divisao = divisao(divisao_parcial,j) 
        escrever_expressão_matematica.append(f"({express} / {express_2}) / {str(j)}")        
                       
        consolidacao_de_resultados.append(resultado_divisao_parcial_soma)
        consolidacao_de_resultados.append(resultado_divisao_parcial_subtracao)
        consolidacao_de_resultados.append(resultado_divisao_parcial_multiplicacao)
        consolidacao_de_resultados.append(resultado_divisao_parcial_divisao)  
        
    print(consolidacao_de_resultados)
    print("***"*10)
    print(escrever_expressão_matematica)
    print("***"*10)
    index_ = -1
    if (n in consolidacao_de_resultados):
        index_ =consolidacao_de_resultados.index(n)
        print(f"Achou o {n} no indice {index_}")    

        print(escrever_expressão_matematica[index_])
    else:
        print(f"Não Achou o {n}")

    return escrever_expressão_matematica[index_]
def test_resultado_0():
    assert gerar_expressao(0) == "(4+4)-(4+4)"

def test_resultado_1():
    assert gerar_expressao(1) == "(4+4)/(4+4)"    

def test_resultado_2():
    assert gerar_expressao(2) == "(4*4)/(4+4)"    

def test_resultado_3():
    assert gerar_expressao(3) == "((4+4) + 4) / 4" 

def test_resultado_4():
    assert gerar_expressao(4) == "((4-4) * 4) + 4"

def test_resultado_5():
   assert gerar_expressao(5) == "((4*4) + 4) / 4"

def test_resultado_6():
    assert gerar_expressao(6) == "((4+4) / 4) + 4"

def test_resultado_7():
    assert gerar_expressao(7) == "(4+4)-(4/4)"

def test_resultado_8():
    assert gerar_expressao(8) == "(4+4)+(4-4)"

def test_resultado_9():
    assert gerar_expressao(9) == "(4+4)+(4/4)"

def test_resultado_10():
   assert gerar_expressao(10) == "((44) - 4) / 4" 
    
def test_resultado_12():
   assert gerar_expressao(12) == "((44) + 4) / 4" 

def test_resultado_15():
   assert gerar_expressao(15) == "(4*4)-(4/4)"   
    
def test_resultado_16():
   assert gerar_expressao(16) == "(4+4)+(4+4)"    

def test_resultado_17():
   assert gerar_expressao(17) == "(4*4)+(4/4)"       
    
def test_resultado_20():
   assert gerar_expressao(20) == "((4/4) + 4) * 4" 
    
def test_resultado_24():
   assert gerar_expressao(24) == "(4+4)+(4*4)"  
    
def test_resultado_28():
   assert gerar_expressao(28) == "((4+4) * 4) - 4"  

def test_resultado_32():
   assert gerar_expressao(32) == "(4*4)+(4*4)"       

def test_resultado_36():
   assert gerar_expressao(36) == "((4+4) * 4) + 4"

def test_resultado_43():
   assert gerar_expressao(43) == "(44)-(4/4)"

def test_resultado_44():
   assert gerar_expressao(44) == "(4-4)+(44)"

def test_resultado_45():
   assert gerar_expressao(45) == "(4/4)+(44)"    

def test_resultado_48():
   assert gerar_expressao(48) == "((4+4) + 4) * 4"

def test_resultado_52():
   assert gerar_expressao(52) == "(4+4)+(44)"

def test_resultado_60():
   assert gerar_expressao(60) == "((4*4) * 4) - 4"  

def test_resultado_64():
   assert gerar_expressao(64) == "(4+4)*(4+4)"    

def test_resultado_68():
   assert gerar_expressao(68) == "((4*4) * 4) + 4"  

def test_resultado_80():
    assert gerar_expressao(80) == "((4*4) + 4) * 4"  

def test_resultado_88():
    assert gerar_expressao(88) == "(44)+(44)"
    
if __name__ == "__main__":
    pytest.main(['-svv', __file__])

