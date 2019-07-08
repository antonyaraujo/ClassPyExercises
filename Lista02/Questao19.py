# Escreva um programa que determina a data cronologicamente maior de duas datas
# fornecidas pelo usuário. Cada data deve ser fornecida por três valores inteiros onde o
# primeiro representa um dia, o segundo um mês e o terceiro um ano.

dia1 = int(input("Informe o dia da data 1: "))
mes1= int(input("Informe o mês da data 1: "))
ano1 = int(input("Informe o ano da data 1: "))

dia2 = int(input("Informe o dia da data 2: "))
mes2 = int(input("Informe o mês da data 2: "))
ano2 = int(input("Informe o ano da data 2: "))

if (ano1 != ano2):
    if (ano1 > ano2):
        print("A data 1 é cronologicamente maior que a data 2")
    else:
        print("A data 2 é cronologicamente maior que a data 1")
else:
    if (mes1 != mes2):
        if (mes1 > mes2):
            print("A data 1 é cronologicamente maior que a data 2")
        else:
            print("A data 2 é cronologicamente maior que a data 1")
    else:
        if (dia1 != dia2):
            if (dia1 > dia2):
                print("A data 1 é cronologicamente maior que a data 2")
            else:
                print("A data 2 é cronologicamente maior que a data 1")
        else:
            print("As datas são exatamente iguais em dia/mes/ano")
