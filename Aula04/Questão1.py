'''Escrever um programa que leia um número inteiro n e calcule e mostre a
tabuada do n. Mostre a tabuada na forma:

1 x n = n

2 x n = 2n

3 x n = 3n

...

10 x n = 10n'''

n = int(input("Informe um valor inteiro n: "))
print("-- Tabuada de %i --" %n)
for i in range(1, 11):
    print("%i x %i = %i" %(i, n, i*n))