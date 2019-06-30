'''Faça um programa que leia uma quantidade não determinada de números
positivos. Calcule a média dos valores pares, a média de valores ímpares
e a média geral dos números lidos. A leitura encerrará quando for
digitado um valor menor ou igual a zero.'''

pares, somaPar, impares, somaImpar = 0, 0, 0, 0

numero = float(input("Informe um valor positivo: "))
while (numero > 0):
    if (numero % 2 == 0):
        pares += 1
        somaPar += numero
    else:
        impares += 1
        somaImpar += numero
    numero = float(input("Informe um valor positivo: "))

print("A média dos valores pares foi de: %.2f" %(somaPar/pares))
print("A média dos valores ímpares foi de: %.2f" %(somaImpar/impares))
print("A média de todos os valores foi de: %.2f" %((somaPar+somaImpar)/(pares+impares)))