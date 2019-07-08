import math
# Escreva um programa que calcule e apresente na tela a área de cada círculo através da fórmula A =
# PI * R * R, onde R (o valor que deverá ser digitado pelo usuário) representa o raio do círculo e PI é o
# número 3,14. Repetir o processo enquanto R for maior que 0.

R = float(input("Informe o valor do raio: "))
while (R > 0):
    A = math.pi * R * R
    print("A área do círculo é A = %.2f" %(A))
    R = float(input("Informe o valor do raio: "))