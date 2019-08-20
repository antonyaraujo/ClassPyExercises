f = 1
ultimo = 0
n = int(input("Informe o valor para saber seu fibonacci: "))
for i in range(2, n+1):
    penultimo = f
    f = f + ultimo
    ultimo = penultimo
print("fibonacci(%i) = %i" %(n, f))
