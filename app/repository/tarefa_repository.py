from app.model import get_connection


class TarefaRepository:

    def listar_todas(self):
        conn = get_connection()
        tarefas = conn.execute("SELECT * FROM tarefas").fetchall()
        conn.close()
        return [dict(t) for t in tarefas]

    def buscar_por_id(self, tarefa_id):
        conn = get_connection()
        tarefa = conn.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,)).fetchone()
        conn.close()
        return dict(tarefa) if tarefa else None

    def criar(self, titulo, descricao=""):
        conn = get_connection()
        cursor = conn.execute(
            "INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)",
            (titulo, descricao),
        )
        conn.commit()
        tarefa_id = cursor.lastrowid
        conn.close()
        return self.buscar_por_id(tarefa_id)

    def atualizar(self, tarefa_id, titulo=None, descricao=None, concluida=None):
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
        tarefa = self.buscar_por_id(tarefa_id)
        if not tarefa:
            return False
        conn = get_connection()
        conn.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        conn.commit()
        conn.close()
        return True
