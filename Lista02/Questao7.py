# Faça um programa que leia um número correspondente a um mês do ano e informe o
# nome do mês ou se o número é inválido (não corresponde a um mês).

mes = int(input("Informe um número de um mês: "))
if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Não corresponde a um mês do ano, segundo o calendário solar (juliano/gregoriano)")
