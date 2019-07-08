# Escreva um programa que imprime a soma de todos os números inteiros entre A e B (incluindo A e
# B), onde A e B são fornecidos pelo usuário.

A = int(input("Informe A: "))
B = int(input("Informe B: "))
soma = 0
for i in range(A, B+1):
    soma+= i
print("A soma dos valores nesse intervalo fechado é: ", soma)