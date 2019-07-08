# Faça um programa que leia 10 valores, um de cada vez, e calcule a média, mostrando o resultado ao
# final.

soma = 0
for i in range(10):
    numero = float(input("Informe um valor: \n"))
    soma += numero

print("A média é: %.2f" %(soma/10))