# Micro-API de Tarefas

API RESTful para gerenciamento de tarefas com sugestao de prioridade por IA.

Projeto desenvolvido como miniprojeto do curso de Engenharia de Software com GenAI (UFG).

## Indice

- [Stack](#stack)
- [Pre-requisitos](#pre-requisitos)
- [Instalacao](#instalacao)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [PriorityAdvisor](#priorityadvisor)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Testes](#testes)
- [Documentacao](#documentacao)
- [Limitacoes e Proximos Passos](#limitacoes-e-proximos-passos)

## Stack

- Python 3.11+
- FastAPI + Pydantic v2
- SQLite
- Uvicorn
- httpx (chamadas a LLM)
- pytest (testes)
- Claude Code / Anthropic (IA como copiloto de desenvolvimento)

## Pre-requisitos

- Python 3.11 ou superior
- Git

## Instalacao

```bash
# Clonar o repositorio
git clone https://github.com/howardroatti/Micro-API-Tarefas.git
cd Micro-API-Tarefas

# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
# Rodar a API
python -m app.main
```

A API estara disponivel em `http://localhost:8000`.

Swagger UI em `http://localhost:8000/docs`.

### Exemplos com curl

**Criar tarefa:**
```bash
curl -X POST http://localhost:8000/api/tarefas/ \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Implementar login", "descricao": "Adicionar autenticacao JWT"}'
```

**Listar tarefas:**
```bash
curl http://localhost:8000/api/tarefas/
```

**Buscar por ID:**
```bash
curl http://localhost:8000/api/tarefas/1
```

**Atualizar tarefa:**
```bash
curl -X PUT http://localhost:8000/api/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{"concluida": true}'
```

**Deletar tarefa:**
```bash
curl -X DELETE http://localhost:8000/api/tarefas/1
```

## Endpoints

| Metodo | Rota | Descricao | Status |
|--------|------|-----------|--------|
| GET | /api/tarefas/ | Listar todas as tarefas | 200 |
| GET | /api/tarefas/{id} | Buscar tarefa por ID | 200 / 404 |
| POST | /api/tarefas/ | Criar nova tarefa | 201 / 422 |
| PUT | /api/tarefas/{id} | Atualizar tarefa | 200 / 404 |
| DELETE | /api/tarefas/{id} | Deletar tarefa | 204 / 404 |

## PriorityAdvisor

Ao criar uma tarefa, a prioridade e sugerida automaticamente:

- **Com `OPENAI_API_KEY`**: consulta LLM (gpt-4.1-mini) para classificar como alta, media ou baixa.
- **Sem chave ou em caso de erro/timeout**: usa heuristica local por palavras-chave.

O CRUD nunca quebra por causa da IA — falhas sao tratadas silenciosamente com fallback.

```bash
# Para ativar a IA, defina a variavel de ambiente:
export OPENAI_API_KEY=sk-...    # Linux/Mac
set OPENAI_API_KEY=sk-...       # Windows
```

## Estrutura do Projeto

```
app/
├── main.py                 # Entry point FastAPI
├── database.py             # Conexao e init SQLite
├── models/
│   └── tarefa.py           # Schemas Pydantic (Create, Update, Response)
├── controllers/
│   └── tarefa_controller.py  # Rotas e endpoints
├── services/
│   ├── tarefa_service.py     # Logica de negocio
│   └── priority_advisor.py   # IA + fallback de prioridade
└── repositories/
    └── tarefa_repository.py  # Acesso a dados (CRUD SQLite)

tests/
├── test_api.py              # Testes de integracao (endpoints)
└── test_priority_advisor.py # Testes unitarios (fallback)

docs/
├── arquitetura.md           # Diagramas Mermaid
├── decisoes.md              # Registro de decisoes tecnicas
├── prompts.md               # Prompts usados com IA
├── escopo-mvp.md            # Escopo do MVP
├── backlog.md               # Backlog priorizado
├── ebook-unidade-3.md       # Material do curso (Unidade III)
└── ebook-unidade-4.md       # Material do curso (Unidade IV)
```

## Testes

```bash
# Rodar todos os testes
python -m pytest tests/ -v
```

Cobertura atual: 16 testes (11 de API + 5 de PriorityAdvisor).

## Documentacao

- [Arquitetura](docs/arquitetura.md) — diagramas Mermaid
- [Decisoes Tecnicas](docs/decisoes.md) — registro de decisoes
- [Prompts](docs/prompts.md) — prompts usados com IA
- [Escopo do MVP](docs/escopo-mvp.md) — funcionalidades e criterios
- [Backlog](docs/backlog.md) — itens priorizados

## Limitacoes e Proximos Passos

### Limitacoes atuais
- Sem autenticacao ou autorizacao (qualquer pessoa pode acessar)
- Banco de dados SQLite (nao recomendado para producao)
- Sem filtros de busca avancados (por prioridade, status, data)
- Sem paginacao na listagem

### Proximos passos
- Autenticacao com JWT
- Migracao para PostgreSQL
- Filtros e paginacao nos endpoints
- Testes de integracao com a API de IA (mock)
- CI/CD pipeline
- Deploy com Docker
