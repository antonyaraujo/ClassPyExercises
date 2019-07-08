# Escreva um programa para calcular o salário semanal de uma pessoa, determinado pelas
# seguintes condições. Se o número de horas trabalhadas for menor ou igual a 40, a pessoa
# recebe 8 reais por hora trabalhada, se não a pessoa recebe 320 reais fixos e mais 12 reais
# para cada hora trabalhada que excede 40 horas. (Exemplo: uma pessoa que trabalha 42
# horas deve receber 344 reais). Seu programa deve ler o número de horas trabalhadas e
# deve imprimir na tela o salário semanal.

horas = int(input("Informe o número de horas trabalhadas: \n"))
if (horas <= 40):
    salario = 8 * horas
else:
    salario = 320 + 12*(horas-40)

print("Seu salário semanal é de R$", salario)