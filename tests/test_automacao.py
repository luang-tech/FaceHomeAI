from database.crud import cadastrar_automacao

cadastrar_automacao(

    residencia_id=1,

    morador_id=1,

    evento="Entrou",

    dispositivo="LED",

    acao="Cor",

    valor="Azul"

)