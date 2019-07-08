# Para ser apta a doar sangue a pessoa deve ter entre 18 e 65 anos e pesar no mínimo
# 50kg. Escreva um programa que leia a idade e o peso de uma pessoa e apresente na tela
# uma mensagem informando se ela pode ser doadora ou não.

idade = int(input("Informe a sua idade: \n"))
peso = float(input("Informe o seu peso: \n"))

if ((18 <= idade <= 65) and (peso >= 50)):
    print("Você está apto(a) para doar sangue")
else:
    print("Você não está apto(a) para doar sangue")