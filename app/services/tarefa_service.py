"""Camada de servico com logica de negocio para Tarefas."""

from fastapi import HTTPException
from app.repositories.tarefa_repository import TarefaRepository
from app.services.priority_advisor import sugerir_prioridade
from app.models.tarefa import TarefaCreate, TarefaUpdate


class TarefaService:
    """Orquestra regras de negocio entre controller e repository."""

    def __init__(self):
        self.repository = TarefaRepository()

    def listar_tarefas(self):
        """Retorna todas as tarefas do banco."""
        return self.repository.listar_todas()

    def buscar_tarefa(self, tarefa_id: int):
        """Busca uma tarefa por ID ou levanta 404."""
        tarefa = self.repository.buscar_por_id(tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
        return tarefa

    def criar_tarefa(self, dados: TarefaCreate):
        """Cria tarefa com prioridade sugerida pelo PriorityAdvisor."""
        prioridade = sugerir_prioridade(dados.titulo, dados.descricao)
        return self.repository.criar(
            dados.titulo.strip(),
            (dados.descricao or "").strip(),
            prioridade,
        )

    def atualizar_tarefa(self, tarefa_id: int, dados: TarefaUpdate):
        """Atualiza campos enviados, mantendo os demais inalterados."""
        tarefa = self.repository.buscar_por_id(tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
        return self.repository.atualizar(
            tarefa_id,
            titulo=dados.titulo,
            descricao=dados.descricao,
            concluida=dados.concluida,
        )

    def deletar_tarefa(self, tarefa_id: int):
        """Remove tarefa ou levanta 404 se nao encontrada."""
        if not self.repository.deletar(tarefa_id):
            raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
