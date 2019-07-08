# Altere o programa anterior para que o usuário informe qual o valor inicial e o valor final em
# farenheit e informe também o intervalo entre estes valores para conversão (de um em um, de dois em
# dois, etc.)

n1 = int(input("Informe o valor inicial: "))
n2 = int(input("Informe o valor final: "))
n = int(input("Informe o intervalo entre os valores: "))
print("   Fº ------ Cº")
for f in range(n1, n2, n):
    c = (f - 32) / 1.8000
    print(" %.2fCº -- %.dFº" %(c, f))