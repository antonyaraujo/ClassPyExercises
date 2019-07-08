# Mesma coisa da Questão 17
# Escreva um programa que leia dois números inteiros e faça a multiplicação de um número pelo outro
# sem utilizar o operador de multiplicação (*). Imprimir na tela o valor encontrado.

A = int(input("Informe o termo A do produto: "))
B = int(input("Informe o termo B do produto: "))

produto = 0
for i in range(B):
    produto += A

print("%i x %i = %i" %(A, B, produto))