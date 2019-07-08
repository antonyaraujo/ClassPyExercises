# Escreva um programa que leia as 50 notas de uma avaliação dos alunos que cursam uma disciplina
# de algoritmos, calcule e imprima na tela:
# • quantidade de notas maiores ou iguais a 7;
# • a porcentagem de notas maiores ou iguais a 7;
# • quantidade de notas maiores ou iguais a 4 e menores que 7;
# • a porcentagem de notas maiores ou iguais a 4 e menores que 7;
# • quantidade de notas menores que 4;
# • a porcentagem de notas menores que 4;
# • a média da turma na avaliação.

soma, nota_7, nota_4_7, nota_4, soma = 0, 0, 0, 0

for i in range(50):
    nota = float(input("Informe a nota: "))
    if nota >= 7:
        nota_7 +=1
    elif 4 <= 4 < 7:
        nota_4_7 += 1
    else:
        nota_4 += 1

    soma += nota

print("A quantidade de notas maiores ou iguais a 7: %i" %(nota_7))
print("A porcentagem de notas maiores ou iguais a 7: %.f"  %((nota_7 / 50)*100))
print("A quantidade de notas maiores ou iguais a 4 e menores que 7: %i" %(nota_4_7))
print("A porcentagem de notas maiores ou iguais a 4 e menores que 7: %.f" %((nota_4_7)/ 50) * 100)
print("A quantidade de notas menores que 4: %i" %(nota_4))
print("A porcentagem de notas menores que 4: %.f" %((nota_4/50)*100))
print("A média na turma é de: %f" %(soma/50))