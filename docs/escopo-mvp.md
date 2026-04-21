# Escopo do MVP - Micro-API de Tarefas

## Objetivo

Construir uma Micro-API RESTful para gerenciamento de tarefas com integracao de IA para sugestao de prioridade, seguindo arquitetura em camadas.

## Funcionalidades do MVP

### CRUD de Tarefas (implementado)
- [x] Criar tarefa (titulo, descricao)
- [x] Listar todas as tarefas
- [x] Buscar tarefa por ID
- [x] Atualizar tarefa (titulo, descricao, status)
- [x] Deletar tarefa

### Integracao com IA (pendente)
- [ ] `PriorityAdvisor` — classe que encapsula chamada a LLM
- [ ] Sugestao automatica de prioridade ao criar tarefa
- [ ] Fallback local quando nao houver chave de API
- [ ] Tratamento de timeout e erro de provedor
- [ ] Nunca quebrar o fluxo principal do CRUD

### Documentacao (em andamento)
- [x] Arquitetura com diagramas Mermaid
- [x] Registro de prompts usados com IA
- [x] Escopo do MVP
- [x] Backlog
- [x] Registro de decisoes tecnicas

## Fora do Escopo (MVP)
- Autenticacao / autorizacao
- Frontend / interface grafica
- Deploy em producao
- Banco de dados relacional (PostgreSQL, MySQL)
- Testes automatizados (sera adicionado em iteracao futura)
- Cache / rate limiting

## Criterios de Aceite do MVP
1. API rodando localmente com todos os endpoints funcionais
2. Swagger acessivel em /docs
3. PriorityAdvisor funcionando com fallback
4. Documentacao completa no diretorio /docs
