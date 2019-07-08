# Escreva um programa em linguagem C que determina se um valor informado pelo usuário é um
# número primo ou não

primo = True
numero = int(input("Informe o número: "))
for i in range(2, numero-1):
    if (numero%i == 0):
        primo = False
        break
    else:
        primo = True

if (primo):
    print("É primo saporra")
else:
    print("É primo nam")