# Uma determinada companhia aérea só contrata aeromoças que preencham os seguintes
# requisitos:
# - Ter idade igual ou superior a 24 anos.
# - Ter altura igual ou superior a 1.70 m.
# - Falar com fluência 2 ou mais idiomas.

idade = int(input("Informe a sua idade: \n"))
altura = float(input("Informe a sua altura: \n"))
idiomas = int(input("Informe a quantidade de idiomas falados com fluência: \n"))

if ((idade >= 24) and (altura >= 1.7) and (idiomas >= 2)):
    print("A candidata atende os requisitos da companhia")
else:
    print("A candidata não atende os requisitos da companhia")

