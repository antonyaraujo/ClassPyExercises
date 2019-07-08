# Fazer um programa que leia um valor n e calcule e mostre o resultado da soma dos n primeiros
# termos da serie abaixo:

N = int(input("Insira o valor de N: "))

c, soma = 1, 0
while (c <= N):
    soma += N / (2*N)
    c += 1
print("A soma dos n primeiros termos da série de N é: %.2f" %(soma))
