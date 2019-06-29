''' Um funcionário recebe um salário fixo mais 4% de comissão sobre
as vendas. Escreva um algoritmo que leia o valor do salário fixo de
um funcionário e o valor de suas vendas, calcule e mostre na tela a
comissão e o salário final do funcionário. '''


salarioBase = float(input("Informe o seu salário base: \n"))
valor = float(input("\nInsira o valor das suas vendas: \n"))

comissao = valor * (0.04)

print("\nO valor da sua comissão é: ", comissao)
print("O seu salário total é: ", (comissao + salarioBase))