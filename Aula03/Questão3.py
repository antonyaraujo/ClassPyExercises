''' Escreva um programa que calcule o valor do desconto de uma
mercadoria paga a vista e o valor total a ser pago. O programa deve
ler o valor da mercadoria e a porcentagem do desconto. Depois o
programa deve calcular e imprimir na tela o valor do desconto e o
novo valor da mercadoria com o desconto.'''

mercadoria = float(input("Informe o valor da mercadoria: "))
desconto = float(input("Informe a porcentagem do desconto: "))
valorDesconto = mercadoria * (desconto/100)
print("O valor do desconto é: R$%.2f" %(valorDesconto))
print("O valor da mercadoria com o desconto é: R$%.2f" %(mercadoria - valorDesconto))
