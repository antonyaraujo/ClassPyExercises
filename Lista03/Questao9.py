# Faça um programa que leia 10 valores, um de cada vez, e conte quantos são positivos, mostrando o
# resultado da contagem ao final.

positivos = 0
for i in range(10):
    numero = float(input("Informe um valor: \n"))
    if (numero > 0):
        positivos += 1

print("Houveram %i números positivos" %positivos)