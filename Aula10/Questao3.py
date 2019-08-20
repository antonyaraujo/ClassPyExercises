'''Escreva um programa que leia 200 números inteiros e
armazene-os em um vetor V. Em seguida separe os elementos
de V em dois vetores A e B, de forma que o vetor A contenha os
elementos dos índices pares de V e B contenha os elementos
dos índices ímpares de V.'''

V, A, B = [], [], []
for i in range(200):
    valor = int(input("Vetor V - Informe o valor %i: " %(i+1)))
    V.append(valor)

for i in range(200):
    if V[i]%2 == 0:
        A.append(V[i])
    else:
        B.append(V[i])

print(V)
print(A)
print(B)