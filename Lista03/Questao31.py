# Professores preocupados com o número de faltas de seus alunos resolveram pedir para que esses
# alunos escrevessem um programa para calcular a média de faltas dos alunos de uma determinada
# turma. Imagine que você é um aluno dessa turma e tem como tarefa escrever tal programa. Esse
# programa deve ler a quantidade de faltas dos alunos dessa turma (permitir a leitura enquanto for
# digitado um número positivo para a quantidade de faltas). Ao final imprimir a quantidade média de
# faltas e o número de alunos que participaram dessa pesquisa.

soma, contagem = 0, 0
faltas = int(input("Informe a quantidade de faltas: "))
while (faltas > 0):
    soma += faltas
    contagem += 1
    faltas = int(input("Informe a quantidade de faltas: "))
print("Quantidade média de faltas: %.2f" %(soma/contagem))
print("Número de alunos que participaram dessa pesquisa: %i" %contagem)

