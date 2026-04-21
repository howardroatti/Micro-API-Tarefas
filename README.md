# Micro-API de Tarefas

API RESTful para gerenciamento de tarefas com sugestao de prioridade por IA.

Projeto desenvolvido como miniprojeto do curso de Engenharia de Software com GenAI (UFG).

## Stack

- Python 3.11+
- FastAPI + Pydantic
- SQLite
- Uvicorn
- httpx (chamadas a LLM)

## Arquitetura

```
Client -> Controllers -> Services -> Repositories -> DB (SQLite)
                            |
                     PriorityAdvisor
                      |          |
                   LLM (API)   Fallback local
```

Detalhes em [docs/arquitetura.md](docs/arquitetura.md).

## Como rodar

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Rodar a API
python -m app.main
```

A API estara disponivel em `http://localhost:8000`.

Swagger UI em `http://localhost:8000/docs`.

## Endpoints

| Metodo | Rota | Descricao |
|--------|------|-----------|
| GET | /api/tarefas | Listar todas |
| GET | /api/tarefas/{id} | Buscar por ID |
| POST | /api/tarefas | Criar tarefa |
| PUT | /api/tarefas/{id} | Atualizar tarefa |
| DELETE | /api/tarefas/{id} | Deletar tarefa |

## PriorityAdvisor

Ao criar uma tarefa, a prioridade e sugerida automaticamente:

- **Com `OPENAI_API_KEY`**: consulta LLM (gpt-4.1-mini) para classificar como alta, media ou baixa.
- **Sem chave ou em caso de erro/timeout**: usa heuristica local por palavras-chave.

```bash
# Para ativar a IA, defina a variavel de ambiente:
export OPENAI_API_KEY=sk-...
```

## Documentacao

- [Arquitetura](docs/arquitetura.md) — diagramas Mermaid
- [Decisoes Tecnicas](docs/decisoes.md) — registro de decisoes
- [Prompts](docs/prompts.md) — prompts usados com IA
- [Escopo do MVP](docs/escopo-mvp.md) — funcionalidades e criterios
- [Backlog](docs/backlog.md) — itens priorizados
