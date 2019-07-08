# Infrações de trânsito e acidentes em geral estão muitas vezes relacionados com excesso
# de velocidade. Pensando nisso a secretaria do DETRAN reajustou o valor das multas e
# encomendou a você um programa que calcule os novos valores, válidos para as rodovias
# federais. Se a velocidade do veículo for até a velocidade permitida, o condutor não paga
# multa; caso ela exceda em até 20% a velocidade permitida, o valor da multa é de R$ 250;
# e caso o excesso seja superior à 20% a multa é de R$750. Escreva um programa que leia
# do teclado a velocidade máxima permitida e a velocidade na qual o veículo trafegava,
# apresentando na tela o valor da multa a ser pago.

velocidade_max = int(input("Informe a velocidade máxima permitida: "))
velocidade = float(input("Informe a velocidade trafegada pelo veículo: "))
ultrapassagem = ((velocidade*100)/velocidade_max) - 100


if (0 < ultrapassagem <= 20):
    print("A multa a ser paga é de R$250, pois ultrapassou em 20% o limite permitido!!")
elif (ultrapassagem > 20):
    print("A multa a ser paga é de R$750, pois ultrapassou em mais de 20% o limite permitido!!")
else:
    print("Não paga multa, pois não ultrapassou a velocidade!")