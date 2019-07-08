# Você passou um questionário onde a primeira questão perguntava a um grupo indeterminado de
# pessoas qual a freqüência com que eles fazem exercícios, sendo as respostas possíveis:
# 0 – nunca; 1
# – poucas vezes; 2 – muitas vezes. Faça um programa que leia as respostas desta primeira questão, ele
# deve se encerrar se a resposta for -1. O programa deve imprimir na tela:
# Quantos responderam “nunca”, quantos responderam “poucas vezes” e quantos responderam
# “muitas vezes”.
# Quantos responderam o questionário.
# Qual foi a porcentagem de respostas “nunca”, “poucas vezes” e “muitas vezes”.

frequencia = 1
contagem = 0
nunca, poucasvezes, muitasvezes = 0, 0, 0
frequencia = int(input("Com que frequência você faz exercícios? \n"))
while (frequencia != (-1)):
    contagem += 1

    if frequencia == 0:
        nunca += 1
    elif frequencia == 1:
        poucasvezes += 1
    elif frequencia == 2:
        muitasvezes += 1

    frequencia = int(input("Com que frequência você faz exercícios? \n"))

print("Nunca: %i" %(nunca))
print("Poucas vezes: %i" %(poucasvezes))
print("Muitas vezes: %i" %(muitasvezes))
print("Total de respostas: %i" %(contagem))
print("Nunca: %.2f%%" %((nunca/contagem)*100))
print("Poucas vezes: %.2f%%" %((poucasvezes/contagem)*100))
print("Muitas vezes: %.2f%%" %((muitasvezes/contagem)*100))