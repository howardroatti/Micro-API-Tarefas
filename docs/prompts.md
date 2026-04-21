# Registro de Prompts - Uso de IA no Desenvolvimento

Documentacao dos prompts utilizados com IA (Claude/Anthropic) durante o desenvolvimento do projeto, conforme orientacao do curso.

Ferramenta: Claude Code (Anthropic) — modelo Claude Opus

---

# Capitulo 3 — Prompts para Codex/Copilot

## Prompt 1 — Modelo Pydantic

> Contexto: API de tarefas em FastAPI para uso interno de equipe.
> Objetivo: Gerar modelos TaskCreate, TaskUpdate e TaskOut com tipagem e validacoes.
> Estilo: Pydantic v2, codigo limpo e docstrings curtas.
> Resposta: Apenas codigo de app/models/tarefa.py.

---

## Prompt 2 — Repository

> Contexto: Preciso de persistencia inicial enxuta para viabilizar a primeira release.
> Objetivo: Criar TarefaRepository em memoria com create, list, get_by_id, update e delete.
> Estilo: Python tipado, sem dependencias externas.
> Resposta: Codigo completo de app/repositories/tarefa_repository.py.

---

## Prompt 3 — Service com regra de prioridade

> Contexto: A prioridade da tarefa pode ser sugerida automaticamente.
> Objetivo: Criar TarefaService que use TarefaRepository e PriorityAdvisor.
> Estilo: Separar regra de negocio da camada de API.
> Resposta: Codigo de app/services/tarefa_service.py.

---

## Prompt 4 — PriorityAdvisor com fallback

> Contexto: Quero rodar sem custo de API quando nao houver chave.
> Objetivo: Implementar PriorityAdvisor com heuristica local e chamada opcional a LLM quando OPENAI_API_KEY existir.
> Estilo: Falha segura, timeout e fallback obrigatorio.
> Resposta: Codigo de app/services/priority_advisor.py.

---

## Prompt 5 — Documentacao do projeto

> Contexto: Requisito do curso para documentar arquitetura, prompts, escopo e backlog.
> Objetivo: Gerar documentacao completa com diagramas Mermaid, registro de decisoes e backlog priorizado.
> Estilo: Markdown limpo, tabelas organizadas, diagramas Mermaid.
> Resposta: Arquivos docs/arquitetura.md, docs/prompts.md, docs/escopo-mvp.md, docs/backlog.md, docs/decisoes.md.

---

## Prompt 6 — Revisao tecnica

> Revise os arquivos do core da API e responda:
> 1) Quais pontos de acoplamento estao altos?
> 2) Onde faltam validacoes?
> 3) Quais 5 testes devo priorizar na proxima release?
> Resposta em checklist.

---

---

# Capitulo 4 — Prompts para Codex/Copilot

## Prompt 1 — Testes do service

> Contexto: Tenho TaskService com CRUD de tarefas.
> Objetivo: Gerar suite Pytest cobrindo criacao, listagem, atualizacao, exclusao e caso de erro por ID inexistente.
> Estilo: Testes claros, nomes descritivos e fixtures simples.
> Resposta: Codigo completo de tests/test_task_service.py.

---

## Prompt 2 — Testes do PriorityAdvisor

> Contexto: PriorityAdvisor possui heuristica local e fallback quando chamada externa falha.
> Objetivo: Gerar testes para os tres niveis de prioridade e para o fallback.
> Estilo: Usar monkeypatch quando necessario.
> Resposta: Codigo de tests/test_priority_advisor.py.

---

## Prompt 3 — Testes de API

> Contexto: API FastAPI com endpoints CRUD de /tasks.
> Objetivo: Criar testes de rota com TestClient para status 201, 200, 204 e 404.
> Estilo: Isolar dependencia de repositorio para evitar estado global entre testes.
> Resposta: Codigo de tests/test_task_routes.py.

---

## Prompt 4 — Refatoracao DRY/SRP

> Analise os arquivos app/services/task_service.py e app/repositories/task_repository.py.
> Objetivo: Sugerir refatoracao com foco em DRY e SRP sem mudar comportamento externo.
> Resposta: 1) lista de mudancas propostas 2) patch sugerido por arquivo.

---

## Prompt 5 — README final tecnico

> Contexto: MVP de micro-API de tarefas com prioridade assistida por IA.
> Objetivo: Gerar README completo com instalacao, execucao, testes, arquitetura, uso da IA, limitacoes e proximos passos.
> Estilo: Markdown profissional e objetivo.
> Resposta: README inteiro.

---

## Prompt 6 — Revisao final de qualidade

> Com base no codigo e nos testes atuais, gere um checklist com:
> - Riscos tecnicos restantes
> - Gaps de cobertura de teste
> - Melhorias prioritarias para a proxima release
> Resposta em bullets curtos.

---

> **Nota:** Todos os prompts passaram por revisao humana antes de serem aceitos no codigo. A IA foi usada como copiloto de desenvolvimento (Modo 1), nao como substituto do desenvolvedor.
