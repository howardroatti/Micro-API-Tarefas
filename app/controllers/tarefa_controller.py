"""Rotas e endpoints REST para o recurso Tarefas."""

from fastapi import APIRouter
from app.models.tarefa import TarefaCreate, TarefaUpdate, TarefaResponse
from app.services.tarefa_service import TarefaService

router = APIRouter(prefix="/api/tarefas", tags=["Tarefas"])
service = TarefaService()


@router.get("/", response_model=list[TarefaResponse])
def listar():
    """Lista todas as tarefas cadastradas."""
    return service.listar_tarefas()


@router.get("/{tarefa_id}", response_model=TarefaResponse)
def buscar(tarefa_id: int):
    """Busca uma tarefa por ID."""
    return service.buscar_tarefa(tarefa_id)


@router.post("/", response_model=TarefaResponse, status_code=201)
def criar(tarefa: TarefaCreate):
    """Cria uma nova tarefa com prioridade sugerida automaticamente."""
    return service.criar_tarefa(tarefa)


@router.put("/{tarefa_id}", response_model=TarefaResponse)
def atualizar(tarefa_id: int, tarefa: TarefaUpdate):
    """Atualiza parcialmente uma tarefa existente."""
    return service.atualizar_tarefa(tarefa_id, tarefa)


@router.delete("/{tarefa_id}", status_code=204)
def deletar(tarefa_id: int):
    """Remove uma tarefa pelo ID."""
    service.deletar_tarefa(tarefa_id)
