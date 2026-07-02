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

def livres_por_categoria(vagas):
    comum = 0
    idoso = 0
    pcd = 0

    for vaga in vagas:
        if not vaga[2]:
            if vaga[1] == "comum":
                comum += 1
            elif vaga[1] == "idoso":
                idoso += 1
            elif vaga[1] == "pcd":
                pcd += 1

    return comum, idoso, pcd

def situacao_estacionamento(vagas):
    livres = vagas_livres(vagas)

    if livres == 0:
        return "Lotado"
    elif livres <= 2:
        return "Quase lotado"
    else:
        return "Disponível"

def buscar_vaga(vagas, numero):
    for vaga in vagas:
        if vaga[0] == numero:
            if vaga[2]:
                return "Vaga ocupada."
            else:
                return "Vaga livre."
    return "Vaga não encontrada."

print("Total de vagas:", total_vagas(vagas))
print("Vagas ocupadas:", vagas_ocupadas(vagas))
print("Vagas livres:", vagas_livres(vagas))

comum, idoso, pcd = livres_por_categoria(vagas)

print("\nVagas livres por categoria:")
print("Comum:", comum)
print("Idoso:", idoso)
print("PCD:", pcd)


print("\nSituação do estacionamento:", situacao_estacionamento(vagas))

numero = int(input("\nDigite o número da vaga para buscar: "))
print(buscar_vaga(vagas, numero))

