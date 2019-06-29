'''
João recebeu seu salário e precisa pagar duas contas que estão
atrasadas. João deverá pagar de multa 2% do valor de cada conta.
Escreva um algoritmo que leia o valor do salário de João e o valor
de cada uma das contas, calcule e mostre na tela quanto restará do
salário de João.
'''

salario = float(input("João, informe seu salário: "))
conta1 = float(input("João, informe o valor da conta 1: "))
conta2 = float(input("João, informe o valor da conta 2: "))
print("\nO valor restante do salário é de: %.2f" %(salario -((conta1*1.02)+(conta2*1.02))))