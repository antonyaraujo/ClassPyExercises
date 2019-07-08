# Faça um programa que leia 10 valores, um de cada vez, e apresente o maior deles ao final.

maior = 0
for i in range(10):
    numero = float(input("Informe o valor %i: " %(i+1)))
    if numero > maior:
        maior = numero

print("O maior valor foi %.2f" %maior)