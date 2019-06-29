'''Faça um programa que leia a idade de uma pessoa expressa em dias e
mostre-a expressa apenas em anos, meses e dias. Assuma, neste
programa, que um ano tem 365 dias e que um mês tem 30 dias.
Exemplo: Se a pessoa digitar que viveu 10260 dias significa que ela
tem 28 anos, 1 mês e 10 dias.'''

idade = int(input("Informe sua idade em dias: "))

anos = idade/365
meses = (idade%365)/30
dias = ((idade%365)%30)

print ("Você já viveu: %i anos, %i meses e %i dias" %(anos, meses, dias))
