"""
https://dojopuzzles.com/problems/contando-linhas-de-codigo/

Contando linhas de código

Desenvolva um utilitário que conte o número de linhas de código efetivo em um arquivo-fonte em Java. Considere uma linha se ela não contiver apenas caracteres em branco ou texto dentro de comentários. Alguns exemplos:

  -   // This file contains 3 lines of code
  1   public interface Dave {
  -     /**
  -      * count the number of lines in a file
  -      */
  2     int countLines(File inFile); // not the real signature!
  3   }

 Comentários dentro de string Java devem ser ignorados.

"""
"""Integrantes:
Cassio
Diogo 
Marcelo
Breno

27/07/2022
03/08/2022
"""
import pytest

def asteriscoFinal(linha, it):
    while '*/' not in linha:
        linha = next(it)
    
def count(code):
    retorno = 0
    code_split = code.split("\n")
    inicio_comentario = '/*'

    it = iter(code_split)
    for linha in it:
        linha = linha.strip()
        if linha.startswith(inicio_comentario):
            asteriscoFinal(linha, it)
            continue
        if inicio_comentario in linha:
            if not linha.startswith(inicio_comentario):
                if ";" in linha or "{" in linha or "}" in linha:
                    retorno += 1    
                asteriscoFinal(linha, it)
            continue        
        
        if linha and not linha.startswith('//') : # and not linha.startswith('/*') and not linha.startswith('*') and not linha.startswith('*/'):  # Remove linhas em branco ( ou só com espaços)
            print(linha)
            retorno += 1
            
    return retorno

def test_code_comment():
    codigo_teste = """
  /**
 ** Exemplo de uma classe simples em Java.
  isso também é um comentário
 */
public class PrimeiraClasse {
    public static void main(String[] args) {
        System.out.println("Hello world !!!");
    }
}
    """
    assert count(codigo_teste) == 5

def test_code_onelinecomment():
    codigo_teste = """
  // Exemplo de uma classe simples em Java.

public class PrimeiraClasse {
    public static void main(String[] args) {
        System.out.println("Hello world !!!");
    }
}
    """
    assert count(codigo_teste) == 5

def test_code_twolinecomment():
    codigo_teste = """
  // Exemplo de uma classe simples em Java.

public class PrimeiraClasse {
    public static void main(String[] args) {
        System.out.println("Hello world !!!");
    }
}
 // Exemplo de uma classe simples em Java.
    """
    assert count(codigo_teste) == 5    

def test_code_comments_interno():
    codigo_teste = """
public class PrimeiraClasse {

    public static void main(String[] args) {
        System.out.println("Hello world !!!");
        // TESTE AQUI
    }
}
    """
    assert count(codigo_teste) == 5

"""
Problema: Quando o comentário de bloco vier no meio da linha de código, considerar testes de implementação.
Pensar numa solução.
"""
def test_code_comments_string_block():
    codigo_teste = """
public class PrimeiraClasse {

    public static void main(String[] args) {
        String var = "//Isso não é um comentário";
        int mult = 1 * 2; /* isso também não é comentário
        System.out.println("Hello world !!!");
  */
    }
}
    """
    assert count(codigo_teste) == 6


def test_code_comments_interno_block():
    codigo_teste = """
public class PrimeiraClasse {

    public static void main(String[] args) {
        System.out.println("Hello world !!!");
  /**
 ** Exemplo de uma classe simples em Java.
  isso também é um comentário
 */
    }
}
    """
    assert count(codigo_teste) == 5    
    
def test_code_no_comments():
    codigo_teste = """
public class PrimeiraClasse {

    public static void main(String[] args) {
        System.out.println("Hello world !!!");
    }
}
    """
    assert count(codigo_teste) == 5


def test_code_hello_com_comentarios_no_println():
    codigo_teste = """
public class Hello {
  public static final void main(String [] args) { // gotta love Java
  // Say hello
          System./*wait*/out./*for*/println/*it*/("Hello/*");
        }
  
    }
    """
    assert count(codigo_teste) == 5
def test_code_hello_com_comentarios_no_println2():
    codigo_teste = """
public class Hello {
  public static final void main(String [] args) { // gotta love Java
  // Say hello
          System.out.println("Hello")/*System.out.println("Hello");*/;
        }
  
    }

    
    """
    assert count(codigo_teste) == 5


def test_code_hello_com_comentarios_no_println3():
    codigo_teste = """
public class Hello {
  public static final void main(String [] args) { // gotta love Java
  //*/* // Say hello
          System.out.println("Hello")/*System.out.println("Hello");*/; */
        }
  
    }

    
    """
    assert count(codigo_teste) == 5

if __name__ == "__main__":
    pytest.main(['-svv', __file__])
  