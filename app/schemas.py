from pydantic import BaseModel, Field


class TarefaCreate(BaseModel):
    titulo: str = Field(..., min_length=1)
    descricao: str = ""


class TarefaUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    concluida: bool | None = None


class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: bool
