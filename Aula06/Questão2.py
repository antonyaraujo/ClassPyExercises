''' Escreva um programa que leia um número indeterminado de notas entre
0 e 10. Ao final, mostre a média das notas e a quantidade de notas
maiores ou iguais a 7. A digitação deve ser encerrada quando for
digitada uma nota inválida.'''

soma, nota, quantidade, maior7 = 0.0, 0, 0, 0

while (0 <= nota <= 10):
    soma += nota
    quantidade += 1
    if nota >= 7:
        maior7 += 1
    nota = float(input("Informe a nota: "))

quantidade -= 1
if quantidade > 0:
    media = soma / quantidade
    print("A média das notas foi de: ", media)
    print("Houveram %i notas maiores ou iguais a 7" %maior7)