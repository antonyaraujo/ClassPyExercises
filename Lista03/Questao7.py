import math
# Escreva um programa que imprime todos os números primos entre 1 e n, onde n é fornecido pelo
# usuário.

n = int(input("Informe o número: "))
i = 2

while (i < n):
    j = 1
    div = 0
    while (j < n):
        # é divisível?
        if ((i % j) == 0):
            div += 1
        j += 1
    if (div <= 2):
        print(i)
    i += 1