# Faça um programa que leia uma quantidade não determinada de números positivos. Calcule a média
# dos valores pares, a média de valores ímpares e a média geral dos números lidos. A leitura encerrará
# quando for digitado um valor menor ou igual a zero.

pares, qt_pares = 0, 0
impares, qt_impares = 0, 0
numero = int(input("Informe um número: "))
while (numero > 0):
    if((numero % 2) == 0):
        pares += numero
        qt_pares += 1
    else:
        impares += numero
        qt_impares += 1
    numero = int(input("Informe um número: "))

print("A média dos valores pares %.2f" %((pares/qt_pares)))
print("A média dos valores ímpares %.2f" %((impares/qt_impares)))
print("A média geral é: %.2f" %((pares+impares)/(qt_impares+qt_pares)))