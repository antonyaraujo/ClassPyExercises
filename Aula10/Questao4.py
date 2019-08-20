'''Escreva um programa que leia 30 números inteiros e
armazene-os em uma lista A e leia também um inteiro n. Em
seguida seu programa deve procurar o valor n em A e imprimir
a posição em que este aparece. Se o elemento não estiver no
vetor, o programa deve imprimir uma mensagem indicando que
o elemento não pertence ao vetor.'''

def pertencer(A):
    for i in range(30):
        if A[i] == n:
            return ("O elemento %i está na posição %i" % (n, i))
    return "O elemento não pertence ao vetor"

A = []
for i in range(30):
    valor = int(input("Vetor A - Informe o valor %i: " %(i+1)))
    A.append(valor)
n = int(input("Informe um inteiro N: "))
encontrado = pertencer(A)
print(encontrado)


