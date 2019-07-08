# Escreva um programa que verifique se um ano lido é ano de copa do mundo. Seu
# programa deve permitir a leitura do ano, depois realizar os testes necessários e exibir na
# tela mensagem de que é ou não ano de copa do mundo. Considerando que um ano de
# copa do mundo é divisível por 2 e não é divisível por 4.

ano = int(input("Informe o ano"))

if ((ano % 2 == 0) and (ano % 4 != 0)):
    print("É ano de Copa!")
else:
    print("Não é ano de copa!!!")