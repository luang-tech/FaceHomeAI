from database.connection import conectar
from database.models import (
    TABELA_RESIDENCIAS,
    TABELA_MORADORES,
    TABELA_VISITANTES,
    TABELA_DISPOSITIVOS,
    TABELA_AUTOMACOES
)


def criar_banco():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(TABELA_RESIDENCIAS)

    cursor.execute(TABELA_MORADORES)

    cursor.execute(TABELA_VISITANTES)

    cursor.execute(TABELA_DISPOSITIVOS)

    cursor.execute(TABELA_AUTOMACOES)

    conn.commit()

    conn.close()

    print("✅ Banco de dados criado com sucesso!")


if __name__ == "__main__":
    criar_banco()