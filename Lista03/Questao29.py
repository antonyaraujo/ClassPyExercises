# Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade e
# quantidade de filhos. Fazer um programa que informe:
# • a média de idade do grupo;
# • quantidade de pessoas com mais de 5 filhos;
# • porcentagem de pessoas com menos de 20 anos e com filhos;
# • quantidade de pessoas entrevistadas;
# O programa finalizará a leitura dos dados quando for digitado um valor negativo para a idade.

soma, filhos_5, porc_filhos, contador = 0, 0, 0, 0
idade = int(input("Informe a idade: "))
qtFilhos = int(input("Informe a quantidade de filhos: "))
while (idade > 0):

    soma += idade

    if qtFilhos > 5:
        filhos_5 += 1
    
    if (idade < 20) and qtFilhos > 0:
        porc_filhos += 1

    idade = int(input("Informe a idade: "))
    qtFilhos = int(input("Informe a quantidade de filhos: "))

    contador += 1

print(soma)
print("A média de idade do grupo: %.2f" %(soma/contador))
print("Quantidade de pessoas com mais de 5 filhos: %.f" %(filhos_5))
print("Porcentagem de pessoas com menos de 20 anos e com filhos: %.2f%%" %((porc_filhos/contador)*100))
print("A quantidade de pessoas entrevistadas foi de: %i" %(contador))