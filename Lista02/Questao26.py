'''Ajude um proprietário de cachorro a calcular quantos dias um pacote de
ração pode durar. Escreva um programa que leia o peso do cachorro em
quilos e o peso da embalagem de ração em quilos, e calcule e imprima a
quantidade de dias que o pacote de ração irá durar. A tabela abaixo indica
a porção diária de acordo com a faixa de peso do cachorro:

    Peso do Cachorro (KG) - Porções diárias
        Até 5Kg           -     60g
        6 - 10 Kg         -     95g
        11 - 15 Kg        -     135g
        16 - 20 Kg        -     170g
        Acima de 21Kg     -     215g
'''

peso = float(input("Informe o peso do doguinho: "))
pesoRacao = float(input("Informe o peso da embalagem de ração: "))

if (peso <= 5):
    print("O pacote ração durará %.2f dias" %(pesoRacao / 0.06))
elif 6 <= peso <= 10:
    print("O pacote ração durará %.2f dias" % (pesoRacao / 0.095))
elif 11 <= peso <= 15:
    print("O pacote ração durará %.2f dias" % (pesoRacao / 0.135))
elif 16 <= peso <= 20:
    print("O pacote ração durará %.2f dias" % (pesoRacao / 0.170))
else:
    print("O pacote ração durará %.2f dias" % (pesoRacao / 0.215))