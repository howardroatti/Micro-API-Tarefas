# Arquitetura - Micro-API de Tarefas

## Visao Geral

Micro-API RESTful para gerenciamento de tarefas, construida com FastAPI + Pydantic, seguindo arquitetura em camadas.

## Stack

- **Linguagem:** Python 3.11+
- **Framework:** FastAPI
- **Validacao:** Pydantic
- **Banco de dados:** SQLite
- **Servidor:** Uvicorn

## Diagrama de Camadas

```mermaid
graph TD
    Client([Client]) -->|HTTP Request| Controller
    Controller -->|Schemas Pydantic| Service
    Service -->|Logica de Negocio| Repository
    Repository -->|SQL| DB[(SQLite)]
    DB -->|Rows| Repository
    Repository -->|Dict| Service
    Service -->|Dict| Controller
    Controller -->|JSON Response| Client
```

## Estrutura de Diretórios

```mermaid
graph LR
    subgraph app
        main.py
        database.py
        subgraph models
            tarefa.py
        end
        subgraph controllers
            tarefa_controller.py
        end
        subgraph services
            tarefa_service.py
            priority_advisor.py
        end
        subgraph repositories
            tarefa_repository.py
        end
    end
    subgraph docs
        arquitetura.md
        decisoes.md
        prompts.md
        escopo-mvp.md
        backlog.md
    end
```

## Fluxo de uma Requisicao (exemplo: criar tarefa)

```mermaid
sequenceDiagram
    participant C as Client
    participant CT as Controller
    participant S as Service
    participant R as Repository
    participant DB as SQLite

    C->>CT: POST /api/tarefas (JSON)
    CT->>CT: Valida via TarefaCreate (Pydantic)
    CT->>S: criar_tarefa(dados)
    S->>R: criar(titulo, descricao)
    R->>DB: INSERT INTO tarefas
    DB-->>R: lastrowid
    R->>DB: SELECT * WHERE id = ?
    DB-->>R: row
    R-->>S: dict
    S-->>CT: dict
    CT-->>C: 201 Created (JSON)
```

## Fluxo Futuro com PriorityAdvisor

```mermaid
graph TD
    Client([Client]) -->|POST /api/tarefas| Controller
    Controller --> Service
    Service --> PriorityAdvisor
    PriorityAdvisor -->|Tem chave API?| Decision{Chave disponivel?}
    Decision -->|Sim| LLM[API de IA - Anthropic/OpenAI]
    Decision -->|Nao| Fallback[Regra Local de Prioridade]
    LLM -->|Timeout/Erro| Fallback
    LLM -->|Sugestao| Service
    Fallback -->|Prioridade padrao| Service
    Service --> Repository
    Repository --> DB[(SQLite)]
```

## Endpoints da API

| Metodo | Rota | Descricao | Status |
|--------|------|-----------|--------|
| GET | /api/tarefas | Listar todas as tarefas | 200 |
| GET | /api/tarefas/{id} | Buscar tarefa por ID | 200 / 404 |
| POST | /api/tarefas | Criar nova tarefa | 201 / 400 |
| PUT | /api/tarefas/{id} | Atualizar tarefa | 200 / 404 |
| DELETE | /api/tarefas/{id} | Deletar tarefa | 204 / 404 |

## Principios

- **Resiliencia:** IA nunca quebra o fluxo principal do CRUD
- **Coesao:** Cada camada tem responsabilidade unica
- **Testabilidade:** Camadas desacopladas facilitam testes unitarios
