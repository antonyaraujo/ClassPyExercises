# Faça um programa que peça para o usuário pensar em número de 1 a 4 e depois pergunte
# se o número é maior que 2 (S-Sim ou N-Não), e caso seja maior que 2, pergunte se ele é
# maior que 3, ou caso não seja maior que 2, pergunte se é maior que 1. Ao final o programa
# deve mostrar o número que o usuário pensou.

numero = int(input ("Digite um número de 1 a 4: "))
if 1 <= numero <= 4:
    maior = (input("O número é maior que 2? S - Sim ou N - Não: "))
    if maior == 'S':
        maior = input("O número é maior que 3? S - Sim ou N - Não: ")
        if maior == 'S':
            print("O número pensado é 4")
        else:
            print("O número pensado é 3")
    else:
        maior = input("Esse número é maior que 1? S - Sim ou N - Não: ")
        if (maior == 'S'):
            print("O número pensado é 2")
        else:
            print("O número pensado é 1")