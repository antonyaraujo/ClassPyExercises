# Adaptar o programa desenvolvido acima para que ela calcule o percentual dos valores positivos e
# negativos em relação ao total de valores fornecidos.

positivos, negativos = 0, 0
total = 1
num = int(input("Informe um número: "))
while (num != 0):
    if num > 0:
        positivos += 1
    if num < 0:
        negativos += 1
    num = int(input("Informe um número: "))
    total += 1

print("Positivos: %.1f%%" %((positivos/total)*100))
print("Negativos: %.1f%%" %((negativos/total)*100))