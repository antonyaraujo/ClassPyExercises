# Escreva um programa que leia o salário de uma pessoa, a quantidade de contas (despesas) que uma
# pessoa precisa pagar em um mês e, para cada conta, leia o valor a ser pago. O programa deve somar
# todos os valores de contas que a pessoa necessita pagar e depois verificar se a diferença entre o
# salário da pessoa e o valor de todas as despesas que deve pagar no mês é positiva. Se a diferença
# (salário – despesas) for positiva imprimir este valor da diferença na tela. Se a diferença for negativa
# imprimir a mensagem “reduzir despesas”.

salario = float(input("Informe o seu salário: "))
qt_contas = int(input("Informe a quantidade de contas a serem pagas: "))

for i in range(qt_contas):
    despesa = float(input("Informe o valor da conta %i: " %(i+1)))
    salario = salario - despesa

if salario > 0:
    print("O saldo restante é  R$%.2f" %(salario))
else:
    print("Você deve reduzir despesas")