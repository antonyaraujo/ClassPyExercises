a = float(input("Informe o lado 1: "))
b = float(input("Informe o lado 2: "))
c = float(input("Informe o lado 3: "))

if  ((abs(b-c)) < a < (b+c)):
    print("Esses valores podem formar os lados de um triângulo")
elif (abs(a-c) < b < a+c):
    print("Esses valores podem formar os lados de um triângulo")
elif (abs (a-b) < c < a+b):
    print("Esses valores podem formar os lados de um triângulo")
else:
    print("Esses valores não podem formar o lado de um triângulo")