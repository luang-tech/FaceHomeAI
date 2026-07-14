from database.crud import buscar_morador_por_nome

morador = buscar_morador_por_nome("Luan Gomes")

print(dict(morador))