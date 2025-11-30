# 📚 Marketing Frameworks & Models

## 🚀 AARRR (Pirate Metrics) - Growth Framework

Framework criado por Dave McClure para medir e otimizar growth.

```
A - ACQUISITION (Como chegam até você?)
├─ Canais: Organic, Paid, Referral, Direct, Social
├─ Métricas: Traffic, CAC, CPL
└─ Objetivo: Trazer visitantes qualificados

A - ACTIVATION (Primeira experiência é boa?)
├─ Momento "Aha!": Quando usuário vê valor
├─ Métricas: Signup rate, Onboarding completion
└─ Objetivo: Converter visitante em usuário ativo

R - RETENTION (Voltam?)
├─ Frequência: Diária, semanal, mensal
├─ Métricas: DAU/MAU, Churn rate, Cohort analysis
└─ Objetivo: Manter usuários engajados

R - REVENUE (Pagam?)
├─ Monetização: Subscription, Transaction, Ads
├─ Métricas: ARPU, LTV, Revenue growth
└─ Objetivo: Gerar receita sustentável

R - REFERRAL (Indicam?)
├─ Viralidade: Organic shares, Referral program
├─ Métricas: K-factor, NPS, Referral rate
└─ Objetivo: Crescimento viral/orgânico
```

### Como Aplicar:
1. **Mapeie seu funil** - Onde você está em cada A/R?
2. **Identifique gargalo** - Qual métrica está pior?
3. **Otimize sequencialmente** - Não adianta focar em Referral se Retention é ruim
4. **Regra 80/20** - 80% esforço no maior gargalo

---

## 🎯 RVCE para Marketing (Adaptado do CHALLENGER)

Framework de viabilidade aplicado a campanhas de marketing.

### REAL - O problema/oportunidade é real?
**Perguntas:**
- Esse público realmente tem esse pain point agora?
- Eles estão ativamente buscando solução? (Google Trends, fóruns, LinkedIn)
- Já tentaram resolver e falharam?
- Pain point é grande o suficiente para pagar?

**Red Flags:**
- ❌ "Achamos que eles vão gostar" (sem validação)
- ❌ Pain point é nice-to-have, não must-have
- ❌ Público não tem budget ou autoridade para comprar

**Como Validar:**
- Entrevistas com 5-10 prospects
- Análise de keywords (volume de busca)
- Análise de concorrentes (se existem, problema é real)

---

### VIÁVEL - Consegue executar essa campanha?
**Perguntas:**
- Tem equipe/skills necessárias?
- Tem conteúdo/criativos prontos ou rápidos de fazer?
- Tem budget suficiente para testar?
- Timeline é realista? (Campanha complexa em 1 semana = inviável)

**Red Flags:**
- ❌ Depende de muitas integrações complexas
- ❌ Precisa de aprovações de 5 pessoas
- ❌ Conteúdo precisa de 3 meses para produzir
- ❌ Budget é 10% do necessário para validar

**Como Garantir Viabilidade:**
- MVP de campanha: 2 canais, 1 audiência, 1 mensagem
- Use ferramentas que já domina (não aprenda nova tool mid-campaign)
- Timeline buffer: 2 semanas vira 3 (sempre atrasa)

---

### CUSTÁVEL - ROI é positivo?
**Perguntas:**
- Projeção de CAC vs LTV está saudável? (LTV > 3x CAC)
- Budget disponível vs objetivo é realista?
- Consegue medir ROI claramente?
- Consegue escalar se funcionar?

**Cálculos Essenciais:**
```
CAC (Customer Acquisition Cost):
= (Gasto Marketing + Vendas) / Novos Clientes

LTV (Lifetime Value):
= (Receita Mensal Média) × (Meses como Cliente)

ROI:
= (Receita - Custo) / Custo

Break-even:
= Quantos meses para LTV cobrir CAC?
```

**Red Flags:**
- ❌ CAC > LTV (nunca paga)
- ❌ Break-even > 12 meses (cashflow problem)
- ❌ Precisa escalar 100x para ser lucrativo
- ❌ Não tem tracking configurado (não vai saber ROI)

**Como Validar:**
- Projeção conservadora: Assume CTR/CR 50% da benchmark
- Se ainda assim ROI > 2x, vale testar
- Se ROI projetado < 1.5x, CHALLENGER aprova? Provavelmente não.

---

### EXECUTÁVEL - Consegue manter sozinho?
**Perguntas:**
- Campanha precisa de babá 24/7 ou roda sozinha?
- Tem automações configuradas? (Email sequences, lead scoring)
- Se você sair de férias 2 semanas, campanha continua rodando?
- Dá para outro da equipe assumir sem 40h de treinamento?

**Red Flags:**
- ❌ Precisa ajustar lances manualmente todo dia
- ❌ Email sequence é manual (não automatizada)
- ❌ Lead qualification é manual
- ❌ Reporte precisa de 8h/semana para compilar

**Como Tornar Executável:**
- Automatize nurturing (n8n, HubSpot, ActiveCampaign)
- Configure regras de lance automático (Google/LinkedIn)
- Dashboards auto-atualizáveis (Looker, Tableau, Google Data Studio)
- Documente processos (SOP - Standard Operating Procedure)

---

## 📊 Attribution Models (Quem leva crédito pela conversão?)

### 1. First Touch (Primeira Interação)
**Conceito:** 100% crédito para o primeiro canal que trouxe o lead
```
User Journey:
Google Search → Blog → Email → Webinar → Compra
        ↑
  100% crédito
```
**Quando usar:** Campanhas de awareness, top-of-funnel
**Limitação:** Ignora todo o nurturing que aconteceu depois

---

### 2. Last Touch (Última Interação)
**Conceito:** 100% crédito para o último canal antes da conversão
```
User Journey:
Google Search → Blog → Email → Webinar → Compra
                                           ↑
                                    100% crédito
```
**Quando usar:** Campanhas de conversão, bottom-of-funnel
**Limitação:** Ignora como o lead foi trazido inicialmente

---

### 3. Linear (Multi-Touch Igual)
**Conceito:** Crédito dividido igualmente entre todos os touchpoints
```
User Journey:
Google (25%) → Blog (25%) → Email (25%) → Webinar (25%) → Compra
```
**Quando usar:** Ver importância de cada etapa do funil
**Limitação:** Trata awareness igual a conversão (nem sempre justo)

---

### 4. Time Decay (Decaimento Temporal)
**Conceito:** Touchpoints mais próximos da conversão valem mais
```
User Journey:
Google (10%) → Blog (20%) → Email (30%) → Webinar (40%) → Compra
```
**Quando usar:** B2B com ciclo de venda longo
**Limitação:** Pode subestimar importância de awareness inicial

---

### 5. Position-Based (U-Shaped)
**Conceito:** 40% para primeiro, 40% para último, 20% dividido no meio
```
User Journey:
Google (40%) → Blog (10%) → Email (10%) → Webinar (40%) → Compra
```
**Quando usar:** Balancear importância de acquisition e conversion
**Mais usado:** Modelo favorito para B2B SaaS

---

## 🧪 Experimentation Framework

### Processo de A/B Testing

**1. HIPÓTESE**
```
Template:
"Acreditamos que [MUDANÇA] vai resultar em [IMPACTO] porque [RAZÃO]"

Exemplo:
"Acreditamos que mudar CTA de 'Saiba mais' para 'Teste grátis 14 dias'
vai aumentar conversão em 25% porque remove fricção e deixa oferta clara"
```

**2. DEFINIR MÉTRICAS**
- Métrica primária: O que você quer melhorar? (ex: Conversion rate)
- Métricas secundárias: O que pode ser afetado? (ex: Bounce rate, Time on page)
- Métrica guardrail: O que NÃO pode piorar? (ex: Qualidade de leads)

**3. TAMANHO DA AMOSTRA**
```
Use calculadora: https://www.optimizely.com/sample-size-calculator/

Exemplo:
- Baseline CR: 2%
- Melhoria esperada: +25% (2% → 2.5%)
- Confiança: 95%
- Poder estatístico: 80%
→ Precisa de ~15,000 visitantes por variante
```

**4. EXECUTAR TESTE**
- Split 50/50 (metade vê A, metade vê B)
- Não mexe durante o teste (pode invalidar)
- Roda até atingir tamanho da amostra ou 2-4 semanas

**5. ANALISAR RESULTADOS**
```
Variante A (Control): 2.0% CR (150 conversões / 7,500 visitantes)
Variante B (Test): 2.6% CR (195 conversões / 7,500 visitantes)
Uplift: +30%
P-value: 0.03 (< 0.05 = estatisticamente significativo)
Winner: B ✅
```

**6. IMPLEMENTAR & DOCUMENTAR**
- Implementa winner em 100% tráfego
- Documenta learning em `memories.md`
- Próximo teste: Iterar em cima do winner

---

## 💰 Pricing & Monetization Frameworks

### Value-Based Pricing
**Conceito:** Preço baseado no valor entregue, não no custo

**Fórmula:**
```
Valor Percebido pelo Cliente = Benefício Quantificável
Preço = % do Valor (geralmente 10-30%)

Exemplo:
Software reduz CAC de cliente em $50k/ano
→ Valor percebido: $50k
→ Preço justo: $5k-15k/ano (10-30% do valor)
```

**Como Descobrir Valor:**
1. Entrevistas: "Quanto vale para você resolver X?"
2. Competição: "Quanto pagam em alternativas?"
3. Teste: Varia preço e mede elasticidade

---

### Freemium Model
**Conceito:** Versão grátis + versão paga com mais features

**Quando Funciona:**
- Produto tem network effects (mais usuários = mais valor)
- Custo marginal baixo (servir usuário grátis custa pouco)
- Upsell clear (free → paid é óbvio)

**Métricas Chave:**
- Free → Paid conversion: 2-5% (benchmark)
- Time to convert: Quanto tempo leva?
- LTV de paid users tem que cobrir CAC de todos (free + paid)

**Gatilhos de Upgrade:**
```
Feature gating: Free tem X, Paid tem X+Y+Z
Usage limits: Free = 10 projetos, Paid = ilimitado
Support: Free = email, Paid = chat + phone
Time: Free = 14 dias trial, depois paga
```

---

### SaaS Pricing Tiers
**Padrão: Good - Better - Best**

```
BASIC ($X/mês):
├─ Usuário individual/pequena empresa
├─ Features essenciais
└─ Self-service support

PROFESSIONAL ($3-5X/mês): ← Mais vendido (sweet spot)
├─ Pequenas e médias empresas
├─ Features avançadas + integrações
└─ Priority support

ENTERPRISE ($10X+/mês):
├─ Grandes empresas
├─ Tudo do Pro + Custom + Dedicação
└─ Dedicated account manager
```

**Psicologia:**
- Tier do meio vende mais (anchor effect)
- Enterprise é "você precisa falar com vendas" (custom pricing)
- Diferença entre tiers: 3-5x (não 2x ou 10x)

---

## 🎨 Messaging Frameworks

### Jobs To Be Done (JTBD)
**Conceito:** Pessoas "contratam" produtos para fazer um "job"

**Template:**
```
Quando eu [SITUAÇÃO]
Eu quero [MOTIVAÇÃO]
Para que eu possa [RESULTADO DESEJADO]

Exemplo:
Quando eu lanço campanha nova no LinkedIn
Eu quero saber se está performando bem
Para que eu possa otimizar antes de desperdiçar budget
```

**Como Usar no Marketing:**
- Identifique o "job" que seu produto faz
- Mensagem foca no job, não em features
- "Nós ajudamos você a [JOB]" vs "Nós temos [FEATURE]"

---

### PAS Framework (Problem-Agitate-Solution)
**Estrutura de Copy que Converte:**

```
1. PROBLEM (Problema)
"Seu CAC está muito alto e você não sabe por quê?"

2. AGITATE (Agrava/Empatiza)
"Todo mês você investe $10k em ads, mas leads não convertem.
Seu CEO pressiona por ROI, mas você não tem visibilidade do que funciona.
Você testa criativos, audiências, copy... mas continua no escuro."

3. SOLUTION (Solução)
"Com [PRODUTO], você tem dashboard em tempo real que mostra exatamente
qual canal, criativo e audiência está gerando leads que convertem.
Pare de desperdiçar budget - otimize baseado em dados."
```

**Onde Usar:**
- Landing pages
- Email sequences
- Ad copy
- Sales presentations

---

### AIDA Framework (Awareness-Interest-Desire-Action)
**Estrutura Clássica para Conversão:**

```
A - AWARENESS (Atenção)
↓ Headline forte, visual impactante
I - INTEREST (Interesse)
↓ Subheadline que detalha benefício
D - DESIRE (Desejo)
↓ Bullets, social proof, escassez
A - ACTION (Ação)
↓ CTA claro e urgente
```

**Exemplo Landing Page:**
```
[AWARENESS]
Headline: "Reduza Seu CAC em 40% em 30 Dias"

[INTEREST]
Subheadline: "CMOs como você estão usando nossa plataforma para
otimizar campanhas em tempo real e gerar 2x mais MQLs"

[DESIRE]
✅ Dashboard de atribuição em tempo real
✅ A/B testing automatizado
✅ Integração com Google Ads, LinkedIn, HubSpot
🏆 "Reduzimos CAC de $800 para $350 em 60 dias" - João, CMO SaaS XYZ

[ACTION]
🎯 [TESTE GRÁTIS 14 DIAS - SEM CARTÃO] 🎯
```

---

## 📈 Growth Loops (Viral & Referral)

### Conceito
Loop de crescimento onde output de um ciclo alimenta input do próximo.

### Exemplo: Referral Loop
```
1. User tem boa experiência →
2. Compartilha com amigo →
3. Amigo se cadastra (incentivo) →
4. User ganha benefício →
5. Repete ciclo
```

**K-Factor:**
```
K = (Convites por usuário) × (% que convertem)

Se K > 1: Crescimento viral (cada user traz mais de 1)
Se K < 1: Crescimento orgânico (não é viral, mas ajuda)

Exemplo:
- Cada user convida 5 amigos
- 30% dos convidados se cadastram
- K = 5 × 0.30 = 1.5 (Viral! 🚀)
```

### Tipos de Growth Loops
1. **Viral Loop** - Compartilhamento inerente ao uso (ex: Zoom - para call, convida outros)
2. **Referral Loop** - Incentivo para indicar (ex: Dropbox - ganha storage)
3. **Content Loop** - UGC atrai novos (ex: Pinterest - pins atraem visitantes)
4. **Paid Loop** - CAC < LTV, reinveste lucro em ads (ex: E-commerce)

---

## 🛠️ Channel Selection Framework

### Como Escolher Canais Certos?

**1. Onde seu ICP está?**
```
B2B Decision Makers:
✅ LinkedIn (alto, mas qualidade)
✅ Google Search (alta intenção)
✅ Email (se tem lista)
✅ Webinars, Podcasts B2B
❌ TikTok, Instagram (baixa presença B2B)

B2C Millennials/Gen Z:
✅ Instagram, TikTok
✅ YouTube
✅ Influencer marketing
❌ LinkedIn (custo alto, baixo engagement)
```

**2. Budget Disponível?**
```
< $1k/mês:
→ SEO, Content marketing, Email (baixo custo)

$1k-10k/mês:
→ Google Search ads, LinkedIn (teste), Email automation

$10k-50k/mês:
→ Multi-canal (Google, LinkedIn, Programmatic, Retargeting)

$50k+/mês:
→ Tudo + Influencers, Events, Brand campaigns
```

**3. Ciclo de Venda?**
```
Curto (< 1 semana):
→ Google Search (alta intenção), Retargeting, Email

Médio (1-4 semanas):
→ Google + LinkedIn + Nurturing sequences

Longo (3+ meses):
→ Content marketing, Webinars, Multi-touch nurturing
```

**4. Teste Small, Scale What Works**
```
Semana 1-2: Teste 3 canais com $500-1000 cada
Semana 3-4: Identifica winner (melhor ROI)
Mês 2: Joga 70% budget no winner, 30% em teste de novo canal
```

---

## 🎓 Continuous Learning Resources

### Must-Read Books
- **Traction** - Gabriel Weinberg (19 canais de acquisition)
- **Lean Analytics** - Alistair Croll (métricas que importam)
- **Hacking Growth** - Sean Ellis (growth hacking frameworks)
- **Obviously Awesome** - April Dunford (positioning)

### Tools to Master
- **Google Analytics 4** - Web analytics
- **HubSpot Academy** - Inbound marketing (free courses)
- **Reforge** - Advanced growth courses (paid, caro mas bom)
- **CXL** - Conversion optimization courses

### Communities
- **Growth Hackers** - Forum de growth marketing
- **Reforge Network** - Community de growth practitioners
- **LinkedIn Groups** - Growth Marketing, SaaS Marketing

---

**Última atualização:** 2025-11-26
**Mantido por:** Luna (Marketing Agent)
