import math
# Escreva um programa que determina quanto tempo (segundos) um corpo leva para cair de
# uma determinada altura (h 0 ≥ 0), dada em metros (m), a partir do repouso (v 0 = 0). Lembre-
# se que h = h 0 + v 0 t + (gt 2 )/2. Assuma: h = 0, g = - 9,8 m/s2. Use a função sqrt (x), da
# biblioteca math.h, para obter a raiz quadrada. Seu programa deve pedir que o usuário
# informe h 0 e adverti-lo caso o valor informado seja negativo.

ho = float(input("Informe a altura inicial: "))
if (ho > 0):
  t = math.sqrt(((-ho)*2)/-9.8)
  print("O corpo leva %.2fs para cair" %(t))
else:
    print("A altura não pode ser negativa")