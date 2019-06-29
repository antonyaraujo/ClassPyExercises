'''Escreva um programa para ajudar a calcular a quantidade de gotas de
um remédio que uma determinada criança precisa tomar. A bula
desse remédio pediátrico recomenda a seguinte dosagem: 5 gotas
para cada 2 kg do peso da criança. Você deve fazer um programa que
leia o peso desta criança, calcule e imprima na tela a quantidade de
gotas a ser tomada.'''

peso = float(input("Informe o peso da criança: "))
qtGotas = (peso / 2)*5
print("A quantidade de gotas a serem tomadas pela criança é de: %.1f gotas" %(qtGotas))