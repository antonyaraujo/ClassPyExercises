'''Para ser apta a doar sangue a pessoa deve ter entre 18 e 65 anos e pesar
no mínimo 50kg. Escreva um algoritmo que leia a idade e o peso de uma
pessoa e apresente na tela uma mensagem informando se ela pode ser
doadora ou não.'''

idade = int(input("Informe a sua idade: "))
peso = float(input("Informe o seu peso: "))

if ( 18 <= idade <= 65 and peso >= 50):
    print("Você pode ser um doador(a) de sangue")
else:
    print("Você não pode ser um doador(a) de sangue")