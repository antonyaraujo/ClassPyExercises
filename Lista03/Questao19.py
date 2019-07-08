# Escreva um programa que leia n números inteiros positivos fornecidos e imprima na tela uma
# mensagem informando se o número é ou não perfeito.
# Obs.: Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao número.
# Ex.: 6 = 1 + 2 + 3.

n = int(input("Informe o valor de n: "))
c = 1
while (c <= n):
    num = int(input("Informe um numero: "))
    soma = 0
    for i in range(1, num):
        if ((num % i) == 0):
            soma+= i
    print(soma)
    if (soma == num):
        print("O número é perfeito!!")
    else:
        print("O número não é perfeito!!")
    c += 1