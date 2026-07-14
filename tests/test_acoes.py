from database.crud import buscar_acoes_do_morador

acoes = buscar_acoes_do_morador(
    "Luan Gomes",
    "Entrou"
)

print("\n===== AÇÕES =====\n")

for acao in acoes:

    print(dict(acao))