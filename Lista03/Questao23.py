# Escreva um programa que leia a quantidade de pessoas entrevistadas. Em seguida, para cada pessoa
# leia a idade e o sexo e calcule e mostre:
# • A média de idade das pessoas;
# • A média de idade das mulheres;
# • A média de idade dos homens;
# • A quantidade de pessoas em cada faixa etária segundo a tabela a seguir;
# • A porcentagem de mulheres da segunda faixa etária

soma_idade, n_mulheres, n_homens = 0, 0, 0
idade_mulheres, idade_homens = 0, 0
idade_15, idade_16_30, idade_31_45, idade_46_60, idade_60 = 0, 0, 0, 0, 0
qt_f_16_30 = 0

n = int(input("Informe a quantidade de pessoas entrevistadas: " ))
for i in range(n):
    idade = int(input("Informe a idade: "))
    sexo = input("Informe o sexo (F mulher ou M homem): ")
    soma_idade += idade
    if (sexo == "F"):
        idade_mulheres += idade
        n_mulheres += 1
    else:
        idade_homens += idade
        n_homens += 1

    if idade <= 15:
        idade_15 += 1
    elif 16 <= idade <= 30:
        idade_16_30 += 1
        if (sexo == "F"):
            qt_f_16_30 += 1
    elif 31 <= idade <= 45:
        idade_31_45 += 1
    elif 46 <= idade <= 60:
        idade_46_60 += 1
    else:
        idade_60 += 1


print("A média de idade das pessoas: %.2f" %(soma_idade/n))
print("A média de idade das mulheres: %.2f" %(idade_mulheres/n_mulheres))
print("A média de idade dos homens: %.2f" %(idade_homens/n_homens))
print(" A quantidade de pessoas na faixa etária 1: %i" %(idade_15))
print(" A quantidade de pessoas na faixa etária 2: %i" %(idade_16_30))
print(" A quantidade de pessoas na faixa etária 3: %i" %(idade_31_45))
print(" A quantidade de pessoas na faixa etária 4: %i" %(idade_46_60))
print(" A quantidade de pessoas na faixa etária 5: %i" %(idade_60))
print(" A quantidade de mulheres na faixa etária 2: %i" %(qt_f_16_30))
