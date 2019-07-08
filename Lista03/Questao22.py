# Uma fábrica tem um vendedor que recebe uma comissão calculada a partir do número de itens de um
# pedido, segundo os seguintes critérios:
# • para pedidos com menos de 20 itens, a comissão é de 10% do valor total do pedido;
# • para pedidos de 20 a 49 itens, a comissão é de 15% do valor total do pedido;
# • para pedidos de 50 a 74 itens, a comissão é de 20% do valor total do pedido;
# • para pedidos iguais ou superiores a 75 itens, a comissão é de 25%.
# Escreva um programa que processe N pedidos vinculados a esse vendedor (N deve ser lido,
# portanto). Para cada pedido o programa deve ler a quantidade de itens vendidos e o valor total. O
# programa deve informar:
# • A soma total das comissões;
# • A média de itens vendidos;
# • Porcentagem de pedidos com menos de 20 itens.

comissao = 0
soma_comissao = 0
soma_itens = 0
pedidos = 0

n = int(input("Informe o valor da quantidade de pedidos: "))
for i in range(n):
    qt_itens = int(input("Informe a quantidade de itens vendidos no pedido %i: " %(i)))
    valor_total = float(input("Informe o valor total do pedido %i: " %(i)))
    if (qt_itens < 20):
        comissao = valor_total * 0.10
        pedidos += 1
    elif (20 <= qt_itens <= 49):
        comissao = valor_total * 0.15
    elif (50 <= qt_itens <= 74):
        comissao = valor_total * 0.20
    else:
        comissao = valor_total * 0.25
    soma_comissao += comissao
    soma_itens += qt_itens

print("A soma total das comissões é de R$%.2f" %(soma_comissao))
print("A média de itens vendidos é de %.2f itens"%(soma_itens/n))
print("A Porcentagem de pedidos com menos de 20 itens é de %.2f itens" %((pedidos / n)*100))