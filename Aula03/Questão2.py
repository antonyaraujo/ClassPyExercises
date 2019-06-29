''' Um grupo de amigos pretende alugar um carro por um único
dia. Consultadas duas agências, a primeira cobra R$62,00 pela
diária e R$1,40 por quilômetro rodado. A segunda cobra diária
de R$80,00 e mais R$1,20 por quilômetro rodado. Escreva um
programa que leia a quantidade de quilômetros a serem
rodados e calcule e imprima na tela o preço a ser pago em cada
uma das agências.'''

qtKm = float(input("Informe a quantidade de quilômetros a serem rodados: "))
print("Por %.1fkm na agência 1 será pago: R$%.2f" %(qtKm,(62+(1.40*qtKm))))
print("Por %.1fkm na agência 2 será pago: R$%.2f" %(qtKm,(80+(1.20*qtKm))))
