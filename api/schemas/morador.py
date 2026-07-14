from pydantic import BaseModel


class MoradorCreate(BaseModel):

    residencia_id: int

    nome: str

    email: str

    telefone: str

    cor_led: str