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
    