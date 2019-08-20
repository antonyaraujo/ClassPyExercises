''' Escreva um programa que contenha um único procedimento que calcula
a soma, a diferença e o produto entre dois números inteiros. A leitura
dos dois inteiros e a impressão dos resultados devem ser feitas pelo
programa principal. '''

def calculadora(n1, n2, operacao):
    if operacao == "+":
        print("%i + %i = %i" %(n1, n2, n1+n2))
    elif operacao == "-":
        print("%i - %i = %i" % (n1, n2, n1 - n2))
    elif operacao == "x" or operacao == "*":
        print("%i x %i = %i" % (n1, n2, n1 * n2))

n1 = int(input("Operando 1: "))
operacao = (input("Operação: "))
n2 = int(input("Operando 2: "))
calculadora(n1, n2, operacao)