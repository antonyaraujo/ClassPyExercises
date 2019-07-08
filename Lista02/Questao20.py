# Escreva um programa em Linguagem C que solicita ao usuário duas datas (dia, mês, ano),
# onde a primeira data é o dia atual e a segunda é a data de vencimento de suas contas, em
# seguida o seu programa deve imprimir se a conta em questão “está atrasada”, “não está
# atrasada” ou “vence neste dia”. Assuma que o usuário informa duas datas válidas.

dia_atual = int(input("Informe o dia atual: "))
mes_atual = int(input("Informe o mês atual: "))
ano_atual = int(input("Informe o ano atual: "))

dia_vencimento = int(input("Informe o dia de vencimento: "))
mes_vencimento = int(input("Informe o mês de vencimento: "))
ano_vencimento = int(input("Informe o ano de vencimento: "))

if (ano_atual > ano_vencimento):
    print("A conta está atrasada em %i ano(s), %i mes(es) e %i dia(s)" %((ano_atual-ano_vencimento), (mes_atual-mes_vencimento),
                                                                         (dia_atual-dia_vencimento)))
else:
    if (mes_atual > mes_vencimento and ano_atual > ano_vencimento):
        print("A conta está atrasada em %i ano(s), %i mes(es) e %i dia(s)" % (
        (ano_atual - ano_vencimento), (mes_atual - mes_vencimento),
        (dia_atual - dia_vencimento)))
    else:
        if (dia_atual > dia_vencimento and mes_atual >= mes_vencimento):
            print("A conta está atrasada em %i ano(s), %i mes(es) e %i dia(s)" % (
            (ano_atual - ano_vencimento), (mes_atual - mes_vencimento),
            (dia_atual - dia_vencimento)))
        else:
            if (dia_atual == dia_vencimento):
                print("A conta vence neste dia")
            else:
                print("A conta não está atrasada")