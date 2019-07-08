# Uma empresa possui um esquema de pontuação que determina o valor de um bônus.
# Essa pontuação é dada através da seguinte fórmula:
# Pontos = Horas extras – 2/3 * Faltas
# Escreva um algoritmo/programa que leia de um empregado, as horas extras trabalhadas e
# as horas de faltas e determine o bônus que é dado pela seguinte tabela:

horas_extras = int(input("Informe a quantidade de horas extras trabalhadas: \n"))
horas_faltas = int(input("Informe a quantidade de horas de faltas: \n"))
pontos = horas_extras - (2/3*horas_faltas)

if pontos > 40:
    print("Seu bônus é de R$5.000,00")
elif 30 < pontos <= 40:
    print("Seu bônus é de R$4.000,00")
elif 20 < pontos <= 30:
    print("Seu bônus é de R$3.000,00")
elif 10 < pontos <= 20:
    print("Seu bônus é de R$2.000,00")
else:
    print("Seu bônus é de R$1.000,00")