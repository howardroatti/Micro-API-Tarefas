"""Schemas Pydantic para validacao de entrada e saida da API."""

from datetime import datetime
from pydantic import BaseModel, Field


class TarefaCreate(BaseModel):
    """Schema de criacao de tarefa (entrada do POST)."""

    titulo: str = Field(..., min_length=3, max_length=100)
    descricao: str | None = Field(None, max_length=500)


class TarefaUpdate(BaseModel):
    """Schema de atualizacao parcial de tarefa (entrada do PUT)."""

    titulo: str | None = Field(None, min_length=3, max_length=100)
    descricao: str | None = Field(None, max_length=500)
    concluida: bool | None = None


class TarefaResponse(BaseModel):
    """Schema de resposta da API com todos os campos da tarefa."""

    id: int
    titulo: str
    descricao: str | None
    concluida: bool
    prioridade: str
    created_at: str
