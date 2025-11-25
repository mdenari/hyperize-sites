# 📋 Procedimento Padrão: Checkpoint de Sessão

**Procedimento obrigatório da metodologia ELabs-Agile**

Todo projeto deve criar checkpoints ao final de cada sessão de trabalho para garantir continuidade e evitar perda de contexto.

---

## 🎯 Quando Criar Checkpoint

**Sempre ao final de:**
- Sessões longas (> 1h de trabalho)
- Antes de pausar projeto por > 24h
- Após completar milestone importante
- Quando sistema/IDE pode cair (rede instável, etc)

**Regra de ouro:** Se você não consegue retomar amanhã sem reler tudo, precisa de checkpoint!

---

## 📝 Estrutura do Checkpoint

### **Nome do Arquivo:**
```
CHECKPOINT-SESSAO-YYYY-MM-DD.md
```

**Exemplo:** `CHECKPOINT-SESSAO-2025-11-12.md`

**Localização:** Raiz do projeto

---

### **Template de Checkpoint:**

```markdown
# 🔖 CHECKPOINT DA SESSÃO - [DATA]

**Horário:** [HH:MM AM/PM]
**Status:** [STATUS ATUAL]
**Sessão:** [BREVE DESCRIÇÃO]

---

## ✅ O QUE FOI FEITO

[Liste tudo que foi realizado nesta sessão]

### [Categoria 1]
- ✅ Item 1
- ✅ Item 2

### [Categoria 2]
- ✅ Item 3

---

## ⏸️ ONDE ESTAMOS AGORA

**FASE ATUAL:** [Ex: Phase 4 - Implementation]

**ÚLTIMA ATIVIDADE CONCLUÍDA:**
[Descreva a última coisa que terminou]

**ESTADO DO CÓDIGO:**
[Branches, commits, arquivos em progresso]

**PRÓXIMOS PASSOS:**
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

---

## 📋 TODO LIST

- [x] [Tarefas completadas]
- [ ] **→ [PRÓXIMA TAREFA]** ← Começar por aqui!
- [ ] [Outras pendentes]

---

## 🔧 COMANDOS EXECUTADOS

[Liste comandos importantes que rodou]

```bash
# Exemplos
git commit -m "feat: implementa X"
npm install pacote-y
docker-compose up -d
```

---

## 🚨 BLOCKERS E ATENÇÕES

**Blockers:**
- [ ] [Nenhum] ou [Liste blockers]

**Atenções:**
- [Coisas a lembrar na próxima sessão]

---

## 💡 DECISÕES TÉCNICAS

[Decisões importantes tomadas e por quê]

**Exemplo:**
- Escolhemos PostgreSQL em vez de MongoDB porque [razão]

---

## 📂 ARQUIVOS MODIFICADOS

[Liste arquivos principais criados/editados]

- `src/main.py` - [O que mudou]
- `docs/prd.md` - [O que mudou]

---

## 🔄 COMO RETOMAR

**Se retomar em < 24h:**
1. Ler este checkpoint (5 min)
2. `git status` para ver mudanças
3. Continuar do item marcado **→**

**Se retomar em > 24h:**
1. Ler este checkpoint completo (10 min)
2. Reler `docs/COMO-RETOMAR.md`
3. Revisar backlog/tasks
4. Atualizar `agents/config.md` se necessário

---

**ÚLTIMA ATUALIZAÇÃO:** [DATA HORA]
**STATUS:** [⏸️ PAUSADO / ✅ CONCLUÍDO]
**PRÓXIMA SESSÃO:** [Data estimada]
```

---

## 🎓 Exemplo Prático

### **CHECKPOINT-SESSAO-2025-11-12.md**

```markdown
# 🔖 CHECKPOINT DA SESSÃO - 2025-11-12

**Horário:** 15:30 PM
**Status:** ⏸️ PAUSADO - Implementação 60% completa
**Sessão:** Implementação do módulo de autenticação

---

## ✅ O QUE FOI FEITO

### Código
- ✅ Criado `src/auth/auth.py` com funções de login/signup
- ✅ Implementados testes em `tests/test_auth.py`
- ✅ Integração Supabase autenticação

### Documentação
- ✅ Atualizado `docs/tech-spec.md` com decisões de auth
- ✅ Criado `docs/api/auth.md` com API reference

### Configuração
- ✅ Adicionado Supabase ao `requirements.txt`
- ✅ Configurado `.env.example` com variáveis de auth

---

## ⏸️ ONDE ESTAMOS AGORA

**FASE ATUAL:** Phase 4 - Implementation (Story #3)

**ÚLTIMA ATIVIDADE CONCLUÍDA:**
Implementação de login com Google OAuth funcionando.
Testes passando (8/8).

**ESTADO DO CÓDIGO:**
- Branch: `feature/auth`
- Último commit: `a1b2c3d - feat: add OAuth login`
- Arquivos não commitados: Nenhum

**PRÓXIMOS PASSOS:**
1. Implementar refresh token (1h estimado)
2. Adicionar middleware de autenticação em rotas (30min)
3. Testar end-to-end (30min)
4. Merge para main

---

## 📋 TODO LIST

- [x] Setup Supabase auth
- [x] Implementar login/signup
- [x] Implementar OAuth Google
- [ ] **→ Implementar refresh token** ← Começar aqui!
- [ ] Middleware de autenticação
- [ ] Testes E2E
- [ ] Merge para main

---

## 🔧 COMANDOS EXECUTADOS

```bash
# Criou branch
git checkout -b feature/auth

# Instalou dependências
pip install supabase

# Rodou testes
pytest tests/test_auth.py

# Commitou
git add .
git commit -m "feat: add authentication with Supabase OAuth"
```

---

## 🚨 BLOCKERS E ATENÇÕES

**Blockers:**
- [ ] Nenhum no momento

**Atenções:**
- JWT tokens expiram em 1h (precisa refresh token antes de deploy)
- Supabase RLS precisa ser configurado (fazer em story #4)
- Lembrar de testar com usuário real (não só mock)

---

## 💡 DECISÕES TÉCNICAS

**1. Escolhemos Supabase Auth em vez de custom JWT:**
- Razão: Managed solution, menos código, RLS integrado
- Trade-off: Vendor lock-in aceitável para MVP

**2. OAuth com Google apenas (não Facebook/Twitter por enquanto):**
- Razão: 90% dos usuários tem Google, priorizar MVP
- Futuro: Adicionar outros providers na Fase 2

---

## 📂 ARQUIVOS MODIFICADOS

**Criados:**
- `src/auth/auth.py` - Funções de autenticação
- `tests/test_auth.py` - 8 testes unitários
- `docs/api/auth.md` - API reference

**Modificados:**
- `requirements.txt` - Adicionado supabase
- `docs/tech-spec.md` - Seção de autenticação
- `.env.example` - Variáveis de Supabase

---

## 🔄 COMO RETOMAR

**Se retomar hoje/amanhã:**
1. Ler seção "PRÓXIMOS PASSOS" (começar por refresh token)
2. Abrir `src/auth/auth.py` linha 45 (onde parei)
3. Implementar função `refresh_token()`

**Se retomar depois de 3+ dias:**
1. Ler este checkpoint completo
2. Rodar testes: `pytest tests/test_auth.py` (garantir nada quebrou)
3. Revisar `docs/api/auth.md` (refrescar contexto)
4. Continuar normalmente

---

**ÚLTIMA ATUALIZAÇÃO:** 2025-11-12 15:30 PM
**STATUS:** ⏸️ PAUSADO (60% da story #3 completa)
**PRÓXIMA SESSÃO:** 2025-11-13 (continuar refresh token)
```

---

## 🛠️ Como Criar Checkpoint Rapidamente

### **Durante a Sessão:**

1. Mantenha anotações simples de decisões importantes
2. Liste comandos significativos que executou
3. Marque TODO list conforme avança

### **Ao Final (10-15 min):**

1. Abra template de checkpoint
2. Preencha seções principais
3. Seja específico mas conciso
4. Foque em: **o que foi feito, onde parou, como retomar**

---

## ✅ Checklist de Checkpoint

Antes de encerrar sessão:

- [ ] Checkpoint criado com nome correto (CHECKPOINT-SESSAO-YYYY-MM-DD.md)
- [ ] Seção "O QUE FOI FEITO" preenchida
- [ ] Seção "ONDE ESTAMOS AGORA" atualizada
- [ ] TODO list com item **→ PRÓXIMO** marcado
- [ ] Comandos importantes listados
- [ ] Decisões técnicas documentadas (se houver)
- [ ] Git commit de tudo (ou WIP se incompleto)
- [ ] Checkpoint commitado

---

## 🎯 Boas Práticas

### **✅ FAÇA:**

1. **Seja específico:**
   - ❌ "Trabalhei no auth"
   - ✅ "Implementei login OAuth Google, 8 testes passando"

2. **Liste próximos passos claros:**
   - ❌ "Continuar desenvolvimento"
   - ✅ "Implementar função refresh_token() em src/auth/auth.py linha 45"

3. **Documente decisões:**
   - Por que escolheu tecnologia X
   - Trade-offs considerados
   - Alternativas descartadas

4. **Marque blockers:**
   - Dependências externas
   - Dúvidas técnicas
   - Itens aguardando resposta

5. **Seja honesto sobre % completo:**
   - Não exagere progresso
   - Melhor subestimar que superestimar

### **❌ NÃO FAÇA:**

1. **Checkpoint vago:**
   - Sem detalhes suficientes para retomar

2. **Esquecer de commitar:**
   - Checkpoint sem commit = pode perder tudo

3. **Pular checkpoints:**
   - "Vou lembrar amanhã" (spoiler: não vai)

4. **Checkpoint genérico:**
   - Copiar/colar sem customizar

---

## 🔄 Integração com Metodologia

### **ELabs-Agile Workflows:**

Checkpoint é parte dos workflows:

- **story-done:** Crie checkpoint ao concluir story
- **sprint-planning:** Revise checkpoints do sprint anterior
- **retrospective:** Use checkpoints para analisar o que funcionou

### **Agents CLI:**

Agent pode criar checkpoint automaticamente:

```
Finalizando sessão. Crie CHECKPOINT-SESSAO-[hoje].md com:
- Resumo do que fizemos
- Estado atual
- Próximos passos
- Comandos executados
```

---

## 📊 Benefícios do Checkpoint

**1. Continuidade:**
- Retome trabalho sem perder tempo
- Contexto completo em 5-10 min

**2. Histórico:**
- Entenda evolução do projeto
- Identifique padrões (onde você trava)

**3. Comunicação:**
- Facilita handoff para outro dev
- Documenta decisões para futuro

**4. Accountability:**
- Track progresso real
- Identifique velocity

**5. Recovery:**
- Se sistema cair, checkpoint te salva
- Backup de contexto mental

---

## 🎓 Adaptações por Tipo de Projeto

### **Projeto Solo:**
- Checkpoint mais informal ok
- Foco em retomar rápido

### **Projeto em Equipe:**
- Checkpoint mais detalhado
- Documente decisões compartilhadas
- Facilita handoff

### **Projeto Cliente:**
- Checkpoint como log de horas
- Documente mudanças de requisitos
- Track decisões do cliente

### **Projeto Longo (3+ meses):**
- Checkpoint + weekly summary
- Milestone checkpoints mais detalhados
- Archive checkpoints antigos (> 1 mês)

---

## 📞 Dúvidas?

**Este procedimento é parte oficial da metodologia ELabs-Agile.**

Consulte:
- `docs/COMO-RETOMAR.md` - Como usar checkpoints
- `../../bmm/docs/` - Documentação ELabs-Agile

---

**Última Atualização:** 2025-11-12
**Status:** Procedimento Padrão Aprovado
**Obrigatório:** SIM para todos os projetos ELabs-Agile
