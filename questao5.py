# Base de casos anteriores
base_de_casos = [
    {"sintomas": {"febre", "tosse", "dor de garganta"}, "diagnostico": "Gripe"},
    {"sintomas": {"dor de cabeça", "sensibilidade à luz", "náusea"}, "diagnostico": "Enxaqueca"},
    {"sintomas": {"dor abadominal", "náusea", "diarreia"}, "diagnostico": "Gastroenterite"},
    {"sintomas": {"febre", "dor muscular", "cansaço"}, "diagnostico": "Dengue"},
    {"sintomas": {"tosse", "falta de ar", "dor no peito"}, "diagnostico": "Bronquite"}
]
def comparar_sintomas(sintomas_paciente, base):
    melhores_casos = []
    maior_similaridade = 0

    for caso in base:
        intersecao = sintomas_paciente.intersection(caso["sintomas"])
        similaridade = len(intersecao)

        if similaridade > maior_similaridade:
            melhores_casos = [caso]
            maior_similaridade = similaridade
        elif similaridade == maior_similaridade and similaridade > 0:
            melhores_casos.append(caso)

    return melhores_casos, maior_similaridade

# Sintomas relatados pelo paciente (exemplo)
#sintomas_paciente = {"dor abdominal", "diarreia", "náusea"}
sintomas_paciente = {"febre"}

# Faz a busca
casos_similares, grau = comparar_sintomas(sintomas_paciente, base_de_casos)

# Mostra o resultado
if casos_similares:
    print(f"\nCasos mais similares encontrados com {grau} sintomas em comum:\n")
    for i, caso in enumerate(casos_similares, 1):
        #print(f"{i}. Diagnóstico sugerido: {caso['diagnostico']} com os sintomas: {caso['sintomas']}")
        print(f"{i}. Diagnóstico sugerido: {caso['diagnostico']}")
else:
    print("\nNenhum caso similar encontrado.")
