from database.crud import listar_residencias

print("\n===== RESIDÊNCIAS =====\n")

for residencia in listar_residencias():

    print(dict(residencia))