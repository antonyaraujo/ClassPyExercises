# Em uma faculdade foram entrevistados 500 alunos. De cada um deles foram colhidas as seguintes
# informações: o código do curso que frequenta (1-engenharia; 2-computação; 3-matemática) e a
# idade. Faça um programa que processe estes dados e que forneça as seguintes informações:
# a) número de alunos por curso;
# b) número de alunos com idade entre 20 e 25 anos, por curso;
# c) o curso com o aluno mais velho e a idade deste aluno, }
# d) o curso com menor média de idade

eng, comp, mat = 0, 0, 0 # Quantidade de alunos no curso
eng_media, comp_media, mat_media = 0, 0, 0
eng_soma, comp_soma, mat_soma = 0, 0, 0 # Soma das idades dos alunos
eng_idade, comp_idade, mat_idade = 0, 0, 0 # O número de alunos com idade entre 20 e 25
curso_maisvelho, idade_maisvelho = 0, 0 # Curso e idade do aluno mais velho

for i in range(500):
    curso = int(input("Informe o código do curso: "))
    idade = int(input("Informe a sua idade: "))
    
    if curso == 1:
        eng += 1
        eng_soma = idade
        if (20 <= idade <= 25):
            eng_idade+= 1
            
    elif curso == 2:
        comp += 1
        comp_soma = idade
        if (20 <= idade <= 25):
            comp_idade+= 1
            
    elif curso == 3:
        mat += 1
        if (20 <= idade <= 25):
            mat_idade+= 1
    
    # Letra C        
    if idade > idade_maisvelho:
        idade_maisvelho = idade
        curso_maisvelho = curso
        
                        
    else:
        print("Código do curso inválido")

print("a) número de alunos por curso: \n"
      "Engenharia: %i; \n"
      "Computação: %i; \n"
      "Matemática: %i; \n" %(eng, comp, mat))

print("b) número de alunos com idade entre 20 e 25 anos, por curso: \n"
      "Engenharia: %i; \n"
      "Computação: %i; \n"
      "Matemática: %i; \n" %(eng_idade, comp_idade, mat_idade))

if (curso_maisvelho == 1):
    curso_maisvelho = "Engenharia"
elif (curso_maisvelho == 2):
    curso_maisvelho = "Computação"
elif (curso_maisvelho == 3):
    curso_maisvelho = "Matemática"

eng_media = eng_soma / eng_idade
comp_media = comp_soma / comp_idade
mat_media = mat_soma / mat_idade

print("c) o curso com o aluno mais velho é %s e a idade deste aluno é de %i anos\n" %(curso_maisvelho, idade_maisvelho))

if (eng_media < comp_media):
    if (eng_media < mat_media):
        print("d) o curso com menor média de idade é Engenharia")
    else:
        print("d) o curso com menor média de idade é Matemática")
else:
    if (comp_media < mat_media):
        print("d) o curso com menor média de idade é Computação")
    else:
        print("d) o curso com menor média de idade é Matemática")
