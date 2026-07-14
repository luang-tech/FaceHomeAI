from fastapi import APIRouter

from database.crud import (
    listar_moradores,
    cadastrar_morador
)

from api.schemas.morador import MoradorCreate

router = APIRouter()


@router.get("/moradores")
def obter_moradores():

    moradores = listar_moradores()

    return moradores


@router.post("/moradores")
def criar_morador(morador: MoradorCreate):

    cadastrar_morador(

        residencia_id=morador.residencia_id,
        nome=morador.nome,
        email=morador.email,
        telefone=morador.telefone,
        cor_led=morador.cor_led

    )

    return {"mensagem": "Morador cadastrado com sucesso!"}