# 📦 ProjectTemplate - Template Base para Projetos

**Template base para todos os projetos ELabs-Agile**

Este é o template master que será copiado para criar novos projetos. Contém estrutura padrão, agents genéricos, scripts de inicialização e orientações.

---

## 📁 Estrutura do Template

```
ProjectTemplate/
├── agents/                     # Agents customizáveis
│   ├── CHALLENGER.md           # Meta-agente crítico
│   ├── config.md               # Configuração do projeto (CUSTOMIZE!)
│   └── (outros agents...)      # Copie do PersonalAgents conforme necessário
│
├── docs/                       # Documentação do projeto
│   ├── COMO-INICIAR.md         # Guia para novo projeto
│   ├── COMO-RETOMAR.md         # Guia para projeto em andamento
│   └── ORIENTACOES-AGENT-CLI.md # O que falar para os agents
│
├── scripts/                    # Scripts de automação
│   ├── setup.sh                # Setup inicial
│   └── (outros scripts...)
│
├── .docker/                    # Docker configurations
│   ├── docker-compose.yml      # Services definition
│   └── .env.example            # Environment template
│
├── src/                        # Código-fonte (quando aplicável)
├── workflows/                  # n8n workflows (exports)
├── tests/                      # Testes automatizados
├── config/                     # Configurações
├── data/                       # Dados locais (gitignored)
│
├── README.md                   # Este arquivo
├── .gitignore                  # Git ignore
├── start-gemini.bat            # Iniciar CLI Gemini
└── start-claude.bat            # Iniciar CLI Claude
```

---

## 🚀 Como Usar Este Template

### **Opção 1: Script Automatizado (Recomendado)**

```bash
# Na pasta ELabs-Agile/scripts/
.\ELabs-init.bat NomeDoProjeto TipoProjeto

# Exemplo:
.\ELabs-init.bat MeuAppIA Projetos_Pessoais
```

Isso cria automaticamente:
- Cópia completa do ProjectTemplate
- Estrutura em `Projetos/TipoProjeto/NomeDoProjeto/`
- Scripts funcionais (start-gemini.bat, start-claude.bat)

### **Opção 2: Cópia Manual**

1. Copie toda pasta `ProjectTemplate/`
2. Cole em `Projetos/[tipo]/[nome-projeto]/`
3. Renomeie pasta para nome do projeto
4. Customize `agents/config.md`
5. Execute setup

---

## ✏️ Customização do Projeto

### **1. Configure agents/config.md**

**OBRIGATÓRIO!** Edite `agents/config.md` com:
- Informações pessoais/empresa
- Objetivos do projeto
- Preferências de trabalho
- Budget e metas
- Integrações (APIs, tools)

### **2. Adicione Agents Especializados**

Copie agents do `PersonalAgents` ou crie novos:
```bash
# Exemplo: adicionar coaching agent
copy ..\..\PersonalAgents\agents\coaching.md agents\
```

Agents disponíveis:
- `coaching.md` - Motivação diária
- `terapia.md` - TCC mensal
- `relacionamentos.md` - Família
- `financas.md` - Gestão financeira
- `empresa.md` - Projetos e negócios
- `orquestrador.md` - Maestro central

### **3. Ajuste Docker (se necessário)**

Edite `.docker/docker-compose.yml` conforme stack do projeto.

### **4. Configure Git**

```bash
git init
git add .
git commit -m "Initial commit from ProjectTemplate"
```

---

## 🤖 Iniciar Agents CLI

### **Gemini (padrão - econômico)**

```bash
.\start-gemini.bat
```

O agent lerá:
1. `agents/config.md` - Configuração do projeto
2. `docs/COMO-INICIAR.md` ou `docs/COMO-RETOMAR.md` - Contexto
3. Outros `agents/*.md` conforme necessário

### **Claude (premium - ocasional)**

```bash
.\start-claude.bat
```

Use para tasks que precisam de maior empatia/profundidade (ex: terapia, análise complexa).

---

## 📚 Arquivos de Orientação

### **docs/COMO-INICIAR.md**
Leia se é a **primeira vez** trabalhando no projeto.

Contém:
- O que é o projeto
- Objetivos principais
- Próximos passos iniciais
- O que dizer ao agent na primeira sessão

### **docs/COMO-RETOMAR.md**
Leia se projeto **já existe** e você está retomando.

Contém:
- Status atual do projeto
- Última sessão de trabalho
- Tarefas pendentes
- O que dizer ao agent para retomar

### **docs/ORIENTACOES-AGENT-CLI.md**
Guia completo de como interagir com agents CLI.

Contém:
- Comandos úteis
- Boas práticas
- Exemplos de prompts
- Troubleshooting

---

## 🔄 Sincronização com Master

Quando o template master (`ELabs-Agile/ProjectTemplate/`) for atualizado:

```bash
# Na pasta ELabs-Agile/scripts/
.\ELabs-sync.bat NomeDoProjeto

# Exemplo:
.\ELabs-sync.bat MeuAppIA
```

Isso faz merge seletivo de:
- Novos agents
- Novos workflows
- Scripts atualizados
- Documentação nova

**Importante:** Suas customizações em `config.md` são preservadas!

---

## 🎯 Metodologia ELabs-Agile

Este template segue a metodologia completa:
- **BMM Module** (`../../bmm/`) - 12 agents, 34 workflows
- **BMB Module** (`../../bmb/`) - Builder tools
- **Core Module** (`../../core/`) - Orchestration

**Workflows disponíveis:**
- Phase 1: Analysis (brainstorm, research, brief)
- Phase 2: Planning (PRD, tech spec, UX design)
- Phase 3: Solutioning (architecture, gate check)
- Phase 4: Implementation (stories, sprints, code review)
- Testing: QA workflows

**Veja:** `../../bmm/docs/` para guias completos

---

## 🔐 Segurança e Privacy

### **O que vai no .gitignore**

```
.env
.env.local
config/secrets.yaml
agents/private/
data/journals/
data/relacionamentos/
data/logs/*.log
data/backups/*.sql
```

### **Dados sensíveis**

Se projeto tem dados pessoais (journals, finanças, relacionamentos):
- Use encryption (AES-256)
- RLS no Supabase
- Backups encriptados

---

## 🛠️ Stack Técnico Sugerido

**Orquestração:**
- Python 3.11+ (orchestrator)
- n8n (workflows visuais)
- Docker Swarm (deploy)

**IA:**
- Gemini 1.5 Flash (default - barato)
- Claude 3.5 Sonnet (premium - ocasional)
- Ollama (local - futuro)

**Database:**
- Supabase Cloud (PostgreSQL + pgvector)
- RLS habilitado

**Integrações:**
- Google (Calendar, Gmail)
- ClickUp, WhatsApp, etc

---

## 📊 Métricas de Sucesso

**Para todo projeto ELabs-Agile, defina:**

- 🎯 Objetivos principais (3-5)
- 📈 KPIs mensuráveis
- ⏱️ Timeline realista
- 💰 Budget de custo (APIs, infra)
- ✅ Critérios de sucesso
- 🔄 Critérios de pivô

**Documente em `agents/config.md`!**

---

## 🚨 Troubleshooting

### **Agent não entende contexto**

1. Verifique se `agents/config.md` está configurado
2. Leia `docs/ORIENTACOES-AGENT-CLI.md`
3. Use prompts mais específicos
4. Consulte `../../bmm/docs/troubleshooting.md`

### **Scripts .bat não funcionam**

1. Verifique paths relativos
2. Execute como administrador se necessário
3. Veja logs em `data/logs/`

### **Docker não sobe**

1. Verifique `.docker/.env`
2. Teste: `docker-compose config`
3. Veja: `../../bmm/docs/troubleshooting.md`

---

## 📝 Checklist de Setup

Antes de começar desenvolvimento:

- [ ] Copiei template para `Projetos/[tipo]/[nome]/`
- [ ] Editei `agents/config.md` com info do projeto
- [ ] Li `docs/COMO-INICIAR.md`
- [ ] Testei `start-gemini.bat`
- [ ] Configurei `.docker/.env` (se aplicável)
- [ ] Inicializei Git
- [ ] Criei primeiro commit

---

## 🎓 Próximos Passos

1. **Leia:** `docs/COMO-INICIAR.md`
2. **Configure:** `agents/config.md`
3. **Inicie:** `start-gemini.bat`
4. **Diga ao agent:** "Leia agents/config.md e docs/COMO-INICIAR.md. Estou começando este projeto. Me ajude a planejar os próximos passos."

---

## 🤝 Contribuindo para o Template

Se desenvolveu algo útil que deve estar no template master:

1. Documente bem
2. Teste em projeto real
3. Adicione em `ELabs-Agile/ProjectTemplate/`
4. Atualize este README
5. Sincronize projetos existentes com `ELabs-sync.bat`

---

## 📞 Suporte

**Documentação:**
- `../../bmm/docs/` - Guias completos
- `docs/` - Orientações deste projeto

**Comunidade:**
- Discord BMad: https://discord.gg/gk8jAdXWmj
- GitHub: (adicionar quando disponível)

---

**Última Atualização:** 2025-11-12
**Versão Template:** 1.0.0
**Status:** Pronto para uso

---

**ProjectTemplate** - Template base para projetos ELabs-Agile
*Copy, Customize, Create* 🏗️✨
