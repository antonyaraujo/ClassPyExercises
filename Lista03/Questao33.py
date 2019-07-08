# Considere um cinema a respeito do qual foi feita uma pesquisa de qualidade. Certo dia, cada
# espectador respondeu a um questionário, no qual constava sua opinião em relação ao filme, segundo
# as seguintes notas:
    # Nota Significado
    # 1 Ótimo
    # 2 Regular
    # 3 Ruim
# Elabore um programa que, lendo esse dado fornecido pelos espectadores, calcule e imprima:
# • A quantidade de pessoas que participaram da pesquisa;
# • A porcentagem de respostas “ótimo” (notas 1);
# • A porcentagem de respostas “regular” (notas 2);
# • A porcentagem de respostas “ruim” (notas 3).
# Quando for digitada uma nota inválida, significa que a digitação dos dados chegou ao fim.

qt_otimo, qt_regular, qt_ruim = 0, 0, 0
nota = 1
while 0 < nota < 4:
    nota = int(input("Informe a sua nota ao filme: "))
    if nota == 1:
        qt_otimo += 1
    elif nota == 2:
        qt_regular += 1
    elif nota == 3:
        qt_ruim += 1

total = qt_otimo + qt_regular + qt_ruim
print("Total de participantes: %i" %total)
print("Ótimo: %.2f%%" %((qt_otimo/total)*100))
print("Regular: %.2f%%" %((qt_regular/total)*100))
print("Ruim: %.2f%%" %((qt_ruim/total)*100))