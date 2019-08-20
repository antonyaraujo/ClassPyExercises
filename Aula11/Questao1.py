'''Após realizar uma série de experimentos, você criou um dicionário
que mostra a probabilidade de detectar certas partículas
subatômicas. Os nomes das partículas são as chaves do
dicionário, e as probabilidades são os valores: {'neutron': 0.55,
'proton': 0.21, 'rneson': 0.03, 'rnuon': 0.07, 'neutrino': 0.14}. Escreva
uma função que receba um dicionário deste tipo como entrada e
que retorna uma lista contendo o nome da partícula menos
provável de ser observada. Para o dicionário mostrado
anteriormente, a resposta deveria ser ['meson']. Havendo empate
em relação ao menor valor, a lista deve conter todos os nomes que
empatam no menor valor. Por exemplo, para o dicionário:
{'neutron': 0.55, 'proton': 0.21, 'rneson': 0.03, 'muon': 0.03,
'neutrino': 0.18} a resposta deveria ser ['rneson; 'muon'] ou ['rnuon;
'meson']. Considere que a função é genérica, ou seja, os valores
possíveis para chaves não se limitam aos cinco mostrados nos
exemplos anteriores. Ela deve retornar a chave do(s) menor(es)
valor(es), quaisquer que sejam os valores e chaves. Se algum
valor do dicionário não for numérico, a função deve causar um erro
de asserção. Também deve reportar erro se a soma das
probabilidades for diferente de 1. Use TDD.'''

probabilidade = {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}
print(probabilidade.values())

menor, valormenor = [''], [0]
for i in probabilidade:
    if valormenor[0] == 0:
        menor[0] = i
        valormenor[0] = 1
    valor = menor[0]
    if probabilidade[i] < probabilidade[valor]:
        menor[0] = i
    if probabilidade[i] == probabilidade[valor]:
        menor.append(i)

print(menor)