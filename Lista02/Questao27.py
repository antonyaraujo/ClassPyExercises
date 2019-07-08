# Um novo terminal de computador foi instalado na biblioteca para facilitar a consulta de
# livros. A você coube fazer a interface de apresentação. Como parte deste projeto escreva
# um pequeno programa que leia do teclado um valor correspondente à hora do dia (XX h
# XX min XX seg) e imprima na tela “Bom Dia!”, “Boa Tarde!” ou “Boa Noite!” de acordo com
# o horário. Se o horário estiver compreendido entre 0h e 6h, deve imprimir “Sistema
# Indisponível”.

hora = int(input("Informe a hora do dia: "))
minuto = int(input("Informe o minuto do dia: "))
segundo = int(input("Informe o segundo do dia: "))

if (hora > 6) and (hora <= 12 and minuto <= 59 and segundo <= 59):
    print("Bom dia!")
elif (hora > 12) and (hora <= 17 and minuto <= 59 and segundo <= 59):
    print("Boa Tarde!")
elif (hora > 18) and (hora <= 23 and minuto <= 59 and segundo <= 59):
    print("Boa Noite!")
else:
    print("Sistema Indisponível!!")
