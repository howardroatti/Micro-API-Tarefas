"""Camada de acesso a dados (CRUD) para a tabela de tarefas."""

from app.database import get_connection


class TarefaRepository:
    """Repositorio com operacoes CRUD sobre a tabela tarefas no SQLite."""

    def listar_todas(self):
        """Retorna todas as tarefas como lista de dicionarios."""
        conn = get_connection()
        tarefas = conn.execute("SELECT * FROM tarefas").fetchall()
        conn.close()
        return [dict(t) for t in tarefas]

    def buscar_por_id(self, tarefa_id):
        """Busca tarefa pelo ID. Retorna dict ou None."""
        conn = get_connection()
        tarefa = conn.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,)).fetchone()
        conn.close()
        return dict(tarefa) if tarefa else None

    def criar(self, titulo, descricao="", prioridade="media"):
        """Insere nova tarefa e retorna o registro criado."""
        conn = get_connection()
        cursor = conn.execute(
            "INSERT INTO tarefas (titulo, descricao, prioridade) VALUES (?, ?, ?)",
            (titulo, descricao, prioridade),
        )
        conn.commit()
        tarefa_id = cursor.lastrowid
        conn.close()
        return self.buscar_por_id(tarefa_id)

    def atualizar(self, tarefa_id, titulo=None, descricao=None, concluida=None):
        """Atualiza campos fornecidos, mantendo os demais intactos."""
        tarefa = self.buscar_por_id(tarefa_id)
        if not tarefa:
            return None

        titulo = titulo if titulo is not None else tarefa["titulo"]
        descricao = descricao if descricao is not None else tarefa["descricao"]
        concluida = concluida if concluida is not None else tarefa["concluida"]

        conn = get_connection()
        conn.execute(
            "UPDATE tarefas SET titulo = ?, descricao = ?, concluida = ? WHERE id = ?",
            (titulo, descricao, concluida, tarefa_id),
        )
        conn.commit()
        conn.close()
        return self.buscar_por_id(tarefa_id)

    def deletar(self, tarefa_id):
        """Remove tarefa pelo ID. Retorna True se deletou, False se nao encontrou."""
        tarefa = self.buscar_por_id(tarefa_id)
        if not tarefa:
            return False
        conn = get_connection()
        conn.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        conn.commit()
        conn.close()
        return True
