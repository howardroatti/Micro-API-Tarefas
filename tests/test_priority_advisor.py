from app.services.priority_advisor import _fallback_prioridade


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
