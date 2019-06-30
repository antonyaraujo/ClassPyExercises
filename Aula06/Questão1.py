import math
'''Escreva um programa que calcule e apresente na tela a área de cada
círculo através da fórmula A = PI * R ** 2, onde R (o valor que deverá
ser digitado pelo usuário) representa o raio do círculo e PI é o número
3,14. Repetir o processo enquanto for digitado um valor de R maior que
0.'''

r = float(input("Informe o valor do raio: "))
while (r > 0):
    a = math.pi * r ** 2
    print("A área do círculo de raio %.2f é de: %.2f" %(r, a))
    r = float(input("Informe o valor do raio: "))