'''Escreva um programa que contenha uma função que receba um número
representando uma temperatura em graus Fahrenheit e calcule e imprima
a temperatura em Celsius. Obs: C=(5/9)*(F-32).'''

def celsius(fahrenheit):
    return (5/9)*(fahrenheit-32)

print(celsius(212), "Cº")