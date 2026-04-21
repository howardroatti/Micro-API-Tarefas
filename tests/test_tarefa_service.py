import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from app.services.tarefa_service import TarefaService
from app.models.tarefa import TarefaCreate, TarefaUpdate


@pytest.fixture(autouse=True)
def setup_test_db(tmp_path, monkeypatch):
    """Usa um banco SQLite temporario para cada teste."""
    db_path = str(tmp_path / "test.db")
    monkeypatch.setattr("app.database.DB_PATH", db_path)
    from app.database import init_db
    init_db()


@pytest.fixture
def service():
    return TarefaService()


def test_criar_tarefa_retorna_dados_corretos(service):
    dados = TarefaCreate(titulo="Tarefa nova", descricao="Descricao teste")
    resultado = service.criar_tarefa(dados)

    assert resultado["titulo"] == "Tarefa nova"
    assert resultado["descricao"] == "Descricao teste"
    assert not resultado["concluida"]
    assert resultado["prioridade"] in ("alta", "media", "baixa")
    assert "id" in resultado


def test_criar_tarefa_strip_espacos(service):
    dados = TarefaCreate(titulo="  Tarefa com espacos  ", descricao="  desc  ")
    resultado = service.criar_tarefa(dados)

    assert resultado["titulo"] == "Tarefa com espacos"
    assert resultado["descricao"] == "desc"


def test_criar_tarefa_sem_descricao(service):
    dados = TarefaCreate(titulo="Tarefa sem desc")
    resultado = service.criar_tarefa(dados)

    assert resultado["titulo"] == "Tarefa sem desc"
    assert resultado["descricao"] == ""


def test_criar_tarefa_usa_priority_advisor(service):
    dados = TarefaCreate(titulo="Bug urgente no deploy")
    resultado = service.criar_tarefa(dados)

    assert resultado["prioridade"] == "alta"


def test_listar_tarefas_vazio(service):
    resultado = service.listar_tarefas()
    assert resultado == []


def test_listar_tarefas_com_itens(service):
    service.criar_tarefa(TarefaCreate(titulo="Tarefa um"))
    service.criar_tarefa(TarefaCreate(titulo="Tarefa dois"))

    resultado = service.listar_tarefas()
    assert len(resultado) == 2


def test_buscar_tarefa_existente(service):
    criada = service.criar_tarefa(TarefaCreate(titulo="Tarefa busca"))
    resultado = service.buscar_tarefa(criada["id"])

    assert resultado["titulo"] == "Tarefa busca"


def test_buscar_tarefa_inexistente_levanta_404(service):
    with pytest.raises(HTTPException) as exc_info:
        service.buscar_tarefa(999)
    assert exc_info.value.status_code == 404


def test_atualizar_tarefa_titulo(service):
    criada = service.criar_tarefa(TarefaCreate(titulo="Original"))
    dados = TarefaUpdate(titulo="Atualizado")
    resultado = service.atualizar_tarefa(criada["id"], dados)

    assert resultado["titulo"] == "Atualizado"


def test_atualizar_tarefa_concluida(service):
    criada = service.criar_tarefa(TarefaCreate(titulo="Para concluir"))
    dados = TarefaUpdate(concluida=True)
    resultado = service.atualizar_tarefa(criada["id"], dados)

    assert resultado["concluida"]


def test_atualizar_tarefa_inexistente_levanta_404(service):
    dados = TarefaUpdate(titulo="Nao existe")
    with pytest.raises(HTTPException) as exc_info:
        service.atualizar_tarefa(999, dados)
    assert exc_info.value.status_code == 404


def test_deletar_tarefa_existente(service):
    criada = service.criar_tarefa(TarefaCreate(titulo="Para deletar"))
    service.deletar_tarefa(criada["id"])

    with pytest.raises(HTTPException):
        service.buscar_tarefa(criada["id"])


def test_deletar_tarefa_inexistente_levanta_404(service):
    with pytest.raises(HTTPException) as exc_info:
        service.deletar_tarefa(999)
    assert exc_info.value.status_code == 404
