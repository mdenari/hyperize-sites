# ⚙️ Configuração do Projeto

**IMPORTANTE:** Este arquivo é lido pelos agents CLI. Seja específico e claro!

---

## 📌 Informações Básicas

### **Nome do Projeto**
[PREENCHA AQUI - Ex: Sistema de Gestão Pessoal, App de Receitas, Precificação Hyperize]

### **Tipo de Projeto**
- [ ] Pessoal (uso próprio)
- [ ] Empresarial (cliente/consultoria)
- [ ] Produto (SaaS/venda)
- [ ] Estudo/Aprendizado
- [ ] Outro: ___________

### **Categoria**
- [ ] Software (aplicação web/mobile)
- [ ] Game (jogo)
- [ ] Strategy (consultoria, planos estratégicos)
- [ ] Content (editorial, documentação)
- [ ] Research (pesquisa pura)

### **Nível de Complexidade** (ELabs-Agile Levels)
- [ ] Level 0: Bug fix ou mudança isolada (< 1 dia)
- [ ] Level 1: Feature pequena com tech-spec (1-2 dias)
- [ ] Level 2: Feature média com PRD (2-5 dias)
- [ ] Level 3-4: Projeto completo com arquitetura (1-4 semanas)

---

## 🎯 O Que Este Projeto Faz?

### **Descrição Resumida** (2-3 frases)
[Descreva o que este projeto faz ou resolve]

Exemplo:
> "Sistema para gerenciar meus projetos pessoais, profissionais e rotinas diárias.
> Integra com ClickUp, Google Calendar e WhatsApp.
> Ajuda a manter foco e produtividade através de agents IA."

### **Problema que Resolve**
[Qual dor ou necessidade este projeto atende?]

Exemplo:
> "Atualmente perco tempo alternando entre múltiplas ferramentas (ClickUp, Google Calendar,
> WhatsApp) e não tenho visão unificada dos meus compromissos e projetos."

### **Público-Alvo**
[Para quem é este projeto?]

Exemplo:
> "Primariamente para mim (Mauricio), mas pode ser adaptado para outros profissionais
> autônomos que gerenciam múltiplos projetos simultaneamente."

---

## 🎪 Objetivos Principais

**Defina 3-5 objetivos SMART (específicos, mensuráveis, alcançáveis):**

1. **Objetivo 1:** [Ex: Criar MVP funcional em 2 semanas com integração básica ClickUp]
2. **Objetivo 2:** [Ex: Implementar notificações automáticas via WhatsApp para tarefas urgentes]
3. **Objetivo 3:** [Ex: Deploy em Docker Swarm com 99% uptime]
4. **Objetivo 4:** [Opcional]
5. **Objetivo 5:** [Opcional]

### **Critério de Sucesso** (Como saberá que funcionou?)
- [Ex: MVP rodando em produção]
- [Ex: 10 usuários testando por 1 semana]
- [Ex: Economizando 2h/dia de gestão manual]

### **Critério de Pivô** (Quando desistir ou mudar direção?)
- [Ex: Se custo de APIs > $100/mês]
- [Ex: Se levar > 4 semanas para MVP]
- [Ex: Se não usar consistentemente por 2 semanas]

---

## 📊 Timeline e Budget

### **Timeline Estimado**
- **Duração Total:** [Ex: 3 semanas]
- **Horas/Semana:** [Ex: 15h/semana]
- **Total de Horas:** [Ex: 45h total]

### **Budget de Custo**
- **APIs (mensal):** [Ex: $30/mês (Gemini $10, Supabase $0, n8n $20)]
- **Infra (mensal):** [Ex: $5/mês (VPS Digital Ocean)]
- **One-time costs:** [Ex: $0 (usando ferramentas gratuitas)]
- **Budget Total (3 meses):** [Ex: $105]

### **Budget de Tempo de Agent**
- **Gemini (cheap):** [Ex: 80% do tempo]
- **Claude (premium):** [Ex: 20% para análises complexas]
- **Custo estimado IA:** [Ex: $15 total do projeto]

---

## 🛠️ Stack Técnico

### **Linguagens**
- [X] Python 3.11
- [ ] JavaScript/TypeScript
- [ ] Outra: ___________

### **Frameworks/Libs**
- [ ] React/Next.js (frontend)
- [ ] Node.js/Express (backend)
- [X] FastAPI (backend Python)
- [X] n8n (workflows)
- [ ] Outro: ___________

### **Database**
- [X] Supabase (PostgreSQL + pgvector)
- [ ] MongoDB
- [ ] MySQL
- [ ] SQLite (local dev)
- [ ] Outro: ___________

### **Deploy/Infra**
- [X] Docker Swarm
- [ ] Docker Compose (local apenas)
- [ ] Vercel/Netlify
- [ ] AWS/GCP/Azure
- [ ] Outro: ___________

### **IA/LLM**
- [X] Gemini API (Gemini 1.5 Flash - default)
- [X] Claude API (Claude 3.5 Sonnet - ocasional)
- [ ] Ollama (local)
- [ ] Outro: ___________

### **Integrações**
- [X] Google Calendar
- [X] ClickUp API
- [X] WhatsApp Business API
- [ ] Gmail
- [ ] Slack
- [ ] Outras: ___________

---

## 🤖 Agents a Usar Neste Projeto

**Marque os agents que fazem sentido para este projeto:**

### **Core (Sempre usar)**
- [X] **CHALLENGER** - Crítico radical (viabilidade, pragmatismo) - SEMPRE USE!

### **Desenvolvimento de Software**
- [ ] **PM** (Product Manager) - Gestão de produto, PRD
- [ ] **Analyst** (Business Analyst) - Análise de requisitos, stories
- [ ] **Architect** - Arquitetura técnica, decisões de design
- [ ] **SM** (Scrum Master) - Gerenciamento de sprint, retrospectivas
- [ ] **DEV** - Desenvolvimento, implementação
- [ ] **TEA** (Test Engineer) - Testes, QA, automação
- [ ] **UX Designer** - Design de interface, experiência do usuário
- [ ] **Technical Writer** - Documentação técnica

### **Desenvolvimento de Games**
- [ ] **Game Designer** - Game design documents, mecânicas
- [ ] **Game Developer** - Implementação de jogos
- [ ] **Game Architect** - Arquitetura de jogos

### **Consultoria/Estratégia** (Projetos não-software)
- [ ] **Analyst** - Análise estratégica, pesquisa
- [ ] **PM** - Gestão de deliverables, timeline
- [ ] **Technical Writer** - Relatórios, apresentações

### **Pessoal (Se aplicável)**
- [ ] **Coaching** - Motivação diária, metas
- [ ] **Terapia** - TCC mensal (projetos pessoais longos)
- [ ] **Relacionamentos** - Família (se projeto envolve tempo familiar)
- [ ] **Finanças** - Gestão financeira (se projeto tem componente financeiro)

### **Orquestração**
- [ ] **Orquestrador** (ELabs Master) - Maestro central multi-agente
- [ ] **Party Mode** - Discussões em grupo com múltiplos agents

---

## 📋 Workflows Planejados

**Workflows ELabs-Agile que você vai usar:**

### **Phase 1: Analysis**
- [ ] `brainstorm-project` - Brainstorm de ideias
- [ ] `product-brief` - Brief inicial do projeto
- [ ] `research` - Pesquisa de mercado/técnica
- [ ] Outro: ___________

### **Phase 2: Planning**
- [ ] `prd` - Product Requirements Document
- [ ] `tech-spec` - Technical Specification (Level 1-2)
- [ ] `create-epics-and-stories` - Criar backlog
- [ ] `gdd` - Game Design Document (games)
- [ ] Outro: ___________

### **Phase 3: Solutioning** (Level 3-4 apenas)
- [ ] `architecture` - Arquitetura técnica
- [ ] `solutioning-gate-check` - Validação antes de implementar
- [ ] Outro: ___________

### **Phase 4: Implementation**
- [ ] `sprint-planning` - Planejamento de sprint
- [ ] `dev-story` - Desenvolvimento de stories
- [ ] `code-review` - Revisão de código
- [ ] `story-done` - Marcar story como concluída
- [ ] Outro: ___________

---

## 🔧 Ambiente e Ferramentas

### **Máquina Local**
- **OS:** [Ex: Windows 11]
- **IDE:** [Ex: VSCode, Cursor]
- **Docker:** [X] Instalado [ ] Não instalado
- **Git:** [X] Configurado [ ] Não configurado

### **Ferramentas Externas**
- **ClickUp:** [X] Conta configurada
- **Supabase:** [X] Projeto criado: [nome-do-projeto]
- **n8n:** [X] Instância rodando em: [URL ou local]
- **Google Cloud:** [X] APIs habilitadas: [Calendar, Gmail]

### **Chaves de API** (NÃO coloque valores aqui! Use .env)
- [ ] GEMINI_API_KEY configurada
- [ ] ANTHROPIC_API_KEY configurada (opcional)
- [ ] SUPABASE_URL e SUPABASE_KEY configuradas
- [ ] CLICKUP_API_KEY configurada
- [ ] Outras: ___________

---

## 👤 Informações Pessoais/Empresa

**IMPORTANTE:** Agents usam isso para personalizar respostas!

### **Nome/Empresa**
[Ex: Mauricio / Hyperize Consulting]

### **Função/Cargo**
[Ex: Founder, Consultor de IA, Desenvolvedor Full-Stack]

### **Experiência Técnica**
- **Nível geral:** [Iniciante / Intermediário / Avançado / Expert]
- **Python:** [1-5 estrelas]
- **JavaScript:** [1-5 estrelas]
- **DevOps:** [1-5 estrelas]
- **IA/ML:** [1-5 estrelas]

### **Estilo de Trabalho**
- **Preferência de comunicação:** [Direto e pragmático / Detalhado e técnico / Casual e simples]
- **Horário de trabalho:** [Ex: Noites (19h-23h), Fins de semana]
- **Frequência de sessões:** [Ex: 3-4x por semana, 2-3h por sessão]

### **Motivação Principal**
[Por que está fazendo este projeto?]

Exemplo:
> "Quero economizar 10h/semana em gestão manual de projetos, para ter mais tempo
> com família e clientes. Este projeto é investimento na minha produtividade e saúde mental."

---

## 🚨 Constraints e Limitações

**Seja honesto sobre limitações! Agents precisam saber disso.**

### **Constraints de Tempo**
- [Ex: Só tenho noites livres (19h-23h)]
- [Ex: Preciso entregar até dia 30/11/2025]
- [Ex: Não posso trabalhar nos fins de semana]

### **Constraints de Budget**
- [Ex: Budget máximo $50/mês]
- [Ex: Não posso pagar serviços premium]
- [Ex: Preciso usar tier gratuito sempre que possível]

### **Constraints Técnicos**
- [Ex: Não posso usar AWS (só Digital Ocean)]
- [Ex: Não sei React (só Python)]
- [Ex: VPS tem apenas 2GB RAM]

### **Constraints Pessoais**
- [Ex: Tenho TDAH - preciso de tarefas curtas e claras]
- [Ex: Primeira vez usando Docker]
- [Ex: Inglês técnico ok, mas prefiro português]

---

## 📝 Notas Adicionais

**Outras informações importantes que agents devem saber:**

[Escreva aqui qualquer contexto adicional, preferências específicas, histórico do projeto, etc]

Exemplo:
> "Este projeto é continuação de um sistema que já tenho rodando há 6 meses.
> Está em Python puro, mas quero migrar para FastAPI com Supabase.
> Já tenho 150 usuários (família e amigos) usando a versão anterior,
> então preciso garantir migração suave sem perda de dados."

---

## ✅ Checklist de Configuração

**Antes de iniciar desenvolvimento:**

- [ ] Preencheu todas as seções acima
- [ ] Definiu objetivos SMART
- [ ] Escolheu stack técnico
- [ ] Marcou agents que vai usar
- [ ] Configurou chaves de API (em .env)
- [ ] Leu `docs/COMO-INICIAR.md`
- [ ] Testou `start-gemini.bat` ou `start-claude.bat`
- [ ] Inicializou Git (`git init`)

---

## 🔄 Manutenção Deste Arquivo

**Quando atualizar:**
- [ ] Mudou objetivos do projeto
- [ ] Adicionou novo agent
- [ ] Mudou stack técnico
- [ ] Atingiu milestone importante
- [ ] Pivotou direção do projeto

**Frequência:** Revisar a cada 2 semanas ou quando necessário

---

## 📞 Precisa de Ajuda?

**Documentação:**
- `docs/COMO-INICIAR.md` - Primeira sessão
- `docs/COMO-RETOMAR.md` - Retomar projeto
- `docs/ORIENTACOES-AGENT-CLI.md` - Como usar agents CLI
- `../../bmm/docs/` - Documentação completa da metodologia

**Comunidade:**
- Discord BMad: https://discord.gg/gk8jAdXWmj

---

**Última Atualização:** [DATA AQUI]
**Status do Projeto:** [PLANEJAMENTO / DESENVOLVIMENTO / PRODUÇÃO / PAUSADO]

---

**Lembre-se:**
> "Código rodando hoje > Arquitetura perfeita amanhã"
>
> "Seja específico neste arquivo - quanto mais contexto, melhor o agent ajuda!"

**Próximo passo:** Leia `docs/COMO-INICIAR.md` e execute `start-gemini.bat`
