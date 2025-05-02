#paises = {
#    "Brasil": "Brasilia",
#    "França": "Páris"
#}

#Alinhamento List e Dicionario
viagens = {
    "França": ["Páris", "Lille", "Dijon"]
}

print(viagens["França"][1])
                #   0    1        2
aninhamento_list = ["A", "B", ["C", "D"]]

#print(aninhamento_list[2][1])


paises = {
    "Brasil": {
        "num_visitas": 8,
        "cidades_visitadas": ["Juazeiro", "Crato", "Barbalha"]
    },
    "França": "Páris",
    "Alemanha": ["Stuttgart", "Berlin"]
}

print(paises["Alemanha"][1])