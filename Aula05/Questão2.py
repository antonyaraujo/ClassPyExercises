'''Uma determinada companhia aérea só contrata aeromoças que preencham
os seguintes requisitos:

    - Ter idade igual ou superior a 24 anos.

    - Ter altura igual ou superior a 1.70 m.

    - Falar com fluência 2 ou mais idiomas.

Escreva um algoritmo que leia a idade, a altura e a quantidade de idiomas
falados com fluência de uma candidata e imprima uma mensagem
informando se essa candidata atende ou não aos requisitos da companhia
aérea.'''

idade = int(input("Informe a sua idade: "))
altura = float(input("Informe a sua altura: "))
idioma = int(input("Informe a quantidade de idiomas falados com fluência: "))

if ((idade >= 24) and (altura >= 1.70) and (idioma >= 2)):
    print("A candidata a areomoça atende aos requisitos da companhia aérea")
else:
    print("A candidata a areomoça não atende aos requisitos da companhia aérea")