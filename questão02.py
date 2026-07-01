numero_vaga = 0
tipo_vaga = 0
ocupada = 0

vagas = [

    (1, "comum", True),

    (2, "idoso", False),

    (3, "pcd", False),

    (4, "comum", True),

    (5, "comum", False)

]

def total_vagas(vagas):
    return len(vagas)


def vagas_ocupadas(vagas):
    contador = 0
    for vaga in vagas:

        if vaga[2]:
            contador += 1

    return contador


def vagas_livres(vagas):
    contador = 0
    for vaga in vagas:

        if not vaga[2]:
            contador += 1

    return contador
