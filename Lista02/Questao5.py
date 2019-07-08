# Faça um programa que leia 4 números positivos e imprima o menor deles. Use somente duas variáveis

numero = -1
while numero < 0:
    numero = float(input("Informe um número: "))
    menor = numero

numero = -1
while numero < 0:
    numero = float(input("Informe um número: "))
    if numero < menor:
        menor = numero

numero = -1
while numero < 0:
    numero = float(input("Informe um número: "))
    if numero < menor:
        menor = numero

numero = -1
while numero < 0:
    numero = float(input("Informe um número: "))
    if numero < menor:
        menor = numero

print("O menor número é %f" %menor)