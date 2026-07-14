from database.connection import conectar

def cadastrar_residencia(
    nome,
    endereco,
    cidade,
    estado,
    telefone,
    email,
    plano="Basic"
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO residencias
        (
            nome,
            endereco,
            cidade,
            estado,
            telefone,
            email,
            plano
        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

    """, (

        nome,
        endereco,
        cidade,
        estado,
        telefone,
        email,
        plano

    ))

    conn.commit()

    conn.close()

    print(f"✅ Residência '{nome}' cadastrada!")
    
def listar_residencias():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM residencias

    """)

    residencias = cursor.fetchall()

    conn.close()

    return residencias

def cadastrar_morador(
    residencia_id,
    nome,
    email,
    telefone,
    cor_led
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO moradores
        (
            residencia_id,
            nome,
            email,
            telefone,
            cor_led
        )

        VALUES (?, ?, ?, ?, ?)

    """, (
        residencia_id,
        nome,
        email,
        telefone,
        cor_led
    ))

    conn.commit()

    conn.close()

    print(f"✅ Morador {nome} cadastrado com sucesso!")

def cadastrar_automacao(
    residencia_id,
    morador_id,
    evento,
    dispositivo,
    acao,
    valor
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO automacoes
        (
            residencia_id,
            morador_id,
            evento,
            dispositivo,
            acao,
            valor
        )

        VALUES (?, ?, ?, ?, ?, ?)

    """, (

        residencia_id,
        morador_id,
        evento,
        dispositivo,
        acao,
        valor

    ))

    conn.commit()

    conn.close()

    print("✅ Automação cadastrada com sucesso!")


def listar_automacoes():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM automacoes

    """)

    automacoes = cursor.fetchall()

    conn.close()

    return automacoes


def buscar_automacoes(morador_id, evento):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM automacoes

        WHERE morador_id = ?

        AND evento = ?

        AND ativo = 1

    """, (

        morador_id,
        evento

    ))

    resultado = cursor.fetchall()

    conn.close()

    return resultado

def buscar_morador_por_nome(nome):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM moradores

        WHERE nome = ?

        AND ativo = 1

    """, (nome,))

    morador = cursor.fetchone()

    conn.close()

    return morador

def buscar_acoes_do_morador(nome, evento):

    morador = buscar_morador_por_nome(nome)

    if morador is None:
        return []

    return buscar_automacoes(
        morador["id"],
        evento
    )
def listar_moradores():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM moradores

    """)

    moradores = cursor.fetchall()

    conn.close()

    return [dict(morador) for morador in moradores]