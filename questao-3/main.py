aparelhos = [
    ("Ar-condicionado", 1200, 8),
    ("Geladeira", 180, 24),
    ("Televisão", 150, 5),
    ("Chuveiro", 5500, 0.5)
]

tarifa_kwh = 1.05

def calcular_consumo_aparelho(potencia, horas):
    return (potencia * horas * 30) / 1000

def classificar_consumo(consumo_total):
    if consumo_total <= 150:
        return "BAIXO CONSUMO"
    elif consumo_total <= 300:
        return "CONSUMO MODERADO"
    else:
        return "ALTO CONSUMO"

def obter_recomendacao(aparelho):
  
    if aparelho == "Ar-condicionado":
        return "Verifique a temperatura configurada e mantenha filtros limpos."
    elif aparelho == "Chuveiro":
        return "Reduza o tempo de banho e utilize a posição verão quando possível."
    elif aparelho == "Geladeira":
        return "Verifique a vedação da borracha e evite abrir a porta sem necessidade."
    else:
        return "Fique atento ao tempo de uso e desligue o aparelho quando não estiver utilizando."

consumo_total = 0  
maior_consumo = -1
aparelho_maior_consumo = ""
resultados_aparelhos = []

for nome, potencia, horas in aparelhos:

    consumo_mensal = calcular_consumo_aparelho(potencia, horas)    
  
    consumo_total += consumo_mensal
    
    resultados_aparelhos.append((nome, consumo_mensal))
    
    if consumo_mensal > maior_consumo:
        maior_consumo = consumo_mensal
        aparelho_maior_consumo = nome

custo_estimado = consumo_total * tarifa_kwh
classificacao = classificar_consumo(consumo_total)
recomendacao = obter_recomendacao(aparelho_maior_consumo)


print("===== RELATÓRIO DE CONSUMO =====")
for nome, consumo in resultados_aparelhos:
    print(f"{nome}: {consumo:.2f} kWh")

print(f"Consumo total: {consumo_total:.2f} kWh")
print(f"Custo estimado: R$ {custo_estimado:.2f}")
print(f"Classificação: {classificacao}")
print(f"Aparelho de maior consumo: {aparelho_maior_consumo}")
print(f"Recomendação: {recomendacao}")
