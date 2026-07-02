def calcular_valor_total(listacompras):
    total = 0.0
    for nome, categoria, valor in listacompras:
        total += valor
    return total

def calcular_valor_frutas_verduras(listacompras):
    total = 0.0
    for nome, categoria, valor in listacompras:
        if categoria == "frutas" or categoria == "verduras":
            total += valor
    return total

def calcular_desconto(valor_frutas_verduras, eh_fidelidade, idade):
    desconto_total = 0.0
    
    if idade > 60:
        desconto_total += 0.10
        
    if eh_fidelidade == True:
        desconto_total += 0.05
        
    if valor_frutas_verduras > 30.00:
        desconto_total += 0.05
    
    if desconto_total > 0.20:
        desconto_total = 0.20
    
    return desconto_total
