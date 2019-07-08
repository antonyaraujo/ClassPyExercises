# Elabore um programa de cálculo de troco no caixa. O programa deve ler o valor a ser
# cobrado e a quantidade em dinheiro recebida, fornecendo como resposta o valor do troco
# ou uma mensagem com os seguintes dizeres “O dinheiro não é suficiente”.

valorCobrado = float(input("Informe o valor a ser cobrado: \n"))
quantidade = float(input("Informe a quantidade em dinheiro recebida: \n"))

if (quantidade > valorCobrado):
    print("O troco é de R$ %.2f" %(quantidade-valorCobrado))
else:
    print("O dinheiro não é suficiente")