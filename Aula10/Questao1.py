'''Escreva um programa que leia 10 números inteiros e os armazene
no vetor A, leia mais 10 números inteiros e os armazene no vetor
B. Depois some o vetor A com o vetor B armazenando no vetor C.
Imprima o vetor C.'''

A, B = [], []
for i in range(10):
    valor = int(input("Vetor A - Informe o valor %i: " %(i+1)))
    A.append(valor)

for i in range(10):
    valor = int(input("Vetor B - Informe o valor %i: " %(i+1)))
    B.append(valor)

C = A+B
print(C)