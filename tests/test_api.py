import os
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def setup_test_db(tmp_path, monkeypatch):
    """Usa um banco SQLite temporario para cada teste."""
    db_path = str(tmp_path / "test.db")
    monkeypatch.setattr("app.database.DB_PATH", db_path)
    from app.database import init_db
    init_db()


@pytest.fixture
def client():
    from app.main import app
    return TestClient(app)


def test_listar_tarefas_vazio(client):
    response = client.get("/api/tarefas/")
    assert response.status_code == 200
    assert response.json() == []


def test_criar_tarefa_valida(client):
    response = client.post("/api/tarefas/", json={
        "titulo": "Minha tarefa",
        "descricao": "Descricao da tarefa"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Minha tarefa"
    assert data["descricao"] == "Descricao da tarefa"
    assert data["concluida"] is False
    assert data["prioridade"] == "media"
    assert "id" in data


def test_criar_tarefa_sem_titulo_retorna_422(client):
    response = client.post("/api/tarefas/", json={
        "descricao": "Sem titulo"
    })
    assert response.status_code == 422


def test_criar_tarefa_titulo_curto_retorna_422(client):
    response = client.post("/api/tarefas/", json={
        "titulo": "ab"
    })
    assert response.status_code == 422


def test_criar_tarefa_urgente_prioridade_alta(client):
    response = client.post("/api/tarefas/", json={
        "titulo": "Bug urgente no sistema"
    })
    assert response.status_code == 201
    assert response.json()["prioridade"] == "alta"


def test_buscar_tarefa_por_id(client):
    create = client.post("/api/tarefas/", json={"titulo": "Tarefa teste"})
    tarefa_id = create.json()["id"]

    response = client.get(f"/api/tarefas/{tarefa_id}")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarefa teste"


def test_buscar_tarefa_inexistente_retorna_404(client):
    response = client.get("/api/tarefas/999")
    assert response.status_code == 404


def test_atualizar_tarefa(client):
    create = client.post("/api/tarefas/", json={"titulo": "Tarefa original"})
    tarefa_id = create.json()["id"]

    response = client.put(f"/api/tarefas/{tarefa_id}", json={
        "titulo": "Tarefa atualizada"
    })
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarefa atualizada"


def test_atualizar_parcial_mantem_campos(client):
    create = client.post("/api/tarefas/", json={
        "titulo": "Tarefa com descricao",
        "descricao": "Descricao original"
    })
    tarefa_id = create.json()["id"]

    response = client.put(f"/api/tarefas/{tarefa_id}", json={
        "concluida": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Tarefa com descricao"
    assert data["descricao"] == "Descricao original"
    assert data["concluida"] is True


def test_deletar_tarefa(client):
    create = client.post("/api/tarefas/", json={"titulo": "Tarefa para deletar"})
    tarefa_id = create.json()["id"]

    response = client.delete(f"/api/tarefas/{tarefa_id}")
    assert response.status_code == 204

    response = client.get(f"/api/tarefas/{tarefa_id}")
    assert response.status_code == 404


def test_deletar_tarefa_inexistente_retorna_404(client):
    response = client.delete("/api/tarefas/999")
    assert response.status_code == 404
