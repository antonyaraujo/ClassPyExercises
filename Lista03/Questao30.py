# A fábrica WK produz uma quantidade de automóveis por dia e deseja fazer um levantamento sobre
# essa produção. Escreva um programa que leia a quantidade de automóveis produzida diariamente,
# enquanto não for digitado um número negativo. Ao final o programa deve mostrar na tela a
# quantidade total de automóveis produzida, a quantidade de dias que foi considerada (ou seja, é a
# quantidade de números digitados), e a quantidade média de carros produzida por dia.
dias = 0
soma = 0
quantidade = int(input("Informe a quantidade de automóveis produzidas no dia: "))

while (quantidade > 0):
    dias += 1
    soma += quantidade
    quantidade = int(input("Informe a quantidade de automóveis produzidas no dia: "))

print("A quantidade total de automóveis produzida foi de: %i" %(soma))
print("A quantidade de dias considerados foram de %i dias" %dias)
print("A quantidade média de carros produzidos por dia foi de %i carros/dia" %(soma/dias))