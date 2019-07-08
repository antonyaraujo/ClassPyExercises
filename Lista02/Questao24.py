# Um serviço de entrega em domicílio cobra 4 reais para fazer qualquer entrega mais um
# acréscimo por quilômetro dependente da distância (d) até o local da entrega, de acordo
# com a tabela a seguir
# Escreva um programa que leia a distância em quilômetros da origem até o destino e
# calcule e imprima na tela o valor a ser pago. Por exemplo: se a entrega for a 5 quilômetros
# de distância, a pessoa irá pagar: 4 + 5*0,75 = 7,75.

d = float(input("Informe a distância de origem até o destino: \n"))

if 0 <= d <= 3:
    valor = 4 + d*0.50
elif 3 < d <= 6:
    valor = 4 + d*0.75
else:
    valor = 4 + d*1

print("O valor a ser pago pela entrega: R$%.2f" %(valor))
