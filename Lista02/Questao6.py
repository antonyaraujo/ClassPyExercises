# Faça um programa que leia 4 números e informe quantos são maiores que 10. Use somente duas variáveis.

maiores = 0
numero = float(input("Informe um número: "))
if (numero > 10):
    maiores += 1
numero = float(input("Informe um número: "))
if (numero > 10):
    maiores += 1
numero = float(input("Informe um número: "))
if (numero > 10):
    maiores += 1
numero = float(input("Informe um número: "))
if (numero > 10):
    maiores += 1

print("Houveram %i números maiores que 10" %maiores)