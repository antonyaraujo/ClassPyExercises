# Um estadunidense em visita ao Brasil tinha muita dificuldade na hora de escolher entre
# “bermudas” ou “calças”, pois ele não entendia nossa medida de temperatura (celsius).
# Escreva um programa que, após a entrada da temperatura em Celsius (C), escreva a
# temperatura em Fahrenheits (F) e também o que vestir. Dado que:
# F = (9C + 160)/5;
# Ele irá vestir:
# calças se F < 65,
# bermudas em caso contrário

c = float(input("Please, report the temperature: \n"))
f = (9*c + 160)/5
if (f < 65):
    print("You should wear: pants, because it's %.2fF" %f)
else:
    print("You should wear: shorts, because it's %.2fF" %f)