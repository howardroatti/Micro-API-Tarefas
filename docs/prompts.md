# Registro de Prompts - Uso de IA no Desenvolvimento

Documentacao dos prompts utilizados com IA (Claude/Anthropic) durante o desenvolvimento do projeto, conforme orientacao do curso.

Ferramenta: Claude Code (Anthropic) — modelo Claude Opus

---

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

> **Nota:** Todos os prompts passaram por revisao humana antes de serem aceitos no codigo. A IA foi usada como copiloto de desenvolvimento (Modo 1), nao como substituto do desenvolvedor.
