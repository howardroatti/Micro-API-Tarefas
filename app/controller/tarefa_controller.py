from fastapi import APIRouter
from app.schemas import TarefaCreate, TarefaUpdate, TarefaResponse
from app.service.tarefa_service import TarefaService

router = APIRouter(prefix="/api/tarefas", tags=["Tarefas"])
service = TarefaService()


@router.get("/", response_model=list[TarefaResponse])
def listar():
    return service.listar_tarefas()


@router.get("/{tarefa_id}", response_model=TarefaResponse)
def buscar(tarefa_id: int):
    return service.buscar_tarefa(tarefa_id)


@router.post("/", response_model=TarefaResponse, status_code=201)
def criar(tarefa: TarefaCreate):
    return service.criar_tarefa(tarefa)


@router.put("/{tarefa_id}", response_model=TarefaResponse)
def atualizar(tarefa_id: int, tarefa: TarefaUpdate):
    return service.atualizar_tarefa(tarefa_id, tarefa)


@router.delete("/{tarefa_id}", status_code=204)
def deletar(tarefa_id: int):
    service.deletar_tarefa(tarefa_id)
