# Faça um programa que solicite dois números inteiros positivos e exiba os múltiplos de 7 existentes
# entre estes números. Faça uma versão com cada um dos laços: for, while e do-while.

n1 = int(input("Informe o número 1: "))
n2 = int(input("Informe o número 2: "))

# em for
print("Múltiplos de 7 [FOR]: ")
for i in range(n1, n2+1):
    if (i % 7 == 0):
        print(i)

# em while
print("\nMúltiplos de 7 [WHILE]: ")
c = n1
while(c <= n2):
    if (c % 7 == 0):
        print(c)
    c += 1