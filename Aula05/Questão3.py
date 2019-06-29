'''A prefeitura de uma cidade abriu uma linha de crédito para os
funcionários estatutários. O valor máximo da prestação não poderá
ultrapassar 30% do salário bruto. Fazer um programa que permita entrar
com o salário bruto e o valor da prestação, e informar se o empréstimo
pode ou não ser concedido.'''

salarioBruto = float(input("Informe o valor do seu salário bruto: "))
valorPrestacao = float(input("Informe o valor da prestação: "))

if (valorPrestacao <= (salarioBruto*0.30)):
    print("O empréstimo pode ser concedido")
else:
    print("O empréstimo não pode ser concedido")