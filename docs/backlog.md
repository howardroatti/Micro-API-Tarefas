# Backlog - Micro-API de Tarefas

## Legenda de Prioridade
- **P0** — Obrigatorio para o MVP
- **P1** — Desejavel para o MVP
- **P2** — Futuro (pos-MVP)

## Legenda de Status
- TODO — Nao iniciado
- IN PROGRESS — Em andamento
- DONE — Concluido

---

## P0 — MVP Obrigatorio

| # | Tarefa | Status |
|---|--------|--------|
| 1 | CRUD completo de tarefas (criar, listar, buscar, atualizar, deletar) | DONE |
| 2 | Arquitetura em camadas (Controller -> Service -> Repository) | DONE |
| 3 | Schemas Pydantic (TarefaCreate, TarefaUpdate, TarefaResponse) | DONE |
| 4 | PriorityAdvisor — chamada a LLM para sugerir prioridade | TODO |
| 5 | Fallback local de prioridade (sem chave de API) | TODO |
| 6 | Tratamento de timeout/erro no PriorityAdvisor | TODO |
| 7 | Campo `prioridade` no modelo de tarefa | TODO |
| 8 | Documentacao de arquitetura (Mermaid) | DONE |
| 9 | Registro de prompts | DONE |
| 10 | Escopo do MVP documentado | DONE |
| 11 | Backlog documentado | DONE |
| 12 | Registro de decisoes tecnicas | DONE |

## P1 — Desejavel para o MVP

| # | Tarefa | Status |
|---|--------|--------|
| 13 | Variavel de ambiente para configurar provedor de IA | TODO |
| 14 | Endpoint para re-calcular prioridade de tarefa existente | TODO |
| 15 | Filtrar tarefas por prioridade | TODO |

## P2 — Futuro (pos-MVP)

| # | Tarefa | Status |
|---|--------|--------|
| 16 | Testes unitarios e de integracao | TODO |
| 17 | Migracao para PostgreSQL | TODO |
| 18 | Autenticacao (JWT) | TODO |
| 19 | Deploy (Docker + cloud) | TODO |
| 20 | CI/CD pipeline | TODO |
| 21 | Frontend basico | TODO |
| 22 | Rate limiting na chamada de IA | TODO |
