# Em uma competição esportiva o desempenho de uma equipe é medida pela quantidade de
# medalhas de ouro que a equipe conquista. Escreva um algoritmo/programa que leia a
# quantidade de medalhas de ouro ganhas pela equipe e escreva na tela uma mensagem
# informando o desempenho da equipe de acordo com a tabela abaixo:

qt = int(input("Informe a quantidade de medalhas de ouro ganhas: \n"))
if (qt >= 30):
    print("Desempenho: Ótimo")
elif 20 <= qt < 29:
    print("Desempenho: Muito Bom")
elif 10 <= qt < 19:
    print("Desempenho: Regular")
else:
    print("Desempenho: Ruim")