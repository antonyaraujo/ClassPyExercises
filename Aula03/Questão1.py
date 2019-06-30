'''
Escreva um programa que leia o peso e a altura de uma pessoa.
Em seguida o programa deve calcular e imprimir índice de
massa corpórea (IMC) dessa pessoa. Dado:
'''

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe sua altura: "))
print ("Seu IMC é: ", (peso/(altura ** 2)))