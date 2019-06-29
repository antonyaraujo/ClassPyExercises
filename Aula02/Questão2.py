''' Sabe-se que para iluminar de maneira correta os cômodos de uma
casa, para cada m² deve-se usar 18 W de potência. Escreva um
algoritmo que leia as dimensões de um cômodo retangular (em
metros), calcule e mostre a sua área (em m2) e a potência de
iluminação que deverá ser utilizada.'''

altura = float(input("Informe a altura do cômodo (em Metros): "))
largura = float(input("Informe a largura do cômodo (em Metros): "))

area = altura * largura
potencia = area / 18

print ("\nÁrea: ", area, "m²")
print ("Potência: ", potencia, "W")