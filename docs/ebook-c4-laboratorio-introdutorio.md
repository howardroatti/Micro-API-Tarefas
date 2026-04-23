# Laboratório Introdutório: Construindo um Miniprojeto com Inteligência Artificial Generativa

**Autores:** Leon Sólon da Silva, Sofia Costa Paiva, Mariana Soller Ramada, Arlindo Rodrigues Galvão Filho, Renata Dutra Braga, Taciana Novo Kudo

**Instituições responsáveis:** Universidade Federal de Goiás (UFG); Centro de Competência Embrapii em Tecnologias Imersivas - AKCIT (Advanced Knowledge Center for Immersive Technologies); Centro de Excelência em Inteligência Artificial (CEIA).

**Instituições financiadoras:** Empresa Brasileira de Pesquisa e Inovação Industrial (Embrapii); Governo do Estado de Goiás; Empresas parceiras do AKCIT.

**Apoio:** Universidade Federal de Goiás (UFG); Pró-Reitoria de Pesquisa e Inovação (PRPI-UFG); Instituto de Informática (INF-UFG).

© Cegraf UFG, 2026 · © Universidade Federal de Goiás, 2026 · © AKCIT, 2026.

---

## Lista de Abreviaturas e Siglas

- **AKCIT** — Centro de Competência Embrapii em Tecnologias Imersivas
- **API** — Application Programming Interface (Interface de Programação de Aplicações)
- **CLI** — Command-Line Interface (Interface de Linha de Comando)
- **CoT** — Chain-of-thought (Cadeia de Raciocínio)
- **CRUD** — Create, Read, Update, Delete
- **DRY** — Don't Repeat Yourself
- **Embrapii** — Empresa Brasileira de Pesquisa e Inovação Industrial
- **genAI** — Generative Artificial Intelligence (Inteligência Artificial Generativa)
- **GIF** — Graphics Interchange Format
- **IA** — Inteligência Artificial
- **IDE** — Integrated Development Environment
- **I/O** — Input/Output
- **LLM** — Large Language Models
- **MVP** — Minimum Viable Product
- **NIST** — National Institute of Standards and Technology
- **NLDD** — Natural Language Driven Development
- **ORM** — Object-Relational Mapping
- **PEP** — Python Enhancement Proposal
- **PRDs** — Product Requirements Documents
- **RAG** — Retrieval Augmented Generation
- **SOLID** — Single Responsibility / Open-Closed / Liskov Substitution / Interface Segregation / Dependency Inversion
- **TDD** — Test-Driven Development
- **UFG** — Universidade Federal de Goiás
- **UI** — User Interface
- **URL** — Uniform Resource Locator
- **UUID** — Universally Unique Identifier
- **VS Code** — Visual Studio Code
- **XSS** — Cross-Site Scripting

---

## Apresentação

Prezado/a Participante,

Seja muito bem-vindo/a ao ebook *Laboratório Introdutório: Construindo um Miniprojeto com Inteligência Artificial Generativa!* Este material didático foi cuidadosamente elaborado como um componente essencial da Trilha de Introdução Prática, parte integrante do prestigiado Curso de Especialização em Engenharia de Software: Automação e Inovação com Inteligência Artificial Generativa. Essa iniciativa representa uma colaboração estratégica entre o AKCIT, a Embrapii e a UFG, visando capacitar profissionais para os desafios e oportunidades da era da inteligência artificial (IA).

Vivemos um momento de profunda transformação tecnológica, onde a inteligência artificial generativa (genAI) não é mais uma promessa futurista, mas uma realidade que redefine os paradigmas do desenvolvimento de software. Desde o surgimento dos primeiros modelos de linguagem de grande escala (LLMs), no início da década de 2020, a maneira como os engenheiros de software concebem, projetam, implementam e mantêm sistemas tem sido revolucionada. Em 2026, ferramentas avançadas, como o GPT-5.3 Codex® da OpenAI® e o Claude 4.6® (nas versões Sonnet e Opus) da Anthropic®, transcenderam o papel de meros assistentes de autocompletar código, tornando-se parceiros de programação capazes de realizar raciocínio complexo, auxiliar na arquitetura de sistemas e até mesmo gerenciar fluxos de trabalho autônomos de desenvolvimento (Garcia, 2025).

O objetivo primordial deste ebook é proporcionar uma jornada prática e imersiva. Nosso foco não se restringe à explanação teórica; pelo contrário, almejamos que, ao final desta leitura e da execução das atividades propostas, você seja capaz de planejar, implementar e publicar um miniprojeto funcional no GitHub. Para isso, utilizaremos as ferramentas e metodologias mais modernas e eficazes disponíveis no mercado. Abordaremos desde a configuração otimizada do ambiente de desenvolvimento no VS Code® e no Cursor® IDE, passando pelas técnicas avançadas de engenharia de prompts até à entrega final do projeto com documentação robusta e aderente às melhores práticas.

A genAI, embora ofereça ganhos exponenciais em produtividade e inovação, também introduz novos desafios éticos, de segurança e técnicos. Conforme destacado por Banh et al. (2025), a prática do "copiloting" no futuro da engenharia de software exige que o desenvolvedor contemporâneo evolua de um simples codificador para um revisor crítico, um arquiteto de soluções e um estrategista de IA. Este material foi estruturado para cultivar essa mentalidade crítica e proativa, garantindo que você empregue a IA como um catalisador para sua criatividade e eficiência, sem jamais comprometer a qualidade, a segurança e a integridade do software que você produz.

Desejamos a você um estudo enriquecedor e uma experiência prática verdadeiramente transformadora! Que este laboratório seja o ponto de partida para sua maestria na engenharia de software assistida por genAI!

---

## Unidade I — Fundamentos, Ambiente e Prompts para Programação

A Unidade I é o alicerce sobre o qual construiremos todo o seu conhecimento e habilidades em genAI aplicada ao desenvolvimento de software. Compreender os princípios subjacentes aos modelos de IA, familiarizar-se com o ambiente de desenvolvimento otimizado e dominar a arte da engenharia de prompts são passos cruciais e indispensáveis para o sucesso em qualquer projeto que envolva assistência de IA.

### 1.1 Visão Prática de Inteligência Artificial Generativa no Desenvolvimento (Assistentes e Limites)

A genAI tem transformado o cenário do desenvolvimento de software de maneira sem precedentes. O que antes era um campo dominado por modelos de predição de texto e autocompletar, hoje se expandiu para sistemas de raciocínio lógico e capacidades agênticas altamente sofisticadas. Atualmente, o ecossistema de desenvolvimento é impulsionado por modelos de "fronteira" que não apenas sugerem trechos de código, mas são capazes de planejar, executar e monitorar tarefas complexas em ambientes de desenvolvimento, atuando como verdadeiros agentes autônomos (Anchan, 2025).

#### 1.1.1 A Evolução Exponencial dos Modelos de Linguagem: do GPT-3® ao GPT-5.3 Codex® e Claude 4.6®

Para apreciar o estado atual da arte, é fundamental revisitar a trajetória de evolução dos LLMs nos últimos anos. O que começou com modelos como o GPT-3®, que demonstravam uma impressionante capacidade de geração de texto coerente, rapidamente progrediu para sistemas especializados em código.

O GPT-3.5 Codex® (lançado em 2021) foi um marco, sendo o motor por trás do GitHub Copilot® original. Ele foi treinado em uma vasta quantidade de código-fonte público, permitindo-lhe gerar sugestões de código, completar funções e até mesmo traduzir comentários em código. No entanto, suas capacidades eram limitadas a trechos menores e exigiam muita supervisão humana.

Com o avanço para o GPT-4® e suas variantes, a capacidade de raciocínio e a janela de contexto dos modelos aumentaram exponencialmente. Isso permitiu que os assistentes de código começassem a entender não apenas a linha atual, mas o contexto de arquivos inteiros e até mesmo de pequenos projetos.

Em 2026, a OpenAI® lançou o GPT-5.3 Codex®, um modelo que representa um salto qualitativo. Esse modelo não se limita a completar código, ele possui uma compreensão profunda das dependências entre múltiplos arquivos; é capaz de depurar, refatorar e até mesmo escrever documentação técnica de alta qualidade. Sua velocidade de inferência foi otimizada para ambientes de codificação em tempo real, e suas capacidades agênticas permitem que ele execute tarefas de ponta a ponta no ciclo de vida do software, desde a escrita de PRDs até o monitoramento de deploy (OpenAI, 2026).

Paralelamente, a Anthropic® tem desenvolvido a família de modelos Claude®, com um foco particular em segurança, interpretabilidade e raciocínio contextual. O Claude 4.6®, lançado em 2026, apresenta duas variantes principais que são de interesse para desenvolvedores:

- **Claude 4.6 Sonnet®:** Projetado para ser um modelo de alto desempenho e custo-benefício, ideal para tarefas de codificação diárias, como geração de funções, refatoração de pequenos módulos e escrita de testes unitários. Oferece um equilíbrio entre velocidade e capacidade de raciocínio (Anthropic, 2026a).
- **Claude 4.6 Opus®:** A versão mais avançada da Anthropic®, otimizada para tarefas que exigem raciocínio complexo, planejamento estratégico e manipulação de grandes bases de código. Sua capacidade de "extended thinking" permite planejar sequências de refatoração, identificar e corrigir bugs arquiteturais e atuar como um arquiteto de software virtual (Anthropic, 2026b).

**Tabela 1 — Características dos principais modelos de linguagem GPT-5.3 Codex® e Claude 4.6®**

| Característica | GPT-5.3 Codex® (OpenAI®) | Claude 4.6 Sonnet® (Anthropic®) | Claude 4.6 Opus® (Anthropic®) |
|---|---|---|---|
| Foco principal | Ciclo de vida completo do software, depuração, deploy, PRDs | Codificação diária, refatoração de módulos, testes unitários | Raciocínio complexo, arquitetura, depuração profunda, agentes |
| Janela de contexto | Muito grande, otimizada para múltiplos arquivos e projetos | Grande, focada em módulos e arquivos específicos | Extremamente grande (até 1M tokens em beta), para projetos inteiros |
| Velocidade | Alta, feedback quase instantâneo | Rápida, excelente para interações ágeis | Moderada a alta, prioriza profundidade de raciocínio |
| Capacidades agênticas | Avançadas, execução de ponta a ponta | Boas, para tarefas bem definidas | Superiores, planejamento e execução de tarefas complexas |
| Segurança | Foco em identificação de vulnerabilidades (cybersecurity) | Forte ênfase em segurança e interpretabilidade | Forte ênfase em segurança e interpretabilidade |

#### 1.1.2 Assistentes de Código e Seus Limites: Onde a Inteligência Artificial Brilha e Onde Ela Falha

Embora os assistentes de código baseados em genAI sejam ferramentas poderosas, é crucial entender suas capacidades e, mais importante, suas limitações. A IA não possui consciência, intenção ou a capacidade de compreender nuances culturais ou comerciais que não foram explicitamente codificadas em seus dados de treinamento. O desenvolvedor humano continua sendo o elo crítico para a tomada de decisões estratégicas e a validação final.

**Onde a IA brilha:**

- **Geração de boilerplate:** código repetitivo, como configurações de API, modelos de dados, CRUD básico.
- **Autocompletar inteligente:** sugestões de código contextuais que aceleram a escrita.
- **Refatoração:** identificação de padrões para melhoria de código, aplicação de princípios SOLID, DRY.
- **Geração de testes:** criação de testes unitários e de integração para cobrir funcionalidades existentes.
- **Documentação:** geração de docstrings, comentários e seções de README.
- **Tradução de linguagens:** converter código de uma linguagem para outra (ex.: Python® para Go).
- **Exploração de APIs:** sugerir como usar uma API com base em sua documentação.

**Onde a IA falha (limitações e riscos):**

- **Alucinações técnicas:** A IA pode gerar código que parece plausível, mas é semanticamente incorreto, usa bibliotecas inexistentes, métodos depreciados ou sintaxe inválida. Exige validação humana rigorosa.
- **Segurança e privacidade:** O envio de código proprietário para modelos de nuvem pode violar políticas de segurança e privacidade. Utilize soluções empresariais ou evite enviar dados críticos (OWASP, 2025). A OWASP Foundation publicou o *OWASP Top 10 para Aplicações LLM (2025)*, destacando riscos como injeção de prompt, vazamento de dados sensíveis e negação de serviço.
- **Viés de treinamento e qualidade do código:** Se os datasets de treinamento contiverem código de baixa qualidade ou vulnerabilidades, a IA pode replicá-los. O código gerado pode não aderir às melhores práticas, exigindo refatoração e revisão humana (Peng et al., 2023).
- **Dependência excessiva:** A confiança cega na IA pode diminuir as habilidades do desenvolvedor. Use a IA como ferramenta de aumento, não de substituição.
- **Custo e complexidade:** A integração e manutenção de modelos de ponta podem ser caras e exigem infraestrutura robusta.

Como ressaltado pelo NIST em seu *Artificial Intelligence Risk Management Framework: Generative AI Profile (NIST AI 600-1)* (NIST, 2024), a gestão de riscos em genAI deve ser contínua, com validação rigorosa via testes automatizados, revisão por pares e auditorias de segurança.

### 1.2 Instalação/Configuração: VS Code® + GitHub Copilot®, Apresentação do Cursor®, Acesso ao ChatGPT®

Para transformar conhecimento teórico em prática, é imperativo configurar um ambiente de desenvolvimento que integre as capacidades da IA diretamente ao seu fluxo de trabalho. Abordaremos as três principais ferramentas que vêm revolucionando a produtividade do desenvolvedor.

#### 1.2.1 Visual Studio Code® e GitHub Copilot®: O Padrão da Indústria

O VS Code® mantém-se como o editor de código mais popular, e o GitHub Copilot® continua sendo a ferramenta de assistência de código mais amplamente adotada. A integração com o VS Code® é fluida.

**Passos para configuração:**

- **Instalação do VS Code®:** baixe e instale a versão mais recente em [code.visualstudio.com](https://code.visualstudio.com).
- **Instalação das extensões GitHub Copilot®:** na aba de Extensões (`Ctrl+Shift+X` / `Cmd+Shift+X`), procure por "GitHub Copilot" e "GitHub Copilot Chat" e instale ambas.
- **Autenticação:** Copilot® requer assinatura ativa (gratuito para estudantes e mantenedores open-source). Após instalar, autentique-se com sua conta GitHub®.

**Recursos avançados do GitHub Copilot®:**

- **Copilot Edits®:** via chat lateral, descreva refatorações ou adições que afetam múltiplos arquivos. O Copilot® analisa o contexto e sugere alterações em todos os arquivos relevantes (GitHub, 2025).
- **Geração de testes e docstrings:** posicione o cursor em uma função e use comandos do Copilot Chat® para gerar testes ou documentação detalhada (Microsoft, 2025a).
- **Explicação de código:** selecione um trecho complexo e peça ao Copilot Chat® uma explicação em linguagem natural (Microsoft, 2025b).

#### 1.2.2 Cursor®: o IDE AI-Native para Alta Produtividade

O Cursor® representa uma nova geração de IDEs construídos desde o início com a IA como componente central. Diferente de uma extensão, no Cursor® a IA é parte integrante do núcleo do editor.

**Principais características:**

- **Composer Mode (`Cmd+K` / `Ctrl+K`):** descreva uma funcionalidade inteira, refatoração complexa ou novo módulo em linguagem natural. O Cursor® gera arquivos, pastas, código e testes necessários de uma só vez (Cursor, 2025).
- **Tab-to-autocomplete agressivo:** sugere blocos inteiros, funções completas e até arquivos com base no contexto.
- **Contexto de repositório e multi-file editing:** o Cursor® indexa todo o projeto localmente, permitindo perguntas como "Onde está definida a lógica de autenticação?" ou alterações que afetam vários componentes simultaneamente (MorphLLM, 2026).
- **Suporte a múltiplos modelos de IA:** alterne entre GPT-5.3 Codex®, Claude 4.6® e modelos locais via Ollama® (Continue Dev, 2025).

#### 1.2.3 Claude Code®: a Inteligência Artificial no Terminal para Automação e Diagnóstico

Uma das inovações mais recentes é o Claude Code®, uma CLI que permite interagir diretamente com os modelos Claude 4.6® a partir do terminal. Útil para fluxos baseados em terminal e automação de tarefas repetitivas.

**Funcionalidades:**

- **Operações Git assistidas:** "Rebase os últimos cinco commits interativamente e combine os dois primeiros" ou "Crie um novo branch a partir de main com um commit vazio".
- **Refatoração e edição de arquivos:** lê arquivos, sugere alterações e aplica diretamente, com confirmação prévia.
- **Diagnóstico de erros:** cole um stack trace e peça explicação e correção; o Claude Code® analisa o contexto do projeto e aponta a causa raiz.
- **Geração de scripts e configurações:** para deploy, configuração de novos serviços etc.

O Claude Code® é ideal para quem busca maximizar automação e eficiência no terminal (TechCrunch, 2026).

### 1.3 Engenharia de Prompts para Geração/Edição de Código (Padrões, Contexto, Exemplos)

A eficácia no uso de assistentes de IA não reside apenas na ferramenta, mas na capacidade de comunicação clara e precisa. A engenharia de prompts evoluiu de simples frases para estruturas complexas que maximizam o potencial dos LLMs.

#### 1.3.1 O Padrão de Prompt Estruturado: Maximizando a Clareza e o Contexto

Um modelo recomendado é o **CO-STAR**, adaptado para engenharia de software:

- **C — Contexto:** ambiente do projeto, tecnologia principal, arquitetura, propósito do módulo. *Ex.:* "Estou trabalhando em um backend Python® com FastAPI®, usando Pydantic® para validação. O objetivo é criar uma API RESTful para gerenciar usuários".
- **O — Objetivo:** tarefa específica, sem ambiguidades. *Ex.:* "Preciso de uma função que valide o formato de um e-mail e retorne True ou False".
- **S — Estilo:** padrão de codificação, linguagem, convenções. *Ex.:* "Python 3.11®, PEP 8, orientado a objetos, docstrings no formato Google®".
- **T — Tonalidade:** útil para documentação ou mensagens de erro. *Ex.:* "Mensagem amigável e clara para o usuário final".
- **A — Audiência:** quem usará/lerá o código. *Ex.:* "Será revisado por desenvolvedores juniores, então deve ser autoexplicativo".
- **R — Resposta:** formato da saída. *Ex.:* "Apenas o código da função, sem explicações, com exemplo de uso".

Seguir o CO-STAR minimiza iterações e refinamentos (Microsoft, 2025a).

#### 1.3.2 Técnicas Avançadas de Prompting para Código

- **Few-shot prompting:** forneça exemplos de pares entrada/saída.
- **Chain-of-Thought (CoT):** peça à IA para "pensar em voz alta" — útil para tarefas complexas, permite identificar erros de raciocínio.
- **Context-window optimization:** forneça apenas o contexto relevante; foque a IA em arquivos/seções específicos.
- **Iterative prompting:** divida a tarefa em etapas, peça rascunhos, dê feedback, peça refinamentos.

#### 1.3.3 Exemplos Práticos de Prompts e Seus Resultados Esperados

**Exemplo 1 — Geração de função de validação**

- *Prompt fraco:* "Escreva uma função Python para validar e-mail."
- *Prompt forte (CO-STAR):* especifica contexto (FastAPI®), objetivo (`is_valid_email`), estilo (biblioteca `email_validator`, docstring Google®), resposta (apenas a função e exemplo de uso).

Resultado esperado:

```python
from email_validator import validate_email, EmailNotValidError

def is_valid_email(email: str) -> bool:
    """Valida se um endereço de e-mail é válido.

    Args:
        email: O endereço de e-mail a ser validado.

    Returns:
        True se o e-mail for válido, False caso contrário.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

if __name__ == "__main__":
    print(f"teste@exemplo.com: {is_valid_email('teste@exemplo.com')}")  # True
    print(f"email_invalido: {is_valid_email('email_invalido')}")        # False
```

**Exemplo 2 — Refatoração de código existente**

- *Prompt fraco:* "Melhore este código."
- *Prompt forte (CoT + CO-STAR):* contexto (função longa demais), objetivo (aplicar SRP), estilo (manter assinatura, delegar a funções auxiliares), passo a passo: identificar responsabilidades, criar funções menores, orquestrar, garantir legibilidade e testabilidade.

Código original analisado pela IA:

```python
def process_user_data(user_id, raw_data):
    # 1. Valida os dados brutos
    if not isinstance(raw_data, dict) or 'name' not in raw_data:
        raise ValueError("Dados inválidos")
    # 2. Normaliza o nome
    name = raw_data['name'].strip().title()
    # 3. Salva no banco de dados
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user_id, name))
    db_connection.commit()
    # 4. Envia notificação por e-mail
    send_email(user_id, f"Bem-vindo, {name}!")
    return {"status": "success", "user_id": user_id, "name": name}
```

Resultado esperado: a IA identifica as quatro responsabilidades (validação, normalização, persistência, notificação) e cria funções separadas, orquestradas pela `process_user_data` original.

Ao dominar a engenharia de prompts, você transforma a IA em um copiloto poderoso, capaz de entender intenções complexas e gerar código de alta qualidade (GitHub, 2025).

#### Saiba mais...

- **OpenAI Prompting Guide:** [platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- **Anthropic Prompt Engineering:** [docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- **Qwen3.5-Coder:** [qwen.ai/blog?id=qwen3.5](https://qwen.ai/blog?id=qwen3.5)
- **Devstral:** [mistral.ai/news/devstral](https://mistral.ai/news/devstral)
- **Prompt Patterns for LLMs:** [arxiv.org/abs/2302.11382](https://arxiv.org/abs/2302.11382)

#### Para relembrar...

- IA voltada para desenvolvimento acelera tarefas, mas não substitui revisão humana.
- Prompts melhores trazem contexto, objetivo, restrições e formato de saída.
- Copilot®, Cursor® e Claude Code® servem a fluxos diferentes.
- LLMs locais e *open weights* ampliam privacidade, custo controlado e experimentação.
- Segurança, alucinações e código desatualizado exigem validação contínua.

---

## Unidade II — Ideação, Arquitetura Mínima e Git/GitHub® para o Projeto

Nesta Unidade, faremos a transição do entendimento das ferramentas para o planejamento e estruturação do miniprojeto. O sucesso reside em uma fundação sólida: ideia bem delineada, arquitetura clara e escalável, e controle de versão robusto. A IA pode ser uma aliada poderosa em cada etapa.

### 2.1 Seleção do Miniprojeto

A escolha do miniprojeto é o primeiro passo prático. O objetivo é construir um MVP que permita explorar a genAI em diferentes estágios do ciclo de vida do desenvolvimento, sem se perder em complexidade desnecessária.

#### 2.1.1 Critérios para a Seleção de um MVP Assistido por IA

- **Escopo limitado e claro:** funcionalidades bem definidas e gerenciáveis. Conclusão em ~30 horas de trabalho prático.
- **Potencial de uso da IA:** múltiplas etapas (geração de código, testes, documentação, refatoração).
- **Familiaridade tecnológica:** linguagem/framework com conhecimento básico prévio.
- **Relevância pessoal:** projeto motivador e engajador.
- **Testabilidade:** facilmente testável, permitindo validar saídas da IA.

#### 2.1.2 Exemplos Detalhados de Projetos Recomendados

**Tabela 2 — Sugestões de projetos e aplicações da IA generativa**

| Projeto Sugerido | Descrição | Tecnologias Sugeridas | Aplicação da IA Generativa |
|---|---|---|---|
| **Micro-API de Gerenciamento de Tarefas (To-Do List)** | API RESTful que permite criar, ler, atualizar e excluir tarefas. Persistência em SQLite ou PostgreSQL®. | Python (FastAPI, SQLAlchemy) ou Node.js® (Express, Prisma/Sequelize) | Geração de modelos (esquemas de BD e Pydantic/TypeScript), endpoints CRUD, testes unitários, docstrings e README. |
| **Chatbot de Q&A (RAG)** | Assistente conversacional que responde com base em um documento específico (ex.: PDF) usando Retrieval Augmented Generation. | Python® (LangChain, OpenAI/Claude API, Streamlit/Gradio) | Processamento de PDFs, geração de embeddings, orquestração da cadeia RAG, geração de respostas contextuais. |
| **Dashboard de monitoramento de clima** | Aplicação web que consome API externa de clima e exibe temperatura, umidade e previsão por cidade. | React/Vue.js, Tailwind CSS, Fetch API/Axios | Geração de componentes UI, integração com API externa, testes de componentes, sugestões de classes Tailwind. |
| **Gerador de senhas seguras** | CLI ou web simples que gera senhas aleatórias com base em critérios do usuário. | Python® (Click/Argparse) ou JavaScript (Node.js®, HTML/CSS/JS) | Lógica de geração, testes de aleatoriedade e conformidade, construção de CLI/UI. |

A escolha deve ser estratégica. O objetivo é aprender a *copilotar* o desenvolvimento (Garcia, 2025), não apenas construir um projeto.

### 2.2 Arquitetura Mínima (Módulos, Dependências, Fluxo de Dados)

Um planejamento arquitetural mínimo é essencial. Modelos como o Claude 4.6 Opus® podem atuar como arquitetos de software virtuais.

#### 2.2.1 Concebendo a Arquitetura com o Auxílio da IA

**Ferramentas de diagramação assistida por IA:** linguagens de descrição baseadas em texto como Mermaid.js ou PlantUML permitem criar diagramas complexos a partir de texto simples — facilmente compreendidos e gerados por LLMs.

**Exemplo de prompt para Diagrama Mermaid:**

> *Contexto:* Micro-API de gerenciamento de tarefas em Python® com FastAPI®. Frontend (React) → backend → PostgreSQL®.
> *Objetivo:* Crie um diagrama de componentes em Mermaid.js mostrando interação entre frontend, backend (controller, service, repository) e banco.
> *Estilo:* C4-PlantUML se possível, com setas de comunicação.
> *Resposta:* Apenas o código Mermaid.

Além de diagramas, a IA pode sugerir estrutura de módulos e hierarquia de pastas que promovam manutenibilidade e escalabilidade.

#### 2.2.2 Definição de Dependências e Tecnologias

Descreva a funcionalidade desejada e peça sugestões de bibliotecas:

> *Contexto:* API RESTful em Python® para gerenciar usuários, com ORM para PostgreSQL® e validação de dados.
> *Objetivo:* Listar bibliotecas Python® recomendadas e gerar `requirements.txt` com versões mais recentes.
> *Estilo:* Apenas as bibliotecas essenciais.

Resultado esperado:

```
fastapi==0.110.0
uvicorn==0.27.1
sqlalchemy==2.0.27
psycopg2-binary==2.9.9
pydantic==2.6.1
```

### 2.3 Git/GitHub® Essencial: Repositório, .gitignore, Commits, Push, Releases/Tags; Requisitos da Submissão

#### 2.3.1 Configuração Inicial do Repositório e Boas Práticas

```bash
# Inicialização do repositório local
git init

# Adicionar arquivos (com .gitignore configurado antes)
git add .

# Primeiro commit
git commit -m "feat: estrutura inicial do projeto e setup básico"

# Conexão com remoto no GitHub
git remote add origin <URL_DO_SEU_REPOSITORIO_GITHUB>
git branch -M main
git push -u origin main
```

#### 2.3.2 O Papel Crucial do .gitignore Inteligente

Ao trabalhar com IA, é comum gerar arquivos temporários, ambientes virtuais (`.venv`), pastas de cache (`__pycache__`, `.next`, `node_modules`) e arquivos de IDE (`.vscode`, `.idea`). Incluí-los no controle de versão pode causar conflitos, aumentar tamanho do repositório e expor informações sensíveis.

Exemplo de `.gitignore` gerado por IA:

```gitignore
# Python
__pycache__/
*.pyc
*.pyd
*.pyo
.Python
build/
dist/
*.egg-info/
.venv/
venv/

# Node.js
node_modules/
npm-debug.log
yarn-debug.log
yarn-error.log
.pnp/
.pnp.js

# VS Code
.vscode/
.history/

# Environment variables
.env
.env.*

# OS generated files
.DS_Store
Thumbs.db
```

#### 2.3.3 Conventional Commits com Auxílio da IA

Estrutura:

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

- **Tipo:** `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.
- **Escopo opcional:** parte do sistema afetada (`feat(auth):`, `fix(api):`).
- **Descrição:** frase imperativa breve.
- **Corpo opcional:** descrição detalhada.
- **Rodapé opcional:** referências a issues, PRs ou *breaking changes*.

A IA (Claude Code® ou Copilot Chat®) pode sugerir mensagens com base nas mudanças *staged*. Exemplo de resultado:

```
feat(user): Adiciona funcionalidade de criação de usuário
fix(validation): Corrige bug na validação de e-mail em user_service.
```

Essa prática melhora a qualidade do histórico e ajuda a pensar de forma estruturada sobre as mudanças (Blischack et al., 2016).

#### 2.3.4 Requisitos para Submissão Final do Projeto no GitHub®

**Checklist de submissão:**

- **Repositório público:** acessível para revisão; sem chaves de API ou senhas expostas (use `.env` ignorado).
- **Histórico de commits consistente:** mínimo de 5 a 10 commits significativos no padrão Conventional Commits.
- **`README.md` detalhado:** título e descrição; instruções de setup; exemplos de uso; tecnologias (incluindo modelos de IA); seção *Limitações e Próximos Passos*; créditos e licença.
- **Gerenciamento de dependências:** arquivo de dependências (`requirements.txt`, `package.json`).
- **Testes automatizados:** testes unitários/integração executáveis e passando.
- **Releases ou tags:** crie uma Release/Tag (ex.: `v1.0.0`) para marcar a versão de entrega.

A IA pode auxiliar em cada um desses pontos (GitHub, 2025).

#### Saiba mais...

- **Diátaxis:** [diataxis.fr](https://diataxis.fr/)
- **Conventional Commits:** [conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)
- **GitHub Docs — Repositories and Projects:** [docs.github.com/en/repositories](https://docs.github.com/en/repositories)
- **OpenHands:** [github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)
- **OpenClaw:** [docs.openclaw.ai](https://docs.openclaw.ai/)

#### Para relembrar...

- Comece com um MVP pequeno, claro e viável.
- Desenhe arquitetura mínima com módulos, dependências e fluxo de dados.
- Use Git desde o início e mantenha um `.gitignore` coerente com a stack.
- Mensagens de commit devem descrever bem a evolução do projeto.
- Prepare o repositório para submissão com README, testes e versão final marcada.

---

## Unidade III — Implementação Guiada (Parte 1): Núcleo da Aplicação

Com planejamento e ambiente prontos, entramos na implementação ativa. Esta Unidade foca no *core* da aplicação: lógica de negócio principal e integrações com APIs externas, incluindo LLMs.

### 3.1 Implementação do Core

#### 3.1.1 Configuração de Entrada e Saída (I/O) com IA

Para APIs RESTful, é comum definir esquemas de dados para requisições e respostas. A genAI é eficiente nessa criação a partir de descrições em linguagem natural.

**Exemplo com FastAPI® e Pydantic®:**

> *Contexto:* API RESTful para gerenciar tarefas; modelo Pydantic® para `Task`.
> *Objetivo:* `Task` com `id` (UUID, opcional na criação), `title` (string, obrigatório, 3–100 chars), `description` (opcional), `status` (bool, padrão `False`), `created_at` (datetime, padrão `datetime.utcnow`).
> *Estilo:* Tipagem estática, docstrings por campo.

Resultado esperado:

```python
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    """Modelo base para uma tarefa, usado para criação e atualização."""
    title: str = Field(..., min_length=3, max_length=100, description="Título da tarefa")
    description: Optional[str] = Field(None, description="Descrição detalhada da tarefa")
    status: bool = Field(False, description="Status de conclusão da tarefa")

class TaskCreate(TaskBase):
    """Modelo para criação de uma nova tarefa."""
    pass

class Task(TaskBase):
    """Modelo completo de uma tarefa, incluindo campos gerados pelo sistema."""
    id: UUID = Field(default_factory=uuid4, description="Identificador único da tarefa")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Data e hora de criação")

    class Config:
        from_attributes = True  # ou orm_mode = True para Pydantic v1
```

De forma similar, a IA pode gerar interfaces TypeScript para frontend, garantindo consistência com o backend.

#### 3.1.2 Integração com APIs de IA: Conectando seu Projeto ao Poder dos LLMs

Se o miniprojeto envolve LLMs (ex.: Chatbot RAG), a integração com APIs OpenAI® ou Anthropic® será central. A IA pode escrever o boilerplate, liberando você para focar na lógica de negócio e prompts.

**Exemplo — integração com OpenAI:**

```python
import os
from typing import List, Optional
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam

async def get_openai_response(messages: List[ChatCompletionMessageParam]) -> Optional[str]:
    """Envia mensagens para o modelo OpenAI e retorna a resposta.

    Args:
        messages: Lista de mensagens no formato da API OpenAI.

    Returns:
        A resposta do modelo como string, ou None em caso de erro.
    """
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    try:
        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erro ao chamar a API OpenAI: {e}")
        return None

if __name__ == "__main__":
    import asyncio

    async def main():
        messages_example: List[ChatCompletionMessageParam] = [
            {"role": "system", "content": "Você é um assistente prestativo."},
            {"role": "user", "content": "Qual a capital da França?"},
        ]
        response_content = await get_openai_response(messages_example)
        if response_content:
            print(f"Resposta da IA: {response_content}")

    asyncio.run(main())
```

Para a API da Anthropic®, a IA também pode gerar código para Claude 4.6®, incluindo `system_prompt` e `tool_use` para agentes (Garcia, 2025).

### 3.2 Uso de Copilot/Cursor® para Gerar Trechos, Esqueleto de Classes/Funções e Docstrings

#### 3.2.1 Composer Mode do Cursor®: A Revolução da Edição Multiarquivo

Ativado por `Cmd+K` / `Ctrl+K`, permite descrever uma tarefa complexa em linguagem natural; a IA tenta implementá-la afetando múltiplos arquivos. Ideal para:

- **Criação de features completas:** *"Adicione upload de avatares: endpoint `/upload-avatar`, serviço para processar e salvar no S3, atualização do modelo `User` com URL do avatar."*
- **Refatorações abrangentes:** *"Mude todos os UUIDs para inteiros auto-incrementais nos modelos de BD e atualize todas as referências na API."*
- **Geração de esqueletos de projeto:** estrutura básica de pastas, arquivos e classes para novos módulos/microsserviços.

O Cursor® apresenta as mudanças em formato de *diff* interativo (Cursor, 2025).

#### 3.2.2 Geração Inteligente de Docstrings e Comentários

- **Docstrings automáticas:** ao iniciar `"""` em Python ou `/**` em JS/TS, Copilot®/Cursor® analisa assinatura, parâmetros, retorno e lógica para sugerir docstring completa. Especifique formato (Google®, NumPy®, JSDoc®).
- **Comentários explicativos:** selecione código complexo e use "Explain Code" no Copilot Chat® ou Cursor®.

A automação garante documentação consistente (Microsoft, 2025a).

### 3.3 Boas Práticas ao Revisar/Refinar Código Sugerido (Evitar Copiar sem Entender)

Um dos maiores riscos é o "Copy-Paste Orientado a IA": copiar sem compreender introduz bugs sutis, vulnerabilidades, dívida técnica e prejudica suas habilidades.

#### 3.3.1 O Ciclo de Revisão Crítica

- **Leitura atenta e compreensão:** se houver partes que você não entende, peça explicação ou consulte a documentação. Você deveria ser capaz de reescrever esse código por conta própria.
- **Validação da lógica e requisitos:** a sugestão resolve o problema? Atende a todos os requisitos? Teste mentalmente com diferentes entradas.
- **Verificação de segurança:** verifique injeção SQL, XSS, exposição de credenciais, tratamento inadequado de entradas, bibliotecas desatualizadas (consulte OWASP, 2025).
- **Adesão a padrões e boas práticas:** Clean Code, SOLID, convenções (PEP 8 etc.).
- **Teste imediato e debugging:** execute, escreva testes, integre. Use as ferramentas de depuração do IDE.

#### 3.3.2 Debugging Assistido por IA: Transformando Erros em Aprendizado

- **Forneça o contexto completo do erro:** mensagem completa, stack trace, trecho relevante e cenário.
- **Peça explicações, não apenas soluções:** *"Recebi um `AttributeError: 'NoneType' object has no attribute 'name'` na linha 42 do `user_service.py`. Explique a causa raiz provável antes de sugerir uma correção."*
- **Use a IA para entender conceitos:** *"O que é um `TypeError` em Python® e como difere de um `ValueError`?"*

Ao adotar essa postura crítica, você aprimora suas próprias habilidades, transformando a IA em ferramenta de aprendizado contínuo (Microsoft, 2025b).

#### Saiba mais...

- **FastAPI®:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)
- **Pydantic®:** [docs.pydantic.dev](https://docs.pydantic.dev/)
- **OpenAI API Quickstart:** [platform.openai.com/docs/quickstart](https://platform.openai.com/docs/quickstart)
- **Anthropic Docs:** [docs.anthropic.com](https://docs.anthropic.com/)
- **Ollama®:** [docs.ollama.com](https://docs.ollama.com/)

#### Para relembrar...

- O *core* deve deixar explícito como os dados entram, são processados e saem.
- Integrações com APIs de IA precisam tratar autenticação, formato de mensagens, erros e limites de uso.
- Copilot® e Cursor® aceleram esqueletos, funções e docstrings — qualidade final é responsabilidade do desenvolvedor.
- Revisar código sugerido é etapa obrigatória para entender lógica, conferir segurança e testar comportamento.
- Debugging assistido funciona melhor com contexto real e pedindo explicação, não só correção.

---

## Unidade IV — Implementação Guiada (Parte 2): Testes, Refatoração e Documentação

Nesta Unidade aprofundamos o compromisso com qualidade e sustentabilidade. Software de excelência precisa ser robusto, testável, legível e bem documentado. A genAI atua como catalisador para elevar o padrão de entrega.

### 4.1 Testes Básicos Criados/Auxiliados pela IA; Execução e Correções

A escrita de testes é uma das áreas em que a genAI (Claude 4.6 Sonnet®, GPT-5.3 Codex®) demonstra valor inestimável. Testes automatizados são a primeira linha de defesa contra regressões.

#### 4.1.1 Geração de Testes Unitários com IA: uma Abordagem Prática

Testes unitários validam a menor unidade testável (função/método) de forma isolada, ajudando a detectar regressões, facilitar refatorações e aumentar confiança ao evoluir o código. A IA acelera a criação cobrindo casos comuns, de borda e de erro. O papel do desenvolvedor continua essencial: revisar, ajustar nomes, melhorar clareza e complementar cenários do domínio.

**Exemplo com Pytest:** considere uma função que calcula desconto percentual.

> *Contexto:* função Python® `apply_discount`.
> *Objetivo:* gerar suíte com pytest cobrindo: cálculo correto, valores zero, valor negativo (deve levantar `ValueError`), desconto fora do intervalo 0–1 (deve levantar `ValueError`).
> *Estilo:* asserções claras, nomes descritivos.

```python
def apply_discount(price: float, discount_rate: float) -> float:
    if price < 0:
        raise ValueError("Price must be non-negative.")
    if not (0 <= discount_rate <= 1):
        raise ValueError("Discount rate must be between 0 and 1.")
    return price * (1 - discount_rate)
```

Resultado esperado:

```python
import pytest
# from discount_calculator import apply_discount

def test_apply_discount_with_valid_values():
    assert apply_discount(100, 0.10) == 90.0
    assert apply_discount(200, 0.25) == 150.0
    assert apply_discount(50, 0.50) == 25.0

def test_apply_discount_with_zero_values():
    assert apply_discount(0, 0.10) == 0.0
    assert apply_discount(100, 0) == 100.0
    assert apply_discount(0, 0) == 0.0

def test_apply_discount_with_full_discount():
    assert apply_discount(80, 1.0) == 0.0

def test_apply_discount_negative_price_raises_error():
    with pytest.raises(ValueError, match="Price must be non-negative"):
        apply_discount(-100, 0.10)

def test_apply_discount_invalid_discount_rate_raises_error():
    with pytest.raises(ValueError, match="Discount rate must be between 0 and 1"):
        apply_discount(100, 1.10)
    with pytest.raises(ValueError, match="Discount rate must be between 0 and 1"):
        apply_discount(100, -0.05)
```

A qualidade do resultado está diretamente ligada à qualidade do prompt: descreva entradas válidas, inválidas, exceções esperadas e estilo. Essa abordagem libera tempo para focar em testes de integração e cenários complexos.

#### 4.1.2 TDD Assistido por IA

O TDD preconiza escrever testes antes do código. A IA pode atuar em cada fase:

- **Red (teste que falha):** descreva a funcionalidade e peça um teste que falhe (a função ainda não existe). *Ex.: "Escreva um teste pytest para `add_item_to_cart`: ao adicionar item, o carrinho contém esse item com a quantidade correta."*
- **Green (código mínimo para passar):** peça à IA o código que faz o teste passar — apenas o necessário.
- **Refactor:** peça refatoração mantendo os testes passando — legibilidade, PEP 8, estrutura mais eficiente (Banh et al., 2025).

Esse ciclo iterativo acelera o desenvolvimento e garante alta cobertura desde o início (Peng et al., 2023).

### 4.2 Refatoração Assistida: Clareza, DRY, Nomes, Modularização

Refatorar é reestruturar o código sem alterar o comportamento externo, melhorando legibilidade, manutenibilidade, escalabilidade e performance. A genAI atua como *code reviewer* incansável e assistente de refatoração.

#### 4.2.1 Aplicação de Princípios de Clean Code com IA

- **DRY:** a IA pode identificar duplicações e sugerir extração para utilitários reutilizáveis. *Ex.: "Analise `service_a.py` e `service_b.py`. Identifique lógica duplicada e sugira função utilitária em `utils.py`, refatorando os serviços."*
- **SOLID Principles:** modelos como Claude 4.6 Opus® aplicam SRP, OCP, LSP, ISP, DIP. *Ex.: "Refatore `PaymentProcessor` para aderir ao SRP: separe validação, transação e notificação."*
- **Nomenclatura semântica:** *Ex.: "Revise `data_manipulation.py`. Sugira nomes mais descritivos seguindo PEP 8 — `proc_data` → `process_raw_data`."*
- **Modularização e desacoplamento:** *Ex.: "Analise `main_logic.js`. Sugira como modularizar separando UI, lógica de negócio e acesso a dados."*

#### 4.2.2 Refatoração com Claude 4.6 Opus®: o Arquiteto de Software Virtual

Para refatorações arquiteturais que afetam múltiplos arquivos, o Opus® se destaca pela janela de contexto massiva e *extended thinking*.

- **Refatoração multiarquivo:** *Ex.: "Projeto Python® com FastAPI® onde a lógica de acesso a dados está nos serviços. Quero introduzir Repository Pattern. Crie interface `IRepository` e implementações concretas `UserRepository` e `TaskRepository`. Refatore `UserService` e `TaskService` para usar essas classes via injeção de dependência. Use tipagem estática e siga SOLID."*
- **Análise de impacto e sugestões preventivas:** o Opus® prevê como uma refatoração impacta outros componentes, sugerindo alterações em testes, documentação ou configurações para evitar quebras (Anthropic, 2026b).

### 4.3 Documentação: Completar README (Instalação, Uso, Exemplos)

#### 4.3.1 Estrutura de um README Profissional Assistido por IA

Seções essenciais e como a IA ajuda:

- **Título e descrição:** *"Escreva título e descrição concisa para uma API de gerenciamento de tarefas em Python® com FastAPI®."*
- **Tabela de conteúdos** (recomendada para READMEs longos): pode ser gerada automaticamente a partir dos títulos.
- **Tecnologias utilizadas:** liste linguagens, frameworks, bibliotecas e ferramentas (incluindo modelos de IA).
- **Pré-requisitos:** o que o usuário precisa ter instalado.
- **Instalação:** passo a passo para clonar, instalar dependências e configurar o ambiente.
- **Uso e exemplos:** para APIs, exemplos `curl` ou HTTPie; para CLI, exemplos de comandos.
- **Estrutura do projeto:** breve descrição da organização.
- **Testes:** como rodar os testes automatizados.
- **Contribuição** (opcional): para projetos open source.
- **Licença.**
- **Limitações e próximos passos:** seção honesta sobre o que o projeto não faz e como pode evoluir — demonstra visão crítica.

#### 4.3.2 Documentação de Código (Docstrings e Comentários) com IA

- **Geração de docstrings:** Copilot Chat® e Cursor® geram docstrings completas no formato escolhido (Google®, NumPy®, Sphinx®). *"Gere uma docstring no formato Google® para esta função Python®."*
- **Explicação de código e comentários:** *"Explique este algoritmo de ordenação e adicione comentários inline para cada passo principal."*

#### Saiba mais...

- **Pytest:** [docs.pytest.org](https://docs.pytest.org/)
- **Refactoring Guru:** [refactoring.guru](https://refactoring.guru/)
- **The Twelve-Factor App®:** [12factor.net](https://12factor.net/)

#### Para relembrar...

- Testes básicos validam comportamento esperado e reduzem regressões.
- TDD assistido por IA acelera o ciclo *red-green-refactor*, com revisão crítica.
- Refatorar é melhorar estrutura sem mudar comportamento externo: clareza, modularidade, menor repetição.
- Nomes semânticos, funções coesas e separação de responsabilidades tornam o projeto sustentável.
- README, docstrings e exemplos de uso são parte do produto.

---

## Unidade V — Empacotamento, README Final, Demonstração e Submissão

Chegamos à fase culminante: empacotamento, finalização da documentação, preparação para a demonstração e submissão oficial. É aqui que você transforma código funcional em produto apresentável e replicável.

### 5.1 Empacotar/Organizar Repositório

#### 5.1.1 Gestão de Dependências e Ambientes Virtuais

**Exemplo com Python® (`requirements.txt` e `pyproject.toml`):**

> *Contexto:* projeto Python® com FastAPI®, Pydantic®, SQLAlchemy e Psycopg2 para PostgreSQL®, gerenciado com pipenv.
> *Objetivo:* gerar `requirements.txt` com versões exatas e sugerir `pyproject.toml` básico para migração ao Poetry®.

Resultado esperado (`requirements.txt`):

```
fastapi==0.110.0
uvicorn==0.27.1
sqlalchemy==2.0.27
psycopg2-binary==2.9.9
pydantic==2.6.1
```

Resultado esperado (`pyproject.toml` para Poetry®):

```toml
[tool.poetry]
name = "meu-miniprojeto"
version = "0.1.0"
description = "Um miniprojeto de IA Generativa."
authors = ["Seu Nome <seu.email@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.110.0"
uvicorn = {extras = ["standard"], version = "^0.27.1"}
sqlalchemy = "^2.0.27"
psycopg2-binary = "^2.9.9"
pydantic = "^2.6.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

**Exemplo com Node.js® (`package.json`):** a IA pode verificar completude e adicionar scripts úteis (`start`, `test`).

#### 5.1.2 Scripts de Automação e Makefile

Centralize comandos comuns:

```makefile
.PHONY: install run test format

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest

format:
	black .
```

### 5.2 README Final (Objetivo, Instalação, Execução, Exemplos, Limitações, Próximos Passos)

O README é a narrativa do seu projeto e deve destacar o papel da genAI no processo de desenvolvimento.

#### 5.2.1 Storytelling do Projeto: O Papel da IA no Desenvolvimento

Pontos a destacar:

- **Desafios superados com IA:** problema complexo + ferramenta usada (ex.: Claude 4.6 Opus® para refatoração arquitetural, GPT-5.3 Codex® para depuração).
- **Ganhos de produtividade:** quantifique tempo economizado em boilerplate, testes ou docs.
- **Decisões arquiteturais:** como a IA influenciou escolhas (Composer Mode do Cursor® para prototipagem; Claude Code® para validação).
- **Lições aprendidas:** limitações da IA, desafios de prompts, importância da revisão humana.

*Exemplo de prompt:* "Escreva uma seção 'Como a IA Acelerou Este Projeto' destacando ganhos de produtividade e ferramentas usadas (Copilot®, Cursor®, Claude 4.6 Sonnet®). Mencione a importância da revisão humana."

#### 5.2.2 Demonstração Visual e Exemplos de Uso

- **Capturas de tela / GIFs:** se houver UI, mostre o projeto em funcionamento. Ferramentas: Peek (Linux®) ou LICEcap® (multiplataforma).
- **Exemplos de requisições API:** *"Gere exemplos `curl` para `/tasks` (GET, POST) e `/tasks/{id}` (GET, PUT, DELETE) da API FastAPI®."*

### 5.3 Demonstração do Projeto e Submissão Oficial

#### 5.3.1 Checklist de Submissão Final

- **Repositório público e acessível** com todos os arquivos necessários.
- **README completo e profissional** com formatação Markdown correta.
- **Histórico de commits consistente** seguindo Conventional Commits (≥ 5 commits significativos).
- **Gerenciamento de dependências** (`requirements.txt`, `package.json`, `pyproject.toml`) com versões.
- **Testes automatizados** presentes e passando, com instruções de execução.
- **Variáveis de ambiente e credenciais** removidas do código e do histórico Git®, carregadas de `.env` (no `.gitignore`).
- **Branch principal limpo:** sem WIP ou arquivos temporários.
- **Release ou Tag** (`v1.0.0`) marcando a versão final.
- **Licença** especificando os termos de uso.

Seguindo este checklist, você demonstra profissionalismo e atenção aos detalhes — qualidades essenciais (GitHub, 2025).

#### Saiba mais...

- **Keep a Changelog:** [keepachangelog.com/en/1.1.0/](https://keepachangelog.com/en/1.1.0/)
- **Choose an Open Source License:** [choosealicense.com](https://choosealicense.com/)
- **GitHub Docs — READMEs:** [docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- **OpenClaw® Docs:** [docs.openclaw.ai](https://docs.openclaw.ai/)

#### Para relembrar...

- Empacotar bem significa organizar estrutura, dependências, scripts e instruções de execução.
- README final deve explicar objetivo, instalação, uso, exemplos, limitações e próximos passos.
- Boa demonstração evidencia problema, solução, funcionamento e participação da IA.
- Antes de submeter, revise acesso público, variáveis de ambiente, testes e documentação.
- A entrega comunica que o projeto funciona e está apresentável, reproduzível e profissional.

---

## Unidade VI — Encerramento

Parabéns! Você concluiu o laboratório introdutório, navegando pelo ciclo completo de desenvolvimento de um miniprojeto assistido por genAI. Esta jornada o equipou com habilidades práticas e o preparou para uma nova era na engenharia de software.

### 6.1 Revisão dos Conceitos Principais e Habilidades Adquiridas

Você:

- **Compreendeu a evolução dos LLMs** — do GPT-3® aos modelos de fronteira (Codex e Claude Sonnet/Opus); aprendeu a escolher o modelo certo para cada tarefa.
- **Dominou a configuração de ambientes modernos** — VS Code® + GitHub Copilot®, Cursor® IDE (com Composer Mode), Claude Code® para terminal.
- **Aprimorou a engenharia de prompts** — padrão CO-STAR, *few-shot* e *chain-of-thought*.
- **Praticou desenvolvimento orientado à qualidade** — Clean Code, refatoração assistida e testes unitários com Claude 4.6 Sonnet®. Reforçou-se a importância da revisão crítica.
- **Reforçou boas práticas de Git e documentação** — Conventional Commits e README abrangente que conta a história do desenvolvimento assistido por IA.

### 6.2 O Futuro do Desenvolvedor "AI-Augmented®": Tendências e Perspectivas

O desenvolvedor do futuro não será substituído pela IA, mas *aumentado* por ela.

**Principais tendências:**

- **Agentes autônomos de software:** modelos como Claude 4.6 Opus® e GPT-5.3 Codex® já planejam, executam e monitoram tarefas complexas. O desenvolvedor passará a atuar como "gerente de agentes" (Anchan, 2025).
- **NLDD (Natural Language Driven Development):** descrever requisitos em linguagem natural com IA gerando código correspondente se tornará cada vez mais sofisticado.
- **Segurança e ética da IA como habilidades essenciais:** compreensão de injeção de prompt, vazamento de dados, viés e responsabilidade (OWASP, 2025; NIST, 2024).
- **Engenharia de prompts como disciplina central:** padrões formais, metodologias e ferramentas dedicadas.
- **Aumento da complexidade e escala dos projetos:** com a IA automatizando o repetitivo, mais foco em problemas complexos (computação quântica, bioinformática, exploração espacial).

O futuro pertence a quem sabe orquestrar e colaborar de forma eficaz com as ferramentas de IA. Continue explorando: novos modelos surgem todos os dias, e LLMs locais cada vez mais acessíveis democratizam o acesso a IA de qualidade.

---

## Referências

- **ANCHAN, P.** *MCP vs. RAG vs. agentes de IA: quem liderará a IA em 2025?* 2025. Disponível em: [clickup.com/pt-BR/blog/456970/rag-vs-mcp-vs-agentes-de-ia](https://clickup.com/pt-BR/blog/456970/rag-vs-mcp-vs-agentes-de-ia). Acesso em: 12 ago. 2025.
- **ANTHROPIC.** *Introducing Claude Sonnet 4.6.* 2026a. Disponível em: [anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6). Acesso em: 08 mar. 2026.
- **ANTHROPIC.** *Introducing Claude Opus 4.6.* 2026b. Disponível em: [anthropic.com/news/claude-opus-4-6](https://www.anthropic.com/news/claude-opus-4-6). Acesso em: 08 mar. 2026.
- **BANH, L. et al.** *Copiloting the future: how generative AI transforms software engineering.* Information and Software Technology, v.183, 2025. DOI: [10.1016/j.infsof.2025.107751](https://doi.org/10.1016/j.infsof.2025.107751).
- **BLISCHAK, J. D. et al.** *A quick introduction to version control with Git and GitHub.* PLoS Computational Biology, v.12, n.1, 2016. DOI: [10.1371/journal.pcbi.1004668](https://doi.org/10.1371/journal.pcbi.1004668).
- **CONTINUE DEV.** *Install — Continue (VS Code/JetBrains).* Docs, 2025. Disponível em: [docs.continue.dev/getting-started/install](https://docs.continue.dev/getting-started/install).
- **CURSOR.** *Overview (Chat & Agent).* Cursor Docs, 2025. Disponível em: [docs.cursor.com/chat/overview](https://docs.cursor.com/chat/overview).
- **GARCIA, V. C.** *Desenvolvimento de software assistido por IA: princípios, práticas e o futuro da engenharia de software.* Dev.to, 2025. Disponível em: [dev.to/vinicius3w/desenvolvimento-de-software-assistido-por-ia-principios-praticas-e-o-futuro-da-engenharia-de-hg7](https://dev.to/vinicius3w/desenvolvimento-de-software-assistido-por-ia-principios-praticas-e-o-futuro-da-engenharia-de-hg7).
- **GITHUB.** *Copilot Chat Cookbook.* GitHub Docs, 2025. Disponível em: [docs.github.com/copilot/copilot-chat-cookbook](https://docs.github.com/copilot/copilot-chat-cookbook).
- **MICROSOFT.** *Use chat in VS Code (Copilot).* VS Code Docs, 2025a. Disponível em: [code.visualstudio.com/docs/copilot/chat/copilot-chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat).
- **MICROSOFT.** *Getting started with chat in VS Code.* VS Code Docs, 2025b. Disponível em: [code.visualstudio.com/docs/copilot/chat/getting-started-chat](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat).
- **MORPHLLM.** *Cursor vs GitHub Copilot 2026: Agents, Pricing & Real ...* 2026. Disponível em: [morphllm.com/comparisons/cursor-vs-copilot](https://www.morphllm.com/comparisons/cursor-vs-copilot).
- **NIST.** *Artificial Intelligence Risk Management Framework: Generative AI Profile (NIST AI 600-1).* 2024. DOI: [10.6028/NIST.AI.600-1](https://doi.org/10.6028/NIST.AI.600-1).
- **OPENAI.** *Introducing GPT-5.3-Codex.* 2026. Disponível em: [openai.com/index/introducing-gpt-5-3-codex/](https://openai.com/index/introducing-gpt-5-3-codex/).
- **OWASP FOUNDATION.** *OWASP Top 10 for LLM Applications.* 2025. Disponível em: [owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf).
- **PENG, S. et al.** *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot.* arXiv, 2023. Disponível em: [arxiv.org/abs/2302.06590](https://arxiv.org/abs/2302.06590).
- **TECHCRUNCH.** *Anthropic releases Opus 4.6 with new 'agent teams'.* 2026. Disponível em: [techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/).
