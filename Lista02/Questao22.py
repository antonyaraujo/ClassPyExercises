# Escreva um programa que calcula um reajuste salarial, de acordo com as regras a seguir:
# o Se o salário for menor que R$ 500,00 então o reajuste é de 15%
# o Se o salário estiver entre R$ 500,00 e R$ 1.000,00 então o reajuste é de 8%
# o Se o salário for superior R$ 1.000,00 então o reajuste é de 3%

salario = float(input("Informe o seu salário: \n"))
if (salario < 500):
    salario *= 1.15
elif 500 <= salario <= 1000:
    salario*=1.08
else:
    salario*=1.03

print("Seu salário reajustado é de R$%.2f" %(salario))