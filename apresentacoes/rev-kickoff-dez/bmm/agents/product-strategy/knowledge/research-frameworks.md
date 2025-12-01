# 📚 Research Frameworks & Methodologies

## 🎯 TAM/SAM/SOM Framework

### O que é?
Framework para sizing de mercado em 3 níveis: Total, Serviceable, e Obtainable.

### Definições

**TAM (Total Addressable Market)**
- **O que é:** Toda a receita possível se você capturasse 100% do mercado
- **Pergunta:** "Se todo mundo que pudesse usar nosso produto usasse, quanto seria?"
- **Exemplo:** 500k restaurantes nos EUA × $100/mês × 12 meses = $600M TAM

**SAM (Serviceable Available Market)**
- **O que é:** Parte do TAM que você consegue alcançar (geograficamente, segmento, etc)
- **Pergunta:** "Qual parte do TAM nós realísticamente conseguimos servir?"
- **Exemplo:** 100k restaurantes pequenos/médios (não enterprise, não food trucks) = $120M SAM

**SOM (Serviceable Obtainable Market)**
- **O que é:** Parte do SAM que você pode capturar nos próximos 1-3 anos
- **Pergunta:** "Qual market share realista conseguimos em 3 anos?"
- **Exemplo:** 0.5% market share = 500 clientes × $100/mês × 12 = $600k SOM

---

### Como Calcular

**Método 1: Top-Down (Começa com total de mercado)**
```
TAM = (# Total de Players no Mercado) × (ARPU anual)

Exemplo - SaaS para Restaurantes:
- Total restaurantes Brasil: 500k
- ARPU: $80/mês = $960/ano
- TAM = 500k × $960 = $480M

SAM = TAM × (% que você alcança)
- Target: Restaurantes pequenos/médios = 50%
- SAM = $480M × 50% = $240M

SOM = SAM × (Market Share realista em 3 anos)
- Market share: 0.5-2% é realista para startup
- SOM = $240M × 1% = $2.4M
```

**Método 2: Bottom-Up (Começa com clientes atuais/pipeline)**
```
SOM = (# Clientes que você pode adquirir) × (ARPU anual)

Exemplo:
Ano 1:
- Meta: 50 clientes
- ARPU: $960/ano
- SOM Ano 1 = 50 × $960 = $48k

Ano 2:
- Meta: 200 clientes (4x growth)
- SOM Ano 2 = 200 × $960 = $192k

Ano 3:
- Meta: 500 clientes (2.5x growth)
- SOM Ano 3 = 500 × $960 = $480k
```

**Método 3: Value Theory (Baseado em valor substituído)**
```
TAM = (Valor que seu produto substitui) × (# Players)

Exemplo - Ferramenta de automação:
- Economiza 10h/mês por cliente
- Valor hora: $50
- Valor substituído: 10h × $50 = $500/mês
- Players: 100k empresas
- TAM = $500 × 100k × 12 = $600M
```

---

### Benchmarks de Viabilidade

**TAM Mínimo:**
- Micro SaaS: $10M+ TAM (30k+ players)
- SaaS Startup: $1B+ TAM (VC-backable)
- Enterprise: $5B+ TAM (large market)

**SOM Realista (Ano 3):**
- Bootstrap: $500k-2M (suficiente para 1-5 pessoas)
- Venture-backed: $5M-20M (Series A viável)
- Unicorn path: $50M+ (Series B+)

**Red Flags:**
- ❌ TAM < $10M (muito pequeno)
- ❌ SAM < 20% TAM (hard to reach)
- ❌ SOM < $200k Ano 3 (não sustenta negócio)

---

## 🧭 Jobs To Be Done (JTBD) Framework

### O que é?
Framework para entender o "job" que cliente "contrata" seu produto para fazer.

### Conceito Core
**"People don't want to buy a quarter-inch drill. They want a quarter-inch hole."**
- Foco no resultado (hole), não no produto (drill)
- Produto é contratado para fazer um "job"

---

### Template JTBD

```
Quando eu [SITUAÇÃO]
Eu quero [MOTIVAÇÃO]
Para que eu possa [RESULTADO DESEJADO]
```

**Exemplo 1 - Restaurante:**
```
Quando eu recebo pedidos de múltiplas plataformas simultaneamente
Eu quero consolidar tudo em um único lugar
Para que eu possa evitar erros e economizar 2h/dia
```

**Exemplo 2 - Freelancer:**
```
Quando eu termino um projeto para cliente
Eu quero enviar invoice profissional e rastrear pagamento
Para que eu possa ser pago rapidamente sem trabalho manual
```

**Exemplo 3 - Gerente de Marketing:**
```
Quando eu preciso reportar ROI de campanhas para CEO
Eu quero dashboard que mostra atribuição multi-canal
Para que eu possa provar valor do marketing e conseguir mais budget
```

---

### Como Descobrir Jobs

**1. Entrevistas (Perguntas Certas):**
```
❌ Ruim: "Que features você quer?"
✅ Bom: "Me conte sobre a última vez que você [fez tarefa X]"

❌ Ruim: "Você gostaria de [feature Y]?"
✅ Bom: "Como você resolve [problema] hoje? Por quê?"

❌ Ruim: "O que você acha desta solução?"
✅ Bom: "Qual seria o resultado ideal? Como você saberia que funcionou?"
```

**2. Observação:**
- Observe pessoas fazendo o job atual
- Onde gastam tempo? Onde se frustram?
- Workarounds que criaram?

**3. Reviews de Concorrentes:**
- "Eu uso X para fazer Y"
- "Mudei de A para B porque precisava de Z"
- Job = Y (o que fazem), não feature = Z

---

### Jobs vs Features

**Features** = O que o produto TEM
**Jobs** = O que o produto FAZ para o usuário

| Feature (O quê) | Job (Por quê) |
|-----------------|---------------|
| Dashboard unificado | "Evitar alternar entre 5 apps" |
| Notificações push | "Não perder pedidos urgentes" |
| Relatórios analytics | "Provar ROI para stakeholders" |
| Integrações API | "Usar dados em ferramentas que já tenho" |

**Marketing JTBD:**
- ❌ Ruim: "Temos dashboard unificado!"
- ✅ Bom: "Pare de perder 2h/dia alternando entre apps"

---

### Jobs Hierarquia

**Functional Job** (Prático)
- "Consolidar pedidos de delivery"
- "Enviar invoices automaticamente"

**Emotional Job** (Sentimento)
- "Me sentir no controle"
- "Não ter medo de perder pedidos"
- "Parecer profissional para clientes"

**Social Job** (Status)
- "Demonstrar eficiência para chefe"
- "Ser visto como tech-savvy"

**Melhor produto:** Resolve functional + emotional + social

---

## 🌊 Blue Ocean Strategy

### O que é?
Framework para criar espaços de mercado não disputados (blue ocean) ao invés de competir em mercados saturados (red ocean).

### Red Ocean vs Blue Ocean

**Red Ocean (Mercado Saturado):**
- Competição intensa
- Guerra de preço
- Features iguais aos concorrentes
- Crescimento lento
- Exemplo: CRM genérico (Salesforce, HubSpot, Pipedrive, + 100 outros)

**Blue Ocean (Espaço Novo):**
- Pouca ou nenhuma competição
- Preço baseado em valor
- Diferenciação clara
- Crescimento rápido (early adopters)
- Exemplo: Notion (não é docs, não é PM, é novo)

---

### Four Actions Framework

**ELIMINATE** - O que a indústria aceita como dado mas você pode eliminar?
```
Exemplo - Basecamp:
ELIMINA: Features complexas (Gantt charts, time tracking detalhado)
Razão: SMBs não precisam, só confunde
```

**REDUCE** - O que pode reduzir bem abaixo do padrão?
```
Exemplo - Zoom:
REDUZ: Setup complexity (rival: Cisco Webex = configuração complexa)
Razão: "1-click to join" > instalar software, configurar
```

**RAISE** - O que pode aumentar bem acima do padrão?
```
Exemplo - Tesla:
AUMENTA: Software updates (OTA - over the air)
Razão: Carros tradicionais não fazem, Tesla adiciona features remotamente
```

**CREATE** - O que pode criar que a indústria nunca ofereceu?
```
Exemplo - Airbnb:
CRIA: "Live like a local" experience
Razão: Hotéis oferecem quarto, Airbnb oferece experiência + comunidade
```

---

### Como Aplicar em Micro SaaS

**Passo 1: Mapeie a Indústria (Concorrentes)**
```
O que TODO concorrente faz?
- Feature A (todos têm)
- Feature B (todos têm)
- Pricing alto (todos cobram $X)
- Suporte ruim (todos demoram 24h)
```

**Passo 2: Aplique 4 Actions**
```
ELIMINATE:
- Feature C (ninguém usa, só complica)

REDUCE:
- Features avançadas (80% users não usam)

RAISE:
- Suporte (responde em 1h, não 24h)
- UX (10x mais simples)

CREATE:
- Integração única (que ninguém tem)
- Community / network effects
```

**Passo 3: Posicionamento Blue Ocean**
```
"Ao invés de [CATEGORIA TRADICIONAL]
Nós somos [NOVA CATEGORIA]
Que [BENEFÍCIO ÚNICO]"

Exemplo:
"Ao invés de CRM complexo para todos
Nós somos CRM visual para freelancers criativos
Que gerencia projetos + clientes em um kanban simples"
```

---

## ⚔️ Porter's Five Forces

### O que é?
Framework para avaliar atratividade competitiva de um mercado.

### As 5 Forças

**1. Rivalry (Intensidade da Competição Atual)**
```
❌ Alta Rivalidade (Ruim):
- 10+ concorrentes fortes
- Guerra de preço
- Produtos commoditizados
- Crescimento lento de mercado

✅ Baixa Rivalidade (Bom):
- 0-5 concorrentes
- Diferenciação clara
- Mercado crescendo
- Pricing baseado em valor
```

**2. Threat of New Entrants (Barreira de Entrada)**
```
❌ Baixa Barreira (Ruim):
- Fácil de copiar
- Sem network effects
- Capital necessário baixo
- Sem regulação

✅ Alta Barreira (Bom):
- Tech complexa / IP
- Network effects (mais users = mais valor)
- Switching costs altos
- Regulação difícil
```

**3. Threat of Substitutes (Alternativas)**
```
❌ Muitos Substitutos (Ruim):
- Soluções gratuitas viáveis (Excel, Google Sheets)
- Manual é aceitável
- Múltiplas categorias resolvem mesmo job

✅ Poucos Substitutos (Bom):
- Seu produto é única solução viável
- Manual é inviável (muito tempo)
- Alternativas são muito piores
```

**4. Buyer Power (Poder de Barganha dos Clientes)**
```
❌ Alto Buyer Power (Ruim):
- Clientes grandes, concentrados
- Fácil de trocar de vendor
- Produto não é crítico
- Baixo switching cost

✅ Baixo Buyer Power (Bom):
- Muitos clientes pequenos (fragmentado)
- Alto switching cost
- Produto é crítico (não podem viver sem)
```

**5. Supplier Power (Poder de Fornecedores)**
```
❌ Alto Supplier Power (Ruim):
- Depende de 1 fornecedor crítico
- Poucos fornecedores alternativos
- Alto custo de trocar

✅ Baixo Supplier Power (Bom):
- Múltiplos fornecedores
- Commoditizado (cloud, APIs)
- Fácil de trocar
```

---

### Scoring de Atratividade

```
Força | Score (1-5) | Nota
------|-------------|------
Rivalry | [X] | 5=baixa, 1=alta
New Entrants | [X] | 5=difícil entrar, 1=fácil
Substitutes | [X] | 5=poucos, 1=muitos
Buyer Power | [X] | 5=fragmentado, 1=concentrado
Supplier Power | [X] | 5=muitos, 1=poucos
**TOTAL** | **[Y]/25** |

Interpretação:
- 20-25: 🟢 Mercado MUITO atrativo
- 15-19: 🟡 Mercado OK
- 0-14: 🔴 Mercado difícil (avoid)
```

---

## 📊 Van Westendorp Price Sensitivity Meter

### O que é?
Método para descobrir range de preço aceitável através de 4 perguntas.

### As 4 Perguntas

```
1. A que preço você consideraria o produto MUITO CARO?
   (Ainda compraria, mas muito caro)

2. A que preço você consideraria o produto CARO?
   (Compraria, mas começa a doer)

3. A que preço você consideraria o produto BARATO?
   (Bom preço, suspeitaria de qualidade?)

4. A que preço você consideraria o produto MUITO BARATO?
   (Barato demais, não confiaria)
```

### Como Aplicar

**1. Survey 50-100 pessoas do ICP**
```
Pergunte as 4 questões
Coleta respostas em planilha

Exemplo:
Pessoa | Muito Caro | Caro | Barato | Muito Barato
-------|------------|------|--------|-------------
1      | $150       | $100 | $40    | $20
2      | $200       | $120 | $50    | $25
...    | ...        | ...  | ...    | ...
```

**2. Plote em gráfico**
```
Eixo X = Preço ($0 - $200)
Eixo Y = % de respondentes

4 linhas:
- "Muito caro" (cumulativa crescente)
- "Caro" (cumulativa crescente)
- "Barato" (cumulativa decrescente)
- "Muito barato" (cumulativa decrescente)
```

**3. Identifique pontos de interseção**
```
OPP (Optimal Price Point):
- Interseção "Caro" × "Barato"
- Sweet spot: Máximo de pessoas acha justo

IPP (Indifference Price Point):
- Interseção "Muito caro" × "Muito barato"
- Preço onde igual # acha muito caro ou muito barato

Range Aceitável:
- Entre interseções de "Muito barato" com "Caro"
  e "Barato" com "Muito caro"
```

**4. Decisão de Pricing**
```
Estratégia Penetração (Ganhar market share):
→ Preço abaixo OPP (closer to "Barato")

Estratégia Premium (Maximizar margem):
→ Preço acima OPP (closer to "Caro")

Estratégia Balanced:
→ Preço = OPP
```

---

## 🎯 Sean Ellis PMF Test

### O que é?
Teste simples para validar se você tem Product-Market Fit.

### A Pergunta

```
"Como você se sentiria se não pudesse mais usar [PRODUTO]?"

a) Muito decepcionado
b) Um pouco decepcionado
c) Não decepcionado (não faz diferença)
d) N/A - Já não uso mais o produto
```

### Interpretação

```
PMF Score = % que responde "Muito decepcionado"

Benchmark:
- > 40%: ✅ Você TEM Product-Market Fit
- 25-40%: 🟡 Perto, mas ainda não
- < 25%: ❌ Longe de PMF
```

### Como Aplicar

**1. Quando aplicar:**
- Após 30-60 dias de uso (deu tempo de adotar)
- Mínimo 50 respondentes (dados suficientes)
- Usuários ativos (não apenas signups)

**2. Como survey:**
```
Email curto:
---
Subject: Pergunta rápida (30 segundos)

Oi [Nome],

Quero melhorar [PRODUTO] e preciso da sua ajuda.

Uma pergunta rápida:

Como você se sentiria se não pudesse mais usar [PRODUTO]?
a) Muito decepcionado
b) Um pouco decepcionado
c) Não decepcionado
d) N/A - Já não uso mais

[LINK PARA SURVEY]

Obrigado!
---
```

**3. Follow-up (se < 40%):**
```
Para quem respondeu "Um pouco" ou "Não decepcionado":

"O que precisaríamos mudar para você ficar MUITO decepcionado
se não pudesse mais usar?"

→ Identifica gaps de features/valor
```

**4. Segmentação:**
```
Analise por segmento:
- ICP correto: 60% "muito decepcionado" ✅
- ICP errado: 10% "muito decepcionado" ❌

Conclusão: Pivot para ICP correto
```

---

## 📈 Cohort Analysis para Retention

### O que é?
Análise de retenção por cohort (grupo de usuários que entraram no mesmo período).

### Como Construir

**1. Defina Cohorts:**
```
Cohort = Mês de signup

Exemplo:
- Cohort Jan 2025: Todos que fizeram signup em Jan
- Cohort Fev 2025: Todos que fizeram signup em Fev
- Etc.
```

**2. Tabela de Retention:**
```
Cohort  | M0   | M1   | M2   | M3   | M4   | M5   | M6
--------|------|------|------|------|------|------|------
Jan 25  | 100% | 85%  | 80%  | 78%  | 75%  | 73%  | 72%
Fev 25  | 100% | 88%  | 82%  | 79%  | 76%  | 74%  | --
Mar 25  | 100% | 90%  | 85%  | 81%  | 78%  | --   | --
Abr 25  | 100% | 92%  | 87%  | 83%  | --   | --   | --

M0 = Mês de signup (100% por definição)
M1 = % que voltou no mês seguinte
M2 = % que voltou 2 meses depois
...
```

**3. Análise:**
```
✅ Boa Retenção (SaaS B2B):
- M1: > 80%
- M3: > 75%
- M6: > 70%
- Curva achata (não continua caindo muito)

❌ Ruim:
- M1: < 70%
- M3: < 50%
- M6: < 30%
- Curva continua caindo (não achata)
```

**4. Insights:**
```
Cohort melhorando ao longo tempo?
→ Produto está ficando melhor (onboarding, features)

Cohort piorando?
→ Competição aumentou, produto piorou, ou ICP mudou

M1 retention baixo?
→ Onboarding ruim, "aha moment" não aconteceu

M1 alto mas M3-M6 baixo?
→ Produto não tem valor contínuo (one-time use)
```

---

**Última atualização:** 2025-11-26
**Mantido por:** Nina (Product Strategy Agent)

*"Good research frameworks turn intuition into evidence and guesses into confidence."*
