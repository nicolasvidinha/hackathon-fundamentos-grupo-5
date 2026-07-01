def calcular_valor_total(listacompras):
    total = 0
    for nome, categoria, valor in listacompras:
        total += valor
        pass
    return total