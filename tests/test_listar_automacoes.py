from database.crud import listar_automacoes

print("\n===== AUTOMAÇÕES =====\n")

for automacao in listar_automacoes():

    print(dict(automacao))