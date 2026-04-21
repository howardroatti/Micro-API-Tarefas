# Registro de Decisoes Tecnicas

## 001 - Framework: FastAPI + Pydantic
- **Data:** 2026-04-21
- **Decisao:** Usar FastAPI com Pydantic em vez de Flask.
- **Motivo:** Requisito do curso (async, tipagem forte, docs automatica via Swagger/OpenAPI).

## 002 - Banco de dados: SQLite
- **Data:** 2026-04-21
- **Decisao:** Usar SQLite como banco de dados do MVP.
- **Motivo:** Simplicidade para prototipacao, sem necessidade de servidor externo.

## 003 - Arquitetura em camadas
- **Data:** 2026-04-21
- **Decisao:** Controller -> Service -> Repository -> DB.
- **Motivo:** Separacao de responsabilidades conforme orientacao do curso. Controller cuida das rotas, Service da logica de negocio, Repository do acesso a dados.

## 004 - Conventional Commits
- **Data:** 2026-04-21
- **Decisao:** Usar conventional commits (feat, fix, refactor, docs, chore).
- **Motivo:** Padronizacao do historico de commits e rastreabilidade das mudancas.
