# 🚀 Como Iniciar um Novo Projeto

**Guia para primeira sessão de trabalho neste projeto**

Leia este arquivo se você está **começando um projeto do zero** usando o template ProjectTemplate.
---

## 📋 Checklist Pré-Início

Antes de chamar o agent CLI, certifique-se de:

- [ ] ✅ Copiou template ProjectTemplate para pasta do projeto
- [ ] ✅ Editou `agents/config.md` com informações do projeto
- [ ] ✅ Definiu objetivos principais (3-5) em `config.md`
- [ ] ✅ Configurou budget estimado (tempo e dinheiro)
- [ ] ✅ Escolheu stack técnico (se já sabe)
- [ ] ✅ Tem acesso a ferramentas necessárias (APIs, cloud, etc)

---

## 🎯 O que é Este Projeto?

**Nome:** [CUSTOMIZE EM config.md]

**Descrição resumida:**
[Descreva em 2-3 frases o que este projeto faz ou resolve]

**Problema que resolve:**
[Qual dor ou necessidade este projeto atende?]

**Público-alvo:**
[Para quem é este projeto? Você? Clientes? Empresa?]

---

## 🎪 Objetivos Principais

**Defina 3-5 objetivos claros:**

1. **Objetivo 1:** [Ex: Criar MVP funcional em 2 semanas]
2. **Objetivo 2:** [Ex: Integrar com API X]
3. **Objetivo 3:** [Ex: Deploy em Docker Swarm]
4. **Objetivo 4:** [Opcional]
5. **Objetivo 5:** [Opcional]

**Critério de sucesso:**
- [Como você saberá que o projeto foi bem-sucedido?]
- [Exemplo: MVP rodando + 10 usuários testando]

---

## 📊 Informações do Projeto

### **Tipo de Projeto**
- [ ] Projeto pessoal
- [ ] Projeto empresarial (cliente)
- [ ] Produto próprio (SaaS)
- [ ] Estudo/aprendizado
- [ ] Outro: _______

### **Complexidade (ELabs-Agile Levels)**
- [ ] Level 0-1: Bug fix ou feature pequena
- [ ] Level 2: Feature média com PRD
- [ ] Level 3-4: Projeto completo (PRD + Arquitetura)

### **Timeline Estimado**
- [ ] < 1 semana
- [ ] 1-2 semanas
- [ ] 2-4 semanas
- [ ] 1-3 meses
- [ ] 3+ meses

### **Budget**
- **Tempo:** [Ex: 40h total, 10h/semana]
- **Dinheiro:** [Ex: $50/mês em APIs, $100 em infra]

---

## 🛠️ Stack Técnico Planejado

**Linguagens:**
- [ ] Python
- [ ] JavaScript/TypeScript
- [ ] Outra: _______

**Frameworks/Libs:**
- [ ] React/Next.js (frontend)
- [ ] Node.js/Express (backend)
- [ ] n8n (workflows)
- [ ] Outro: _______

**Database:**
- [ ] Supabase (PostgreSQL)
- [ ] MongoDB
- [ ] MySQL
- [ ] Outro: _______

**Deploy:**
- [ ] Docker Swarm
- [ ] Vercel/Netlify
- [ ] AWS/GCP/Azure
- [ ] Outro: _______

**IA/LLM:**
- [ ] Gemini API (default)
- [ ] Claude API (ocasional)
- [ ] Ollama (local)
- [ ] Outro: _______

---

## 🤖 Agents que Você Vai Usar

**Marque os agents que fazem sentido para este projeto:**

### **Core (Sempre usar)**
- [x] **CHALLENGER** - Crítico radical (viabilidade)
- [ ] **Orquestrador** - Maestro central
- [ ] **Coaching** - Motivação e metas diárias

### **Desenvolvimento**
- [ ] **PM** - Product Management
- [ ] **Analyst** - Business Analysis
- [ ] **Architect** - Technical Architecture
- [ ] **DEV** - Development
- [ ] **TEA** - Testing & QA

### **Outros**
- [ ] **Terapia** - TCC mensal (projetos longos)
- [ ] **Relacionamentos** - Família (se aplicável)
- [ ] **Finanças** - Gestão financeira
- [ ] **Empresa** - Gestão de projetos

---

## 🚀 Próximos Passos (Primeira Sessão)

### **Fase 1: Setup (30 min)**
1. Configure `.docker/.env` (se aplicável)
2. Inicialize Git
3. Teste ambiente local

### **Fase 2: Planejamento (1-2h com agent)**
1. Inicie `start-gemini.bat`
2. Diga ao agent: (veja prompt abaixo)
3. Agent convoca PM, Analyst, Architect
4. Cria documentação inicial (PRD, Tech Spec)

### **Fase 3: Primeiro Sprint (restante da semana)**
1. Agent cria backlog de stories
2. Prioriza usando CHALLENGER
3. Desenvolve primeira feature
4. Deploy MVP

---

## 💬 O Que Dizer ao Agent (Primeira Sessão)

**Copy/paste este prompt no CLI:**

```
Olá! Estou iniciando um novo projeto chamado [NOME DO PROJETO].

Por favor, leia os seguintes arquivos:
1. agents/config.md - Configuração e objetivos
2. docs/COMO-INICIAR.md - Este arquivo

Contexto do projeto:
- Tipo: [pessoal/empresarial/produto]
- Objetivo principal: [descreva em 1 frase]
- Timeline: [ex: 2 semanas para MVP]
- Stack: [Python, Supabase, Docker Swarm]

Preciso que você:
1. Entenda o contexto completo do projeto
2. Convoque os agents necessários (PM, Analyst, Architect)
3. Me ajude a criar o Product Brief e PRD inicial
4. Defina o backlog de stories priorizadas
5. Me guie nos próximos passos

Use o agent CHALLENGER para questionar e garantir viabilidade.

Vamos começar pela fase de planejamento. Qual o primeiro passo?
```

---

## 🎯 Workflows ELabs-Agile a Usar

**Para projeto novo (greenfield):**

### **Phase 1: Analysis**
1. `*brainstorm-project` - Geração de ideias
2. `*product-brief` - Brief inicial
3. `*research` - Pesquisa de mercado/técnica (opcional)

### **Phase 2: Planning**
1. `*prd` - Product Requirements Document
2. `*tech-spec` - Technical Specification (Level 2+)
3. `*create-epics-and-stories` - Backlog

### **Phase 3: Solutioning** (Level 3-4 apenas)
1. `*architecture` - Arquitetura técnica
2. `*solutioning-gate-check` - Validação

### **Phase 4: Implementation**
1. `*sprint-planning` - Planejamento sprint
2. `*dev-story` - Desenvolvimento de stories
3. `*code-review` - Revisão de código
4. `*story-done` - Conclusão de stories

**Veja:** `../../bmm/docs/` para guias detalhados de cada workflow

---

## 📝 Documentação Inicial a Criar

**Com ajuda do agent, crie:**

1. **Product Brief** (`docs/product-brief.md`)
   - Problema, solução, objetivos
   - 2-3 páginas

2. **PRD** (`docs/prd.md`)
   - Requisitos funcionais e não-funcionais
   - User stories
   - 5-10 páginas

3. **Tech Spec** (`docs/tech-spec.md`) - Se Level 2+
   - Arquitetura, stack, decisões técnicas
   - 3-5 páginas

4. **Backlog** (`docs/backlog.md`)
   - Epics e stories priorizadas
   - Estimativas (story points)

5. **Architecture** (`docs/architecture.md`) - Se Level 3-4
   - Diagramas, componentes, integrações
   - 10+ páginas

---

## 🔄 Depois da Primeira Sessão

**Quando retomar o projeto:**
- Leia `COMO-RETOMAR.md` (não este arquivo)
- Use checkpoints (crie `CHECKPOINT-SESSAO-YYYY-MM-DD.md`)
- Mantenha `agents/config.md` atualizado

---

## ✅ Checklist de Finalização (Primeira Sessão)

Ao final da primeira sessão, você deve ter:

- [ ] Product Brief criado
- [ ] PRD inicial criado (pode ser draft)
- [ ] Backlog de stories definido
- [ ] Tech Spec iniciado (se Level 2+)
- [ ] Architecture iniciada (se Level 3-4)
- [ ] Primeiro commit no Git
- [ ] Ambiente de desenvolvimento configurado
- [ ] Checkpoint da sessão criado

---

## 🚨 Red Flags (Atenção!)

**Se após primeira sessão você ainda não tem clareza sobre:**
- [ ] Qual problema o projeto resolve
- [ ] Quem é o público-alvo
- [ ] Qual MVP mínimo viável
- [ ] Stack técnico básico
- [ ] Próximos 3 passos concretos

**→ Convoque CHALLENGER agent para questionar e refinar!**

---

## 💡 Dicas de Sucesso

1. **Seja específico:** Quanto mais contexto no `config.md`, melhor
2. **Use CHALLENGER:** Questione tudo, garanta viabilidade
3. **MVP first:** Comece pequeno, itere rápido
4. **Documente:** Crie checkpoint após cada sessão
5. **Commit cedo:** Git commit frequente, mesmo em docs

---

## 📞 Precisa de Ajuda?

**Consulte:**
- `ORIENTACOES-AGENT-CLI.md` - Como usar agents CLI
- `../../bmm/docs/quick-start.md` - Quick start ELabs-Agile
- `../../bmm/docs/troubleshooting.md` - Resolução de problemas

**Comunidade:**
- Discord BMad: https://discord.gg/gk8jAdXWmj

---

**Boa sorte no seu projeto!** 🚀

Lembre-se:
> "Código rodando hoje > Arquitetura perfeita amanhã"

**Próxima leitura:** Após primeira sessão, leia `COMO-RETOMAR.md`

---

**Última Atualização:** 2025-11-12
