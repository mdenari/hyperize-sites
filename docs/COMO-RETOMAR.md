# 🔄 Como Retomar um Projeto Existente

**Guia para retomar trabalho em projeto já iniciado**

Leia este arquivo se você está **voltando a trabalhar** em um projeto que já foi iniciado anteriormente.

---

## 📋 Checklist Pré-Retomada

Antes de chamar o agent CLI:

- [ ] ✅ Leu último `CHECKPOINT-SESSAO-YYYY-MM-DD.md`
- [ ] ✅ Revisou `agents/config.md` (ainda está atualizado?)
- [ ] ✅ Verificou Git status (`git status`)
- [ ] ✅ Puxou últimas mudanças (`git pull` se trabalho em equipe)
- [ ] ✅ Verificou backlog/tasks pendentes
- [ ] ✅ Tem clareza do objetivo da sessão de hoje

---

## 🎯 Antes de Começar: Responda

### **1. Quanto tempo desde última sessão?**
- [ ] < 24h (ainda fresco na memória)
- [ ] 1-3 dias (preciso refrescar)
- [ ] 1+ semana (preciso revisar tudo)
- [ ] 1+ mês (projeto pausado, retomando agora)

### **2. O que mudou desde então?**
- [ ] Nada, continuo de onde parei
- [ ] Novos requisitos/objetivos
- [ ] Mudança de stack/tecnologia
- [ ] Mudança de timeline/budget
- [ ] Outro: _______

### **3. Qual o objetivo de HOJE?**
[Escreva em 1 frase específica]

Exemplo:
- "Implementar autenticação com Supabase"
- "Corrigir bug X reportado no teste"
- "Criar workflow n8n para notificações"

---

## 📍 Onde Estou?

### **Status Atual do Projeto**

**Fase atual:**
- [ ] Phase 1: Analysis (brainstorm, research, brief)
- [ ] Phase 2: Planning (PRD, tech spec, stories)
- [ ] Phase 3: Solutioning (arquitetura)
- [ ] Phase 4: Implementation (desenvolvimento)
- [ ] Testing & QA
- [ ] Deploy & Production

**Última atividade concluída:**
[Ex: "Criei PRD e 10 user stories prioritizadas"]

**Próxima atividade planejada:**
[Ex: "Implementar story #1 - Setup inicial"]

**Blockers atuais:**
- [ ] Nenhum blocker
- [ ] Técnico: [descreva]
- [ ] Dependência externa: [descreva]
- [ ] Falta de clareza: [descreva]
- [ ] Outro: [descreva]

---

## 📚 Documentação Existente

**Verifique quais docs já existem:**

- [ ] `docs/product-brief.md` - Product Brief
- [ ] `docs/prd.md` - PRD (Product Requirements)
- [ ] `docs/tech-spec.md` - Technical Specification
- [ ] `docs/architecture.md` - Arquitetura
- [ ] `docs/backlog.md` - Backlog de stories
- [ ] `CHECKPOINT-SESSAO-*.md` - Checkpoints anteriores

**Docs mais recentes:**
- [Liste os 2-3 docs mais importantes para revisar hoje]

---

## 🔍 Revisão Rápida (5-10 min)

### **1. Leia Último Checkpoint**
Arquivo: `CHECKPOINT-SESSAO-[data].md`

**Perguntas a responder:**
- O que foi feito na última sessão?
- Onde parou?
- O que estava planejado para hoje?
- Havia algum alerta/atenção?

### **2. Git Status**
```bash
git status
git log --oneline -10
```

**Verificar:**
- Commits recentes (o que foi feito)
- Arquivos não commitados (work in progress)
- Branch atual (main? feature?)

### **3. Backlog/Tasks**
Onde estão suas tasks?
- [ ] `docs/backlog.md`
- [ ] ClickUp
- [ ] GitHub Issues
- [ ] Outro: _______

**Tasks pendentes hoje:**
1. [Task 1]
2. [Task 2]
3. [Task 3]

---

## 💬 O Que Dizer ao Agent (Retomada)

**Copy/paste este prompt no CLI:**

```
Olá! Estou retomando trabalho no projeto [NOME DO PROJETO].

Por favor, leia os seguintes arquivos:
1. agents/config.md - Configuração do projeto
2. CHECKPOINT-SESSAO-[última data].md - Onde paramos
3. docs/COMO-RETOMAR.md - Este arquivo

Contexto da retomada:
- Última sessão: [data]
- Status atual: [ex: Phase 4 - Implementation]
- Última atividade: [ex: "Implementamos story #3"]
- Objetivo de hoje: [seja específico!]

Preciso que você:
1. Revise o contexto e entenda onde estamos
2. Me ajude a planejar a sessão de hoje
3. Identifique se há algum blocker ou dependência
4. Me guie nos próximos passos

[Se houver blockers, mencione aqui]

Vamos começar? Qual o primeiro passo para [objetivo de hoje]?
```

---

## 🎯 Tipos de Retomada

### **Tipo 1: Continuação Normal (< 3 dias)**

**Você lembra do contexto:**
- Leia checkpoint rápido (5 min)
- Revise Git commits
- Continue de onde parou

**Diga ao agent:**
"Continuando de onde paramos. Última sessão implementamos [X]. Hoje vamos fazer [Y]."

---

### **Tipo 2: Retomada Após Pausa (1-2 semanas)**

**Contexto ficou nebuloso:**
1. Leia checkpoint completo (10 min)
2. Revise backlog e prioridades
3. Re-leia PRD/Tech Spec principais
4. Atualize `agents/config.md` se mudou algo

**Diga ao agent:**
"Retomando após [X] dias. Preciso refrescar contexto completo. Por favor, me faça um resumo do projeto e onde estávamos."

---

### **Tipo 3: Retomada Após Pausa Longa (1+ mês)**

**Projeto estava congelado:**
1. Leia TUDO do início (30-60 min):
   - `COMO-INICIAR.md`
   - Product Brief
   - PRD
   - Tech Spec
   - Todos checkpoints
2. Avalie se objetivos ainda fazem sentido
3. Convoque CHALLENGER para re-validar viabilidade
4. Possivelmente crie novo plano

**Diga ao agent:**
"Retomando projeto após [X] meses pausado. Preciso de uma revisão completa: objetivos ainda fazem sentido? Arquitetura ainda é viável? O que mudou no mercado/tecnologia? Devemos continuar ou pivotar?"

---

### **Tipo 4: Retomada com Mudanças**

**Algo mudou (requisitos, stack, timeline):**
1. Atualize `agents/config.md` com mudanças
2. Documente o que mudou e por quê
3. Convoque PM/Analyst para re-avaliar impacto
4. Possivelmente atualize PRD/Tech Spec
5. Re-priorize backlog

**Diga ao agent:**
"Retomando projeto mas houve mudanças: [liste mudanças]. Preciso re-avaliar impacto no projeto. Convoque PM e Analyst para me ajudar a ajustar documentação e backlog."

---

## 🔄 Fluxo Típico de Retomada

### **1. Preparação (10-15 min)**
```
1. Ler checkpoint
2. Git pull
3. Revisar backlog
4. Definir objetivo da sessão
```

### **2. Contexto com Agent (5-10 min)**
```
1. Iniciar CLI (start-gemini.bat ou start-claude.bat)
2. Agent lê checkpoint e config.md
3. Agent resume status e próximos passos
4. Você confirma ou ajusta plano
```

### **3. Execução (1-3h)**
```
1. Trabalhar na task de hoje
2. Commits incrementais
3. Testar conforme avança
4. Documentar decisões importantes
```

### **4. Finalização (10-15 min)**
```
1. Commit final
2. Atualizar backlog (marcar done)
3. Criar novo checkpoint
4. Planejar próxima sessão
```

---

## 📝 Atualizar Documentação

**Durante a retomada, mantenha atualizado:**

### **A cada sessão:**
- [ ] Criar novo `CHECKPOINT-SESSAO-[hoje].md`
- [ ] Git commits frequentes
- [ ] Atualizar backlog (done/in-progress)

### **Quando aplicável:**
- [ ] Atualizar `agents/config.md` (se objetivos mudaram)
- [ ] Atualizar PRD (se requisitos novos)
- [ ] Atualizar Tech Spec (se decisões técnicas mudaram)
- [ ] Atualizar Architecture (se arquitetura evoluiu)

---

## 🚨 Sinais de Alerta

**Se ao retomar você percebe:**

### **🔴 Projeto perdeu sentido**
- Objetivos não fazem mais sentido
- Stack escolhido ficou obsoleto
- Problema que resolvia não existe mais

**→ Ação:** Convoque CHALLENGER + PM para re-avaliar. Considere pivô ou arquivamento.

### **🟡 Projeto viável mas precisa ajustes**
- Alguns requisitos mudaram
- Timeline precisa ser estendida
- Budget precisa ajuste

**→ Ação:** Atualize config.md e docs. Re-priorize backlog.

### **🟢 Projeto no caminho certo**
- Objetivos ainda válidos
- Progresso visível
- Próximos passos claros

**→ Ação:** Continue normalmente!

---

## 🎯 Templates de Prompts

### **Prompt: Resumo Rápido**
```
Me faça um resumo executivo (3-5 frases):
- O que é este projeto
- Fase atual
- Última coisa feita
- Próximos 3 passos
```

### **Prompt: Identificar Blockers**
```
Analisando o checkpoint anterior e status atual,
identifique possíveis blockers ou dependências
que podem me impedir de avançar hoje.
```

### **Prompt: Re-priorizar**
```
Considerando mudanças [liste mudanças],
me ajude a re-priorizar o backlog.
Convoque CHALLENGER para validar viabilidade.
```

### **Prompt: Continuar Story**
```
Estávamos implementando story #[X]: [nome].
Status: [ex: 60% completo].
Revisei o código em [arquivo].
Me ajude a continuar de onde parei.
```

---

## ✅ Checklist de Finalização (Fim da Sessão)

Antes de encerrar:

- [ ] Commitei todas mudanças
- [ ] Atualizei backlog (marcado done/in-progress)
- [ ] Criei checkpoint da sessão
- [ ] Documentei decisões importantes (se houver)
- [ ] Deixei projeto em estado "retomável"
- [ ] Sei exatamente o que fazer na próxima sessão

---

## 💡 Boas Práticas de Retomada

1. **Checkpoint é sagrado:** Sempre crie ao final da sessão
2. **Commits frequentes:** Não espere "terminar tudo"
3. **Objetivo claro:** Sessão sem objetivo = procrastinação
4. **Timebox:** Defina tempo (ex: 2h hoje) e foque
5. **Documente dúvidas:** Se algo não está claro, documente

---

## 🔄 Sincronizar com Master

**Se o template ProjectTemplate foi atualizado:**

```bash
# Na pasta ELabs-Agile/scripts/
.\ELabs-sync.bat [NomeDoProjeto]
```

Isso traz:
- Novos agents
- Scripts atualizados
- Docs novos
- Bugfixes

**Suas customizações são preservadas!**

---

## 📞 Precisa de Ajuda?

**Se perdido:**
1. Leia todos checkpoints recentes (entenda histórico)
2. Releia COMO-INICIAR.md (objetivos originais)
3. Convoque PM + Analyst para realinhamento
4. Use CHALLENGER para questionar viabilidade

**Consulte:**
- `ORIENTACOES-AGENT-CLI.md` - Como usar agents
- `../../bmm/docs/troubleshooting.md` - Troubleshooting

**Comunidade:**
- Discord BMad: https://discord.gg/gk8jAdXWmj

---

**Boa retomada!** 💪

Lembre-se:
> "Progresso consistente > Sessões perfeitas"

**Próximo checkpoint:** Ao final desta sessão, crie `CHECKPOINT-SESSAO-[hoje].md`

---

**Última Atualização:** 2025-11-12
