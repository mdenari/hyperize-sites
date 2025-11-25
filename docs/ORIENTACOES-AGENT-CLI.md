# 🤖 Orientações para Usar Agents CLI

**Guia completo de interação com Gemini CLI e Claude CLI**

---

## 🎯 O que são Agents CLI?

**Agents CLI** são interfaces de linha de comando para modelos de IA (Gemini, Claude) que funcionam como assistentes especializados para desenvolvimento.

**Benefícios:**
- 🧠 Contexto de projeto completo
- 📝 Leem arquivos .md (agents, docs, config)
- 🔄 Memória de sessão
- 🛠️ Executam comandos e escrevem código
- 🎯 Seguem metodologia ELabs-Agile

---

## 🚀 Iniciando uma Sessão

### **Gemini CLI (Default - Econômico)**

```bash
.\start-gemini.bat
```

**Quando usar:**
- Desenvolvimento geral (80% das tasks)
- Planejamento e documentação
- Code review
- Troubleshooting

**Custo:** ~$0.50/1000 tokens (6x mais barato que Claude)

---

### **Claude CLI (Premium - Ocasional)**

```bash
.\start-claude.bat
```

**Quando usar:**
- Análise complexa (arquitetura, decisões técnicas)
- Empatia necessária (terapia cognitiva, coaching profundo)
- Raciocínio avançado (debugging difícil)
- Code generation sofisticado

**Custo:** ~$3/1000 tokens

---

## 📖 Como os Agents Entendem o Projeto

### **Arquivos que o Agent Lê Automaticamente:**

1. **`agents/config.md`** - Configuração e objetivos do projeto
2. **`docs/COMO-INICIAR.md`** (primeira vez)
3. **`docs/COMO-RETOMAR.md`** (retomada)
4. **`CHECKPOINT-SESSAO-*.md`** (último checkpoint)
5. **Outros `agents/*.md`** conforme necessário

### **Como Solicitar Leitura:**

```
Por favor, leia:
- agents/config.md
- docs/prd.md
- CHECKPOINT-SESSAO-2025-11-12.md
```

---

## 💬 Anatomia de um Bom Prompt

### **Estrutura Recomendada:**

```
[1. CONTEXTO]
Estou trabalhando em [projeto X] que faz [Y].

[2. ESTADO ATUAL]
Já implementei [A, B, C].
Estou na fase de [D].

[3. OBJETIVO]
Preciso fazer [objetivo específico].

[4. RESTRIÇÕES/PREFERÊNCIAS]
- Usar stack [tecnologia]
- Prazo: [tempo]
- Budget: [custo]

[5. PEDIDO ESPECÍFICO]
Me ajude a [ação concreta].
```

### **Exemplo Prático:**

```
Estou trabalhando no PersonalAgents, um orquestrador de vida pessoal com IA.

Já criei a documentação (11 docs) e 8 agents especializados.
Estou na fase de implementação do orquestrador Python.

Preciso criar o arquivo src/orchestrator/main.py que:
- Lê agents/*.md
- Chama Gemini API
- Gera agenda diária
- Salva no Supabase

Stack: Python 3.11, Gemini API, Supabase
Prazo: hoje (2-3h)

Me ajude a implementar este arquivo com código completo e comentado.
```

---

## 🎭 Convocar Agents Especializados

### **Como Funciona:**

Agents CLI podem "convocar" outros agents da metodologia ELabs-Agile:

```
Convoque o agent PM para me ajudar a criar o Product Brief.
```

```
Convoque Architect para revisar a arquitetura proposta.
```

```
Convoque CHALLENGER para questionar a viabilidade desta solução.
```

### **Agents Disponíveis:**

**Core Development:**
- PM, Analyst, Architect, SM, DEV, TEA, UX Designer, Technical Writer

**Meta-Agents:**
- CHALLENGER (crítico radical)

**Específicos do Projeto:**
- Coaching, Terapia, Relacionamentos, Finanças, Empresa

---

## 📝 Comandos e Workflows

### **Workflows ELabs-Agile:**

Você pode usar workflows da metodologia:

```
Execute o workflow *brainstorm-project
```

```
Execute o workflow *prd para criar o PRD inicial
```

```
Execute o workflow *architecture para a arquitetura técnica
```

**Lista completa:** `../../bmm/workflows/`

---

### **Comandos Úteis:**

```bash
# Listar arquivos do projeto
Mostre a estrutura de pastas do projeto

# Ler arquivo específico
Leia o arquivo src/orchestrator/main.py

# Criar/editar arquivo
Crie o arquivo src/agents/coaching.py com [código]

# Executar comando
Execute: git status

# Buscar no código
Busque por "def gerar_agenda" no projeto
```

---

## 🎯 Padrões de Interação

### **1. Planejamento (Início de Sessão)**

```
Olá! Estou iniciando sessão de trabalho.

Leia:
- agents/config.md
- CHECKPOINT-SESSAO-[último].md

Objetivo de hoje: [específico]

Me ajude a planejar a sessão:
1. O que preciso fazer?
2. Qual a ordem ideal?
3. Algum blocker potencial?
```

---

### **2. Implementação (Durante Desenvolvimento)**

```
Vamos implementar a feature X.

Requisitos:
- [req 1]
- [req 2]
- [req 3]

Stack: [tecnologia]

Crie o código completo com:
- Testes unitários
- Tratamento de erros
- Documentação inline
```

---

### **3. Troubleshooting (Quando travar)**

```
Estou com um erro/problema:
[descreva o problema]

Contexto:
- O que tentei: [X, Y, Z]
- Erro obtido: [copie o erro]
- Arquivo: [caminho]

Me ajude a debugar e resolver.
```

---

### **4. Revisão (Code Review)**

```
Revisei o código em [arquivo].

Por favor:
1. Analise se segue boas práticas
2. Identifique possíveis bugs
3. Sugira melhorias de performance
4. Verifique segurança (SQL injection, XSS, etc)

Use o agent TEA para análise de testes.
```

---

### **5. Documentação (Criar Docs)**

```
Preciso documentar [componente/feature].

Crie documentação estilo:
- README técnico
- Exemplos de uso
- API reference
- Troubleshooting comum

Target: desenvolvedores que vão usar isso.
```

---

### **6. Finalização (Fim de Sessão)**

```
Finalizando sessão de hoje.

O que fizemos:
- [item 1]
- [item 2]
- [item 3]

Crie um CHECKPOINT-SESSAO-[hoje].md com:
- Resumo do que foi feito
- Estado atual do projeto
- Próximos passos planejados
- Comandos executados
- Como retomar
```

---

## 🧠 Contexto e Memória

### **Memória de Sessão:**

O agent lembra de toda a conversa da sessão atual:

```
# Sessão começa
Você: "Vamos criar feature X"
Agent: [implementa]

# Mais tarde na mesma sessão
Você: "Agora adicione testes para isso"
Agent: [sabe que "isso" = feature X]
```

### **Sem Memória Entre Sessões:**

Nova sessão = contexto zero. Por isso:
1. Crie checkpoints ao final
2. Agent lê checkpoint ao retomar
3. Rebuild do contexto

---

## 💡 Boas Práticas

### **✅ FAÇA:**

1. **Seja específico:**
   - ❌ "Ajuda com o código"
   - ✅ "Implemente função X que faz Y com input Z"

2. **Dê contexto:**
   - Sempre mencione stack, constraints, objetivos
   - Referencie arquivos relevantes

3. **Peça para ler arquivos:**
   - Agent não adivinha o que ler
   - Seja explícito: "Leia agents/config.md"

4. **Use workflows:**
   - Aproveite os 34 workflows do BMM
   - Ex: `*prd`, `*architecture`, `*dev-story`

5. **Convoque agents especializados:**
   - PM para planejamento
   - Architect para arquitetura
   - CHALLENGER para questionar

6. **Crie checkpoints:**
   - Sempre ao final da sessão
   - Facilita retomada

---

### **❌ NÃO FAÇA:**

1. **Prompts vagos:**
   - "Me ajuda com isso" (isso o quê?)

2. **Assumir contexto:**
   - Nova sessão = novo contexto sempre

3. **Ignorar erros:**
   - Se agent erra, corrija e instrua melhor

4. **Esquecer de commitar:**
   - Agent pode gerar muito código - commite frequente

5. **Sessões infinitas:**
   - Timebox! (ex: 2h) depois pausa

---

## 🚨 Troubleshooting

### **Agent não entende contexto**

**Solução:**
1. Seja mais explícito
2. Peça para ler arquivos específicos
3. Dê exemplo concreto
4. Use analogia

---

### **Agent gera código errado**

**Solução:**
1. Corrija e explique o erro
2. Dê exemplo do código correto
3. Especifique constraints (ex: "use Python 3.11+")

---

### **Agent esqueceu algo**

**Memória intra-sessão:**
- Normal lembrar de toda conversa
- Se esqueceu, repita a info

**Entre sessões:**
- Normal esquecer tudo
- Use checkpoint para rebuild

---

### **Custo subindo muito**

**Claude caro:**
- Use Gemini como default
- Reserve Claude para tasks complexas específicas
- Limite sessões com Claude

**Gemini também caro:**
- Prompts mais curtos e objetivos
- Cache responses (futuro)
- Use free tier ($300 créditos)

---

## 📊 Métricas e Tracking

### **Acompanhe:**

- **Tokens usados** (custo)
- **Tempo de sessão**
- **Produtividade** (LOC, features, etc)
- **Qualidade** (bugs, code review)

### **Otimize:**

- Prompts mais eficientes
- Reutilize código gerado
- Documente soluções comuns

---

## 🎓 Exemplos Práticos

### **Exemplo 1: Criar Feature Completa**

```
Vamos criar feature de autenticação com Supabase.

Requisitos:
- Sign up com email/senha
- Login com Google OAuth
- JWT tokens
- RLS habilitado

Stack:
- Backend: Python FastAPI
- Database: Supabase

Estrutura:
1. Crie src/auth/auth.py com funções de auth
2. Crie tests/test_auth.py com testes
3. Documente em docs/api/auth.md

Me dê código completo + testes + docs.
```

---

### **Exemplo 2: Debug de Erro**

```
Erro ao executar orchestrator.py:

Error: supabase.exceptions.APIError: {"message":"JWT expired"}

Contexto:
- Arquivo: src/orchestrator/main.py linha 45
- Tentei: refresh token manualmente, não funcionou
- Supabase config: [copie config relevante]

Diagnostique e me dê solução step-by-step.
```

---

### **Exemplo 3: Code Review**

```
Convoque agent TEA para code review.

Arquivo: src/orchestrator/main.py

Verifique:
1. Tratamento de erros adequado?
2. Testes unitários cobrindo casos edge?
3. Performance (N+1 queries, etc)?
4. Segurança (injection, XSS)?
5. Code style (PEP8)?

Dê feedback estruturado com exemplos de melhoria.
```

---

## 🔄 Workflows Recomendados

### **Projeto Novo:**
1. `*brainstorm-project` → Ideação
2. `*product-brief` → Brief
3. `*prd` → Requisitos
4. `*architecture` → Arquitetura (Level 3-4)
5. `*sprint-planning` → Planejamento
6. `*dev-story` → Desenvolvimento

### **Projeto Existente:**
1. `*workflow-status` → Status atual
2. `*story-context` → Contexto de story
3. `*dev-story` → Desenvolvimento
4. `*code-review` → Revisão
5. `*story-done` → Conclusão

### **Projeto Brownfield:**
1. `*document-project` → Documentar existente
2. `*workflow-init` → Iniciar metodologia
3. Continuar normalmente

---

## 📞 Precisa de Ajuda?

**Comandos úteis no CLI:**

```
/help - Ajuda do CLI
/clear - Limpar sessão
/exit - Sair
```

**Consulte:**
- `../../bmm/docs/` - Documentação ELabs-Agile
- `../../bmm/docs/troubleshooting.md` - Troubleshooting

**Comunidade:**
- Discord BMad: https://discord.gg/gk8jAdXWmj

---

**Boa sessão!** 🤖

Lembre-se:
> "Agent é amplificador, você é o piloto"

---

**Última Atualização:** 2025-11-12
