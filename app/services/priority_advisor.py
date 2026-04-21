import os
import httpx


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TIMEOUT_SECONDS = 10


def _fallback_prioridade(titulo: str, descricao: str | None) -> str:
    """Heuristica local para sugerir prioridade sem depender de IA."""
    texto = f"{titulo} {descricao or ''}".lower()
    palavras_alta = ["urgente", "critico", "bug", "erro", "falha", "seguranca"]
    palavras_baixa = ["melhoria", "refatorar", "documentar", "limpeza", "ajuste"]

    if any(p in texto for p in palavras_alta):
        return "alta"
    if any(p in texto for p in palavras_baixa):
        return "baixa"
    return "media"


def sugerir_prioridade(titulo: str, descricao: str | None) -> str:
    """Sugere prioridade usando LLM se disponivel, senao usa fallback local."""
    if not OPENAI_API_KEY:
        return _fallback_prioridade(titulo, descricao)

    try:
        response = httpx.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4.1-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "Voce e um assistente que classifica prioridade de tarefas. "
                            "Responda APENAS com uma palavra: alta, media ou baixa."
                        ),
                    },
                    {
                        "role": "user",
                        "content": f"Titulo: {titulo}\nDescricao: {descricao or 'sem descricao'}",
                    },
                ],
                "max_tokens": 10,
                "temperature": 0,
            },
            timeout=TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        resposta = response.json()["choices"][0]["message"]["content"].strip().lower()
        if resposta in ("alta", "media", "baixa"):
            return resposta
        return _fallback_prioridade(titulo, descricao)
    except Exception:
        return _fallback_prioridade(titulo, descricao)
