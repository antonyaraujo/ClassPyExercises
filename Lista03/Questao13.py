# Escreva um programa que leia números inteiros até que a soma de tais números totalize no mínimo
# 100. Devem ser lidos tantos valores quantos necessários para que o limite seja atingido ou superado.
# Quando isto ocorrer, o programa também deve exibir quantos números foram lidos e sua média.

soma = 0
numero = int(input("Informe um valor: "))
soma += numero
lidos = 1

while (soma <= 100):
    numero = int(input("Informe um valor: "))
    soma += numero
    lidos += 1

print("Soma: ", soma)
print("Números lidos: ", lidos)
print("Média: ", (soma/lidos))