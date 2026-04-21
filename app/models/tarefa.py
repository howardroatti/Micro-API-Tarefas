from datetime import datetime
from pydantic import BaseModel, Field


class TarefaCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    descricao: str | None = Field(None, max_length=500)


class TarefaUpdate(BaseModel):
    titulo: str | None = Field(None, min_length=3, max_length=100)
    descricao: str | None = Field(None, max_length=500)
    concluida: bool | None = None


class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: str | None
    concluida: bool
    prioridade: str
    created_at: str
