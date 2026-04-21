from unittest.mock import patch
import httpx
from app.services.priority_advisor import _fallback_prioridade, sugerir_prioridade


# --- Testes do fallback local ---

def test_fallback_retorna_alta_para_palavras_urgentes():
    assert _fallback_prioridade("Bug critico em producao", None) == "alta"
    assert _fallback_prioridade("Erro no login", "falha de autenticacao") == "alta"
    assert _fallback_prioridade("Tarefa urgente", "") == "alta"


def test_fallback_retorna_baixa_para_melhorias():
    assert _fallback_prioridade("Refatorar servico de tarefas", None) == "baixa"
    assert _fallback_prioridade("Documentar API", "") == "baixa"
    assert _fallback_prioridade("Limpeza de codigo legado", None) == "baixa"


def test_fallback_retorna_media_para_tarefas_comuns():
    assert _fallback_prioridade("Criar endpoint de usuarios", None) == "media"
    assert _fallback_prioridade("Implementar filtro por status", "nova feature") == "media"


def test_fallback_ignora_case():
    assert _fallback_prioridade("URGENTE: deploy", None) == "alta"
    assert _fallback_prioridade("MELHORIA no dashboard", None) == "baixa"


def test_fallback_com_descricao_none():
    assert _fallback_prioridade("Tarefa normal", None) == "media"


# --- Testes de sugerir_prioridade com monkeypatch ---

def test_sugerir_prioridade_sem_api_key_usa_fallback(monkeypatch):
    monkeypatch.setattr("app.services.priority_advisor.OPENAI_API_KEY", None)
    resultado = sugerir_prioridade("Bug urgente", None)
    assert resultado == "alta"


def test_sugerir_prioridade_com_timeout_usa_fallback(monkeypatch):
    monkeypatch.setattr("app.services.priority_advisor.OPENAI_API_KEY", "fake-key")

    def mock_post(*args, **kwargs):
        raise httpx.TimeoutException("timeout")

    monkeypatch.setattr("httpx.post", mock_post)
    resultado = sugerir_prioridade("Tarefa normal", None)
    assert resultado == "media"


def test_sugerir_prioridade_com_erro_http_usa_fallback(monkeypatch):
    monkeypatch.setattr("app.services.priority_advisor.OPENAI_API_KEY", "fake-key")

    def mock_post(*args, **kwargs):
        raise httpx.HTTPStatusError("500", request=None, response=None)

    monkeypatch.setattr("httpx.post", mock_post)
    resultado = sugerir_prioridade("Documentar API", None)
    assert resultado == "baixa"


def test_sugerir_prioridade_resposta_invalida_usa_fallback(monkeypatch):
    monkeypatch.setattr("app.services.priority_advisor.OPENAI_API_KEY", "fake-key")

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return {"choices": [{"message": {"content": "invalido"}}]}

    monkeypatch.setattr("httpx.post", lambda *a, **kw: MockResponse())
    resultado = sugerir_prioridade("Tarefa comum", None)
    assert resultado == "media"


def test_sugerir_prioridade_resposta_valida(monkeypatch):
    monkeypatch.setattr("app.services.priority_advisor.OPENAI_API_KEY", "fake-key")

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return {"choices": [{"message": {"content": "alta"}}]}

    monkeypatch.setattr("httpx.post", lambda *a, **kw: MockResponse())
    resultado = sugerir_prioridade("Qualquer tarefa", None)
    assert resultado == "alta"
