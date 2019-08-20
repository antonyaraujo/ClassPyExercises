''' Escreva um programa que contenha uma função que receba dois
números e retorne verdadeiro ou falso indicando se o primeiro número é
divisível pelo segundo. A função principal deve imprimir uma
mensagem apropriada de acordo com o resultado da função.'''

def divisivel(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

print(divisivel(4,2))
