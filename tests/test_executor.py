from database.crud import buscar_acoes_do_morador
from app.services.executor import executar_acoes

acoes = buscar_acoes_do_morador(
    "Luan Gomes",
    "Entrou"
)

executar_acoes(acoes)