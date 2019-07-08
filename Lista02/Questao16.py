# Fazer um programa que leia a altura em metros e o sexo de uma pessoa (masculino ou
# feminino), e calcule e mostre o peso ideal, utilizando as seguintes fórmulas:
# • Para homens: (72.7 * altura) - 58
# • Para mulheres: (62.1 * altura) - 44.7

altura = float(input("Informe a sua altura: \n"))
sexo = input("Informe o seu sexo (M ou F): \n")

if (sexo == 'M' or sexo == "m" or sexo == "masculino" or sexo == "Masculino"):
    print("O seu peso ideal é de %.2f" %((72.7*altura)-58))
else:
    print("O seu peso ideal é de %.2f" %((62.1 * altura) - 44.7))