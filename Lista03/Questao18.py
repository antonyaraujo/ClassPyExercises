# Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em uma determinada
# cidade. Para isso são fornecidos os seguintes dados de 500 consumidores:
# • quantidade de kWh consumidos durante o mês;
# • código do tipo de consumidor (1 - residencial, 2 - comercial, 3 - industrial).
# Calcular:
    # a) a média de consumo residencial;
    # b) a media de consumo comercial;
    # c) a média de consumo industrial;
    # d) o total de consumo para cada um dos tipos de consumidores;
    
residencial, comercial, industrial = 0, 0, 0
qt_residencial, qt_comercial, qt_industrial = 0, 0, 0
for i in range(5):
    kWh = float(input("Informe a quantidade de kWh consumidos durante o mês: \n"))
    codigo = int(input("Informe o código do tipo de consumidor: \n"))
    if (codigo == 1):
        residencial += kWh
        qt_residencial += 1
    elif (codigo == 2):
        comercial += kWh
        qt_comercial += 1
    elif (codigo == 3):
        industrial += kWh
        qt_industrial += 1
    else:
        print("Código do tipo de consumidor é inválido")
    
print("A) a média de consumo residencial: %.2fkWh" %(residencial/qt_residencial))
print("B) a média de consumo comercial: %.2fkWh" %(comercial/qt_comercial))
print("C) a média de consumo industrial: %.2fkWh" %(industrial/qt_industrial))
print("D) o total de consumo para cada um dos tipos de consumidores: %.2fkWh" %(residencial+comercial+industrial))
    