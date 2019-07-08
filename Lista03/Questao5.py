# Escreva um programa que lê uma sequência de números inteiros e imprime qual o maior e qual o
# menor valor dessa seqüência. A seqüência termina com o número 0 (zero)

numero = 1
numero = int(input("Informe o valor inteiro: "))
maior = numero
menor = numero
while (numero != 0):
    if (numero > maior):
        maior = numero
    if (numero < menor):
        menor = numero
    numero = int(input("Informe o valor interior: "))

print("O maior valor é: %i" %(maior))
print("O menor valor é: %i" %(menor))