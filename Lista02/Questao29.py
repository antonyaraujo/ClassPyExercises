# Uma agência de viagens quer disponibilizar a seus passageiros que chegam ao Brasil um
# terminal de conversão de taxa de câmbio. Tal terminal será utilizado num aeroporto que
# recebe principalmente passageiros norte-americanos, europeus e japoneses. Escreva um
# programa que leia do teclado a opção desejada: converter dólares, euros ou ienes para
# reais, leia a quantia em moeda estrangeira e apresente na tela o valor dado e seu
# equivalente em reais. Faça um programa que utilize apenas a estrutura if-else e outro que
# utilize apenas a estrutura switch.
# Considere:
# 1,00 DÓLAR = R$ 2,35
# 1,00 EURO = R$ 2,98
# 1,00 IENE = R$ 0,02

valor = float(input("Informe a quantia a ser convertida: "))
opcao = int(input("Informe a moeda de conversão: 1 - Dólar\n 2 - Euro\n 3 - Iene\n "))
if (opcao == 1):
    conversao = valor*2.35
    print("US$%.2f = RS$%.2f" %(valor, conversao))
elif (opcao == 2):
    conversao = valor * 2.98
    print("%.2f € = RS$%.2f" % (valor, conversao))
elif (opcao == 3):
    conversao = valor * 0.02
    print("¥%.2f = RS$%.2f" % (valor, conversao))
else:
    print("Opção Inválida")