''' Escreva um programa que leia 30 valores inteiros positivos e
armazene-os em uma lista, e calcule e imprima:
• O menor valor da lista;
• A quantidade de elementos da lista que são divisíveis pelo
menor valor.'''

A = []
for i in range(30):
    valor = int(input("Vetor A - Informe o valor %i: " %(i+1)))
    A.append(valor)

menor, contador = A[0], 0
for i in range(30):
    if A[i]<menor:
        menor = A[i]

for i in range(30):
    if A[i]%menor == 0:
        contador += 1

print('O menor valor da lista é:', menor)
print('Há:', contador, 'números divisíveis por', menor)