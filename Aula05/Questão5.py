'''Em São Paulo, durante um determinado intervalo de horários, veículos
cuja placa termina em:

    1 ou 2: Não podem trafegar na segunda-feira;

    3 ou 4: Não podem trafegar na terça-feira;

    5 ou 6: Não podem trafegar na quarta-feira;

    7 ou 8: Não podem trafegar na quinta-feira;

    9 ou 0: Não podem trafegar na sexta-feira;

Escreva um programa que leia a parte numérica da placa de um carro e
imprima uma mensagem adequada informando qual o dia da semana em
que o veículo não pode circular.'''

placa = int(input("Informe a parte numérica da placa do carro: ")[3])
# outra solução: placa =  placa / 1 % 10
print("último dígito da placa é: %i" %placa)
if (0 < placa < 3):
    print("Não podem trafegar na segunda-feira")
elif (2 < placa < 5):
    print("Não podem trafegar na terça-feira")
elif (4 < placa < 7):
    print("Não podem trafegar na quarta-feira")
elif (6 < placa < 9):
    print("Não podem trafegar na quinta-feira")
else:
    print("Não podem trafegar na sexta-feira")