from fastapi import HTTPException
from app.repository.tarefa_repository import TarefaRepository
from app.schemas import TarefaCreate, TarefaUpdate


class TarefaService:

    def __init__(self):
        self.repository = TarefaRepository()

    def listar_tarefas(self):
        return self.repository.listar_todas()

    def buscar_tarefa(self, tarefa_id: int):
        tarefa = self.repository.buscar_por_id(tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return tarefa

    def criar_tarefa(self, dados: TarefaCreate):
        return self.repository.criar(dados.titulo.strip(), dados.descricao.strip())

    def atualizar_tarefa(self, tarefa_id: int, dados: TarefaUpdate):
        tarefa = self.repository.buscar_por_id(tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return self.repository.atualizar(
            tarefa_id,
            titulo=dados.titulo,
            descricao=dados.descricao,
            concluida=dados.concluida,
        )

    def deletar_tarefa(self, tarefa_id: int):
        if not self.repository.deletar(tarefa_id):
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
