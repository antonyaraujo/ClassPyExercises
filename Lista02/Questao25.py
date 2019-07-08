peso = float(input("Informe o peso da criança: \n"))
idade = int(input("Informe a idade da criança: \n"))
pesoNormal = ((idade - 6)/ 4.4) + 2.3*(idade-6)+22
print(pesoNormal)
if (2 <= (pesoNormal) <= 5):
    print("Pare de tomar refrigerante.")
elif (5 < (pesoNormal) < 10):
    print("Pare de comer doces.")
else:
    print("Pare de tomar refrigerante e comer doces.")