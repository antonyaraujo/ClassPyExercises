# Um grupo de professores deseja fazer uma festa no feriado. Foi solicitado aos docentes que
# informassem os seguintes dados:
# - A escolha do lugar entre as opções ‘p’ (praia) ou ‘h’ (hotel fazenda);
# - A escolha do tipo de comida entre as opções ‘c’ (churrasco) ou ‘f’ (feijoada) ou ‘m’
# (massa);
# - A escolha do dia preferido entre as opções ‘s’ (sábado) ou ‘d’ (domingo).
# Sua tarefa é fazer um programa que leia as opções de uma quantidade indeterminada de professores
# que votaram e imprimir na tela as opções campeãs (lugar, tipo de comida e dia preferido). O
# programa deve perguntar se deseja continuar a cada ciclo de repetição.
c = 'S'
praia, hotelfazenda, sabado, domingo = 0, 0, 0, 0
churrasco, feijoada, massa = 0, 0, 0
while (c == 'S'):
    lugar = input("Escolha do lugar entre as opções ‘p’ (praia) ou ‘h’ (hotel fazenda): ")
    tipo_comida = input("Escolha do tipo de comida entre as opções ‘c’ (churrasco) ou ‘f’ (feijoada) ou ‘m’"
"(massa): ")
    dia_preferido = input("A escolha do dia preferido entre as opções ‘s’ (sábado) ou ‘d’ (domingo): ")

    if lugar == 'p':
        praia += 1
    else:
        hotelfazenda += 1

    if tipo_comida == 'c':
        churrasco += 1
    elif tipo_comida == 'f':
        feijoada += 1
    elif tipo_comida == 'm':
        massa += 1

    if dia_preferido == 's':
        sabado += 1
    else:
        domingo += 1

    c = input("Deseja continuar? S - Sim ou N - Não")

if (praia > hotelfazenda):
    print("Lugar: Praia")
else:
    print("Lugar: Hotel Fazenda")

if (churrasco > feijoada):
    if (churrasco > massa):
        print("Tipo de Comida: Churrasco")
    else:
        if massa > feijoada:
            print("Tipo de Comida: Massa")
else:
    if feijoada > massa:
        print("Tipo de Comida: Feijoada")
    else:
        print("Tipo de Comida: Massa")

if (sabado > domingo):
    print("Dia preferido: Sábado")
else:
    print("Dia preferido: Domingo")