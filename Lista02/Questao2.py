nota = float(input("Informe a nota: \n"))
if nota >= 9:
    print("Conceito: A")
elif 8 <= nota < 9:
    print("Conceito: B")
elif 7 <= nota < 8:
    print("Conceito: C")
elif 6 <= nota < 7:
    print("Conceito: D")
else:
    print("Conceito: F")