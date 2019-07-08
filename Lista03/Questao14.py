# Escreva um programa que leia a nota final um número indeterminado de alunos, e escreva na tela a
# situação de cada um. “APROVADO” se NF >= 7; “EM EXAME” se 4 <= NF < 7; “REPROVADO”
# se NF < 4. O programa deve ser encerrado se for digitada uma nota final fora do intervalo entre 0 e
# 10.

NF = 1
while (0 <= NF <= 10):
    NF = float(input("Informe a nota final: "))
    if (NF >= 7):
        print("APROVADO")
    elif (4 <= NF < 7):
        print("EM EXAME")
    else:
        print("REPROVADO")