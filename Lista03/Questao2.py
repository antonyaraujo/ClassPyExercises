# Faça um programa que mostre uma tabela de conversão de graus fahrenheit para centígrados para
# todos valores inteiros de 32 a 80 farenheit, mostrando o valor em centígrados e ao lado o valor em
# fahrenheit. A conversão de graus fahrenheit para centígrados é obtida por fahrenheit=
# (9*centígrados/5)+32.

print("   Fº ------ Cº")
for f in range(32, 81):
    c = (f - 32) / 1.8000
    print(" %.2fCº -- %.dFº" %(c, f))

