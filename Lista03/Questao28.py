# Escreva um programa que leia um número indeterminado de notas entre 0.0 e 10.0. Ao final imprima
# a quantidade de notas maiores ou iguais a 7. A digitação deve ser encerrada quando for digitada uma
# nota inválida.
nota, nota_7 = 0, 0
nota = float(input("Insira a nota: "))
while 0<=  nota <= 10:
    if nota >= 7:
        nota_7 += 1
    nota = float(input("Insira a nota: "))
print("A quantidade notas maiores ou iguais a 7: %i" %(nota_7))