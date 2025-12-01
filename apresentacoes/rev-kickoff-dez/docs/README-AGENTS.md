# 🤖 Guia de Agentes - Estrutura de 3 Camadas

**Como usar, customizar e criar agentes neste projeto**

---

## 📁 Estrutura de 3 Camadas

```
agents/
├── *.md                    ← CAMADA 1: Agentes padrão (versionados)
│   ├── pm.md
│   ├── analyst.md
│   ├── architect.md
│   ├── dev.md
│   ├── tea.md
│   ├── CHALLENGER.md
│   └── config.md
│
├── custom/                 ← CAMADA 2: Customizações (NÃO versionadas)
│   ├── pm-hyperize.md
│   ├── analyst-custom.md
│   └── .gitkeep
│
└── private/                ← CAMADA 3: Privados (NÃO versionados)
    ├── terapeuta.md
    ├── financeiro.md
    └── .gitkeep
```

---

## 🎯 Quando Usar Cada Camada

### **CAMADA 1: agents/*.md** (Agentes Padrão)

**Uso:**
- Agentes copiados da metodologia ELabs-Agile
- Templates utilizáveis como estão
- Podem ser versionados no Git

**Exemplos:**
- `pm.md` - Product Manager
- `analyst.md` - Business Analyst
- `architect.md` - Technical Architect
- `dev.md` - Developer
- `CHALLENGER.md` - Crítico radical

**Quando usar:**
- ✅ Agente funciona como está
- ✅ Não precisa customização
- ✅ Pode ser compartilhado entre projetos

---

### **CAMADA 2: agents/custom/** (Customizações)

**Uso:**
- Versões customizadas de agentes padrão
- Específicos deste projeto
- NÃO versionados no Git
- Visíveis para time local

**Exemplos:**
- `pm-hyperize.md` - PM adaptado para Hyperize
- `analyst-custom.md` - Analyst com foco em precificação
- `dev-frontend.md` - DEV especializado em React

**Quando usar:**
- ✅ Precisa adaptar agente para projeto específico
- ✅ Adicionar contexto do projeto
- ✅ Customizar tom/abordagem
- ❌ NÃO para info sensível (use private/)

**Como criar:**
```bash
scripts\customize-agent.bat pm
# Cria: agents\custom\pm-custom.md
```

---

### **CAMADA 3: agents/private/** (Privados)

**Uso:**
- Agentes com informações sensíveis
- NÃO versionados no Git
- NÃO compartilhar com outros
- Apenas uso local

**Exemplos:**
- `terapeuta.md` - TCC, saúde mental
- `financeiro.md` - Finanças pessoais, salários
- `relacionamentos.md` - Família, relacionamentos

**Quando usar:**
- ✅ Informações pessoais/confidenciais
- ✅ Dados financeiros sensíveis
- ✅ Saúde mental/terapia
- ✅ Relacionamentos privados

**Como criar:**
```bash
scripts\create-agent.bat TERAPEUTA private
# Cria: agents\private\TERAPEUTA.md
```

---

## 🛠️ Scripts Disponíveis

### **1. customize-agent.bat** - Customizar Agente Existente

**Uso:**
```bash
cd scripts
customize-agent.bat NomeDoAgente [custom|private]
```

**Exemplos:**
```bash
# Customizar PM para este projeto
customize-agent.bat pm

# Customizar Analyst como privado
customize-agent.bat analyst private
```

**O que faz:**
1. Copia agente de `agents/pm.md` → `agents/custom/pm-custom.md`
2. Adiciona header de customização
3. Abre para edição
4. NÃO versiona no Git (já está em .gitignore)

---

### **2. create-agent.bat** - Criar Novo Agente

**Uso:**
```bash
cd scripts
create-agent.bat NomeDoAgente [custom|private]
```

**Exemplos:**
```bash
# Criar agente financeiro (custom)
create-agent.bat FINANCEIRO custom

# Criar agente terapeuta (private)
create-agent.bat TERAPEUTA private
```

**O que faz:**
1. Cria template completo com seções
2. Salva em `agents/custom/` ou `agents/private/`
3. Abre para edição
4. Pronto para preencher e usar

---

## 📋 Fluxos Comuns

### **Fluxo 1: Usar Agente Padrão**

```
1. Projeto criado com ELabs-init.bat
   → 12+ agentes copiados para agents/

2. Use diretamente:
   "Preciso que o agent PM me ajude a criar o PRD"

3. Agent CLI lê agents/pm.md
```

**Simples e direto!**

---

### **Fluxo 2: Customizar para Projeto**

```
1. Projeto precisa PM com contexto Hyperize

2. Customize:
   scripts\customize-agent.bat pm

3. Edite agents/custom/pm-custom.md:
   - Adicione contexto Hyperize
   - Adapte tom para consultoria
   - Adicione conhecimento do cliente

4. Use:
   "Use o agent PM customizado (pm-custom) para criar PRD"
```

---

### **Fluxo 3: Criar Agente Novo**

```
1. Projeto precisa análise financeira específica

2. Crie:
   scripts\create-agent.bat FINANCEIRO custom

3. Preencha template:
   - Propósito: Análise financeira e precificação
   - Expertise: Modelagem financeira, ROI, Value-based pricing
   - Deliverables: Modelo .xlsx, Apresentação .pptx

4. Use:
   "Convoque o agent FINANCEIRO para criar modelo de precificação"
```

---

### **Fluxo 4: Promover Custom → Template**

```
1. Agent custom/FINANCEIRO.md ficou muito útil

2. Quer usar em outros projetos

3. Promova:
   a) Copie para ELabs-Agile/bmm/agents/financeiro.md
   b) OU use bmb/create-agent para formalizar
   c) Agent vira template oficial

4. Próximos projetos já terão FINANCEIRO disponível
```

---

## 🎨 Anatomia de um Agente

### **Seções Essenciais:**

```markdown
# NOME DO AGENT

## 🎯 Propósito
[O que este agente faz, em 2-3 frases]

## 🧠 Expertise
[Áreas de conhecimento]

## 📋 Responsabilidades
[O que o agente deve fazer]

## 🎭 Personalidade e Estilo
[Como o agente se comunica]

## 🔧 Ferramentas e Métodos
[Ferramentas que usa, frameworks]

## 🤝 Colaboração
[Com quais outros agents trabalha]

## ⚙️ Instruções de Uso
[Como e quando convocar]
```

---

## 🔄 Versionamento e Git

### **O que É versionado:**
```
✅ agents/*.md           (agentes padrão)
✅ agents/config.md      (configuração)
❌ agents/custom/        (customizações)
❌ agents/private/       (privados)
```

### **.gitignore configurado:**
```gitignore
# Customizações (não versionar)
agents/custom/
!agents/custom/.gitkeep

# Privados (não versionar)
agents/private/
!agents/private/.gitkeep

# Sufixos (não versionar)
agents/*-custom.md
agents/*-private.md
```

---

## 🎯 Boas Práticas

### **✅ DO:**
- Use agentes padrão quando possível
- Customize apenas quando necessário
- Crie agentes private para info sensível
- Documente bem agentes novos
- Teste antes de usar em produção
- Promova bons agentes para template

### **❌ DON'T:**
- Editar agentes padrão diretamente (customize!)
- Versionar agentes private no Git
- Criar agent novo quando existe padrão
- Deixar TODOs/placeholders no código
- Compartilhar private agents

---

## 📚 Agentes Disponíveis (Padrão)

### **Core Development (8 agents)**
- **pm.md** - Product Management, PRD, estratégia
- **analyst.md** - Business Analysis, requisitos, stories
- **architect.md** - Technical Architecture, decisões técnicas
- **sm.md** - Scrum Master, sprints, retrospectivas
- **dev.md** - Development, implementação de código
- **tea.md** - Test Engineering, QA, automação
- **ux-designer.md** - UX/UI Design, experiência do usuário
- **tech-writer.md** - Documentação técnica

### **Game Development (3 agents)**
- **game-designer.md** - Game design, mecânicas
- **game-developer.md** - Implementação de jogos
- **game-architect.md** - Arquitetura de games

### **Core Methodology (1 agent)**
- **CHALLENGER.md** - Crítico radical, viabilidade

---

## 🔮 Futuro: Supabase

**Planejado:**
```
Supabase:
├── agent_templates/           ← Templates master
├── projects/
│   └── projeto1/
│       ├── agents_used/       ← Quais usa
│       ├── agents_custom/     ← Customizações
│       └── history/           ← Histórico de uso
```

**Vantagens:**
- ✅ Versionamento automático
- ✅ Sync entre projetos
- ✅ Histórico de customizações
- ✅ Promover agent = 1 botão
- ✅ Acesso de qualquer lugar

---

## ❓ FAQ

### **P: Posso editar agents/*.md diretamente?**
**R:** Pode, mas NÃO recomendado. Use `customize-agent.bat` para criar versão customizada.

### **P: Como uso um agent customizado?**
**R:** No CLI, referencie pelo nome: "Use agent pm-custom" ou "agents/custom/pm-custom.md"

### **P: Posso ter múltiplas versões do mesmo agent?**
**R:** SIM! Ex: `pm.md`, `custom/pm-hyperize.md`, `custom/pm-elabs.md`

### **P: Como compartilho agent custom com time?**
**R:** Se não tem info sensível, pode versionar manualmente. Ou promova para template.

### **P: Agent private é seguro?**
**R:** É ignorado pelo Git, mas fica local. Para máxima segurança, use encryption.

### **P: Como atualizo agents padrão quando ELabs-Agile atualiza?**
**R:** Por enquanto manual. Futuro: `sync-agents.bat` ou Supabase auto-sync.

---

## 📞 Precisa de Ajuda?

**Documentação:**
- Este arquivo: `docs/README-AGENTS.md`
- Template de agent: Use `create-agent.bat` e veja template gerado
- Metodologia completa: `bmm/docs/`

**Scripts:**
- `scripts/customize-agent.bat` - Customizar existente
- `scripts/create-agent.bat` - Criar novo
- `bmb/workflows/create-agent/` - Workflow completo (avançado)

---

**Última Atualização:** 2025-11-25
**Versão:** 2.0 (Estrutura de 3 Camadas)

---

🤖 **Agents são o coração do ELabs-Agile!**
*Use-os, customize-os, crie novos - explore possibilidades!*
