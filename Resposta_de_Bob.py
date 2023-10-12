"""
https://exercism.org/tracks/python/exercises/bob

DATA: 07/11/2022 
Instruções
Sua tarefa é determinar o que Bob responderá a alguém quando ele disser algo ou fazer uma pergunta.

Bob só responde uma das cinco coisas:

* "Certo." Esta é a resposta dele se você fizer uma pergunta, como "Como você está?" A convenção usada para perguntas é que termina com um ponto de interrogação.
* "Whoa, relaxe!" Esta é a resposta dele se você gritar com ele. A convenção usada para gritar é TODAS AS LETRAS DE CAPITAL.
* "Acalme-se, eu sei o que estou fazendo!" É o que ele diz se você gritar uma pergunta para ele.
* "Bem. Seja assim!" É assim que ele responde ao silêncio. A convenção usada para o silêncio não é nada, ou várias combinações de caracteres de espaço em branco.
* "Tanto faz." É isso que ele responde a qualquer outra coisa.

PARTICIPANTES:
- João M.
- Fredinhuuu (yamete kudasai)?
- Greg
- M.conrado
- Adailton
- Lucas
- Eventinho IA
-


"""

import pytest


def pergunta(entrada):
    entrada = entrada.rstrip('')
    eh_pergunta = entrada.endswith("?")
    eh_maiuscula = entrada.isupper()
    eh_vazio = entrada.isspace() or len(entrada) == 0
    resposta = "Tanto faz"
    
    if eh_pergunta:
        resposta = "Certo"
        
    if eh_maiuscula and eh_pergunta:
            resposta = "Acalme-se, eu sei o que estou fazendo!"
        
    elif eh_maiuscula:
        resposta = "Whoa, relaxe!"
        
    elif eh_vazio:
        resposta = "Bem. Seja assim!"
      
    return resposta


def test_pergunta():
    assert pergunta("como vc está?") == "Certo"
    assert pergunta("eae?") == "Certo"
    assert pergunta("?eae") == "Tanto faz"
    assert pergunta("AAA") == "Whoa, relaxe!"
    assert pergunta("aaa") == "Tanto faz"
    assert pergunta("AAA?") == "Acalme-se, eu sei o que estou fazendo!"
    assert pergunta(" ") == "Bem. Seja assim!"
    assert pergunta("") == "Bem. Seja assim!"
    assert pergunta("    ") == "Bem. Seja assim!"
    assert pergunta("aNiMal") == "Tanto faz"
    assert pergunta("?") == "Certo"
    assert pergunta("2+2=5?") == "Certo"
    assert pergunta("2+2=5") == "Tanto faz"


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
