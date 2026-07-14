from database.connection import conectar   # ou database.database, caso ainda não tenha renomeado

conn = conectar()

cursor = conn.cursor()

cursor.execute("SELECT * FROM moradores")

moradores = cursor.fetchall()

print("\n===== MORADORES =====\n")

for morador in moradores:

    print(dict(morador))

conn.close()