# Uma empresa quer dar uma bonificação para determinados funcionários. Deverão receber
# um bônus de R$ 500,00 no salário os funcionários com mais de 50 anos ou que trabalhem
# na empresa há pelo menos 5 anos. Escreva um programa que leia a idade, o tempo de
# serviço (em anos) e o salário do funcionário e imprima na tela o valor do salário a ser
# recebido.

idade = int(input("Informe a sua idade: \n"))
tempo = int(input("Informe quantos anos vocÊ tem de serviço: \n"))
salario = float(input("Informe o seu salário: \n"))

if ((idade > 50) or (tempo>=5)):
    salario = salario + 500.00

print("Seu salário atual é: %.2f" %salario)