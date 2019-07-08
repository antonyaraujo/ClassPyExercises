# Faça um programa que leia uma quantidade não determinada de números inteiros. Calcule a
# quantidade de números positivos e negativos. O número que encerrará a leitura será zero.

positivos, negativos = 0, 0
num = int(input("Informe um número: "))
while (num != 0):
    if num > 0:
        positivos += 1
    if num < 0:
        negativos += 1
    num = int(input("Informe um número: "))
print("Positivos: %i" %positivos)
print("Negativos: %i" %negativos)
