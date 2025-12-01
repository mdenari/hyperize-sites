# 🎯 Campaign Playbooks - Ready-to-Use Templates

## LinkedIn B2B Lead Generation Campaign

### Objetivo
Gerar MQLs qualificados para produto B2B SaaS via LinkedIn Ads

### Quando Usar
- ICP são decision makers (CMO, VP, Director level)
- Ticket médio > $5k/ano
- Ciclo de venda 30-90 dias
- Budget mínimo: $2k/mês

---

### Setup (Pre-Campaign)

**1. ICP & Targeting**
```yaml
Empresa:
  - Indústria: [SaaS, Tech, Finance, etc]
  - Tamanho: 50-500 funcionários
  - Receita: $5M-50M

Decision Maker:
  - Cargo: CMO, VP Marketing, Head of Growth
  - Seniority: Director+
  - Skills: Marketing Analytics, Growth Hacking, SaaS
  - Grupos: Reforge, SaaStr, Marketing communities
```

**2. Campanha Structure**
```
Campaign 1: Cold Awareness
├─ Ad Set: CMOs SaaS 50-200 emp
├─ Ad Set: VPs Marketing Tech 200-500 emp
└─ Budget: 40% do total

Campaign 2: Retargeting Warm
├─ Ad Set: Visitou site nos últimos 30 dias
├─ Ad Set: Engajou com post/ad
└─ Budget: 30% do total

Campaign 3: Lead Magnet
├─ Ad Set: Same targeting Campaign 1
├─ Oferta: Ebook, Webinar, Calculator
└─ Budget: 30% do total
```

**3. Creative Strategy**
```
Teste 3 formatos:
1. Carousel (Dados/Estatísticas)
   - "5 Maneiras de Reduzir CAC"
   - Cada card = 1 dica visual

2. Single Image (Social Proof)
   - Cliente quote + logo
   - "Como empresa X reduziu CAC 40%"

3. Video (15-30s)
   - Problema → Solução → CTA
   - Legendado (90% assistem muted)
```

**4. Messaging per Stage**
```
COLD (Awareness):
Headline: "Seu CAC está muito alto?"
Body: "CMOs como você estão reduzindo em 40% com [solução].
       Veja como →"
CTA: "Saiba como"

WARM (Consideration):
Headline: "Viu nosso artigo sobre CAC? Temos mais..."
Body: "Baixe o guia completo: 10 táticas para reduzir CAC
       baseado em 50+ empresas SaaS"
CTA: "Baixar guia grátis"

HOT (Decision):
Headline: "Pronto para reduzir seu CAC?"
Body: "Agende demo de 15min e veja como funciona na prática"
CTA: "Agendar demo"
```

---

### Execution (During Campaign)

**Week 1: Launch & Monitor**
- [ ] Campanhas live com budget baixo ($20-30/dia)
- [ ] Monitor diário: CTR, CPC, CPL
- [ ] Pause ad sets com CTR < 0.4% após 48h
- [ ] Escale vencedores em 20% budget

**Week 2-3: Optimize**
- [ ] A/B test criativos vencedores (headline, visual, CTA)
- [ ] Expanda audiências similares (Lookalike)
- [ ] Ajusta lances baseado em CPL target
- [ ] Setup retargeting para quem engajou

**Week 4: Scale**
- [ ] Joga 70% budget nos winners
- [ ] Mantém 30% para testes contínuos
- [ ] Expande para novos ad sets (job titles, empresas)

---

### KPIs & Benchmarks

```yaml
Performance Targets:
  CTR (Click-Through Rate): 0.5-1% (cold), 2-4% (retargeting)
  CPL (Cost Per Lead): $80-150
  Landing Page CR: 15-30%
  Lead → MQL: 40-50%
  CAC Target: < $300

Red Flags:
  CTR < 0.3%: Mensagem não ressoa, troca criativo
  CPL > $200: Audiência errada ou oferta fraca
  LP CR < 10%: Landing page ruim, otimiza
```

---

### Nurturing Sequence (Post-Lead)

**Email Sequence (10 dias):**
```
Day 0: Entrega do lead magnet
Subject: "Seu [Ebook/Guia] está aqui 🎉"
Body: PDF attached + dica #1

Day 2: Valor adicional
Subject: "Dica #2: Como empresa X fez isso"
Body: Case study + link para blog post

Day 5: Educação
Subject: "3 erros que estão aumentando seu CAC"
Body: Artigo + stats

Day 7: Soft Pitch
Subject: "Quer ver como funciona na prática?"
Body: Convite para webinar/demo

Day 10: Direct Offer
Subject: "Teste grátis por 14 dias (sem cartão)"
Body: CTA para trial
```

---

### Post-Campaign Analysis Template

```markdown
## LinkedIn Campaign - [Nome] - Analysis

**Período:** [Data início] - [Data fim]
**Budget:** $X,XXX
**Objetivo:** XX MQLs

### Performance Overall
- Impressions: XXX,XXX
- Clicks: X,XXX (CTR X%)
- Leads: XXX (CPL $XX)
- MQLs: XX (Lead→MQL XX%)
- CAC: $XXX
- ROI: Xx

### Performance por Ad Set
| Ad Set | Budget | Leads | CPL | MQLs | Winner? |
|--------|--------|-------|-----|------|---------|
| CMOs SaaS 50-200 | $XXX | XX | $XX | XX | ✅ |
| VPs Marketing Tech | $XXX | XX | $XX | XX | ❌ |

### Performance por Creative
| Creative | Impressions | CTR | CPL | Winner? |
|----------|-------------|-----|-----|---------|
| Carousel Stats | XX,XXX | X% | $XX | ✅ |
| Single Image Quote | XX,XXX | X% | $XX | ❌ |

### What Worked
- [Ex: Carousel com estatísticas teve CTR 2x maior]
- [Ex: Audiência "CMOs SaaS" converteu muito melhor]

### What Didn't Work
- [Ex: Ad set de VPs teve CPL 50% maior]
- [Ex: Video teve CTR baixo (talvez audience prefere texto)]

### Learnings
- [Ex: Mensagem focada em dados/ROI ressoa mais que features]
- [Ex: Job title "CMO" > "Marketing Director" para targeting]

### Next Steps
- [ ] Scale campaign 1 (CMOs SaaS) com +50% budget
- [ ] Testar novo criativo (video com legendas)
- [ ] Expandir para Google Search Ads com mesma mensagem
```

---

## Google Search Ads Campaign (High-Intent)

### Objetivo
Capturar leads com alta intenção de compra via Google Search

### Quando Usar
- Pessoas estão ativamente buscando solução
- Palavras-chave têm volume suficiente (>500/mês)
- Budget mínimo: $1k/mês

---

### Keyword Research

**1. Seed Keywords (Core)**
```
Categoria: Problema
- "como reduzir CAC"
- "ferramentas marketing analytics"
- "melhorar conversão landing page"

Categoria: Solução
- "marketing automation software"
- "lead scoring tool"
- "attribution software B2B"

Categoria: Comparação
- "[Concorrente] alternative"
- "[Concorrente] vs [Você]"
- "best [categoria] for B2B"

Categoria: Branded
- "[Sua marca]"
- "[Sua marca] review"
- "[Sua marca] pricing"
```

**2. Match Types**
```
Exact Match: [como reduzir CAC]
→ Alta intenção, baixo volume

Phrase Match: "marketing automation software"
→ Médio equilíbrio

Broad Match: +marketing +automation
→ Alto volume, mas menos qualificado
```

**Estratégia:**
- 70% budget em Exact/Phrase (alta intenção)
- 30% em Broad (discovery de novas keywords)

---

### Campaign Structure

```
Campaign 1: Branded (Defesa)
├─ Ad Group: Brand terms
├─ Keywords: [sua marca], [sua marca] + pricing/review/login
├─ Budget: 10-15%
└─ Goal: Capture quem já conhece (CR alta, CPC baixo)

Campaign 2: Problem/Pain Point
├─ Ad Group 1: CAC reduction
├─ Ad Group 2: Lead generation
├─ Budget: 40%
└─ Goal: Top-of-funnel, educação

Campaign 3: Solution
├─ Ad Group 1: Marketing automation
├─ Ad Group 2: Lead scoring
├─ Budget: 35%
└─ Goal: Meio-de-funil, comparação

Campaign 4: Competitor
├─ Ad Group: [Concorrente] alternative
├─ Budget: 15%
└─ Goal: Captura insatisfeitos
```

---

### Ad Copy Templates

**Template 1: Problema + Solução**
```
Headline 1: Reduza Seu CAC em 40% | [Sua Marca]
Headline 2: Marketing Analytics em Tempo Real
Headline 3: Teste Grátis 14 Dias - Sem Cartão
Description: Plataforma de atribuição usada por 500+ empresas
B2B. Veja qual canal/criativo gera mais MQLs. Setup em 10 min.
CTA: Teste Grátis | Agendar Demo
```

**Template 2: Social Proof**
```
Headline 1: 500+ CMOs Usam [Sua Marca]
Headline 2: Reduza CAC | Aumente MQLs | ROI Mensurável
Headline 3: Avaliação 4.8⭐ | G2 & Capterra
Description: "Reduzimos CAC de $800 para $350 em 60 dias" - João,
CMO SaaS XYZ. Veja como você pode fazer o mesmo.
CTA: Ver Case Studies | Teste Grátis
```

**Template 3: Comparação (Competitor)**
```
Headline 1: Alternativa ao [Concorrente] | 50% Mais Barato
Headline 2: Mesmas Features | Melhor Suporte | Sem Lock-in
Headline 3: Migre em 24h | Setup Gratuito
Description: Clientes do [Concorrente] estão migrando para
[Você]. Melhor preço, integração rápida, suporte em PT.
CTA: Compare Features | Migrar Agora
```

---

### Landing Pages per Intent

**High-Intent (Bottom Funnel)**
```
Hero Section:
- Headline direto: "Marketing Attribution para B2B SaaS"
- Subheadline: Benefício principal
- Form curto (3 campos: Nome, Email, Empresa)
- CTA: "Teste Grátis" ou "Agendar Demo"

Social Proof:
- Logos de clientes
- Testimonial 1-2 (com foto, nome, cargo)

Features (3-5 bullets):
- Benefício, não feature: "Veja ROI de cada campanha" > "Dashboard analytics"

CTA repetido:
- Form no final da página também
```

**Mid-Intent (Research)**
```
Hero + Oferta:
- Lead magnet: "Baixe: Guia Completo de Marketing Attribution"
- Form: Nome, Email, Cargo

Conteúdo Educacional:
- Explicação do problema
- Como solução funciona (diagrama, video)
- Case studies

CTAs:
- Primário: Download lead magnet
- Secundário: Ver demo, Trial
```

---

### Budget Allocation

```yaml
Budget Total: $5,000/mês

Branded (Defesa): $500 (10%)
  - CPC baixo, CR alta
  - Não deixa concorrente roubar tráfego

Problem/Pain: $2,000 (40%)
  - Volume médio, CPC médio
  - Educação + captura email

Solution: $1,750 (35%)
  - CPC alto, mas intenção alta
  - Conversão melhor

Competitor: $750 (15%)
  - CPC variável
  - Oportunista
```

---

### Optimization Checklist

**Semanal:**
- [ ] Pause keywords com CPA > 2x target
- [ ] Aumenta lance em keywords com impressões < 10/dia
- [ ] Adiciona negative keywords (buscas irrelevantes)
- [ ] A/B test ad copy (novo headline/description)

**Mensal:**
- [ ] Análise de Search Terms Report (novas keywords)
- [ ] Revisa Quality Score (< 6 = problema)
- [ ] Testa novas landing pages (A/B test)
- [ ] Expande para Display/YouTube se Search funcionou

---

## Email Nurturing Campaigns

### Welcome Series (Novo Lead)

**Objetivo:** Educar novo lead e preparar para oferta

**Sequência (7 dias):**

```
EMAIL 1 - Day 0 (Imediato)
Subject: "Seu [Lead Magnet] + Próximos Passos"
Preview: "Obrigado por baixar! Aqui está..."

Body:
- Entrega do lead magnet (PDF, link)
- Dica rápida #1 relacionada
- CTA: "Leia nosso blog" (soft, não venda)

EMAIL 2 - Day 2
Subject: "[Nome], você viu isso? 🔥"
Preview: "3 empresas como a sua reduziram CAC em..."

Body:
- Case study curto (1 parágrafo)
- Link para caso completo
- CTA: "Ver mais cases"

EMAIL 3 - Day 4
Subject: "O erro #1 que aumenta seu CAC"
Preview: "90% das empresas fazem isso..."

Body:
- Artigo educacional
- Stats/dados
- CTA: "Quer evitar? Veja como" (link para webinar/demo)

EMAIL 4 - Day 6
Subject: "Convite especial: Webinar Quarta 14h"
Preview: "Vagas limitadas - Como reduzir CAC na prática"

Body:
- Convite para webinar/workshop
- O que vai aprender (3 bullets)
- CTA: "Garantir vaga"

EMAIL 5 - Day 7 (Se não registrou webinar)
Subject: "Prefere conversar 1-on-1?"
Preview: "Agende 15min com especialista"

Body:
- Oferece demo personalizada
- "Vamos analisar seu caso específico"
- CTA: "Agendar demo" (Calendly link)
```

---

### Trial Onboarding (SaaS)

**Objetivo:** Ativar trial user e converter para paid

**Sequência (14 dias - trial period):**

```
EMAIL 1 - Day 0 (Signup)
Subject: "Bem-vindo ao [Produto]! Comece aqui 👇"
Preview: "Setup em 5 minutos"

Body:
- Boas-vindas
- Quick start guide (3 passos)
- Video tutorial (2 min)
- CTA: "Começar agora" (link para plataforma)

EMAIL 2 - Day 1
Subject: "[Nome], conectou suas ferramentas?"
Preview: "Integre Google Ads, HubSpot, etc em 2 cliques"

Body:
- Benefício de integrar (ver dados em tempo real)
- Passo-a-passo com screenshots
- CTA: "Conectar ferramentas"

EMAIL 3 - Day 3 (Se não completou onboarding)
Subject: "Precisa de ajuda? Estamos aqui!"
Preview: "90% dos usuários fazem isso nos primeiros 3 dias"

Body:
- Offer ajuda (chat, call, tutorial)
- "Quer que a gente configure para você?"
- CTA: "Falar com suporte"

EMAIL 4 - Day 7 (Checkpoint)
Subject: "Já viu seu primeiro insight? 📊"
Preview: "Usuários que fazem X têm 3x mais chance de converter"

Body:
- Incentiva usar feature principal
- "Empresas que usam X veem ROI em 30 dias"
- Case study curto
- CTA: "Ver meu dashboard"

EMAIL 5 - Day 10 (Pre-Expiration)
Subject: "Seu trial expira em 4 dias"
Preview: "Upgrade agora e ganhe 20% off primeiro mês"

Body:
- Reminder do valor recebido
- Social proof ("500+ empresas já upgraded")
- Oferta especial (desconto, extended trial)
- CTA: "Fazer upgrade"

EMAIL 6 - Day 14 (Expiration)
Subject: "Último dia: Mantenha seu acesso 🔒"
Preview: "Não perca seu progresso e dados"

Body:
- Urgência (conta será suspensa)
- Recap do que vai perder
- One-click upgrade
- CTA: "Continuar assinatura"

EMAIL 7 - Day 15 (Expirou, não converteu)
Subject: "Sentiremos sua falta... mas aqui está 30% off"
Preview: "Última chance de voltar com desconto especial"

Body:
- Win-back offer (desconto maior)
- "O que podemos fazer melhor?" (feedback)
- CTA: "Voltar com desconto"
```

---

### Abandoned Cart (E-commerce)

**Sequência (3 dias):**

```
EMAIL 1 - 1 hora depois
Subject: "Você esqueceu algo no carrinho 🛒"
Preview: "[Produto X] ainda está te esperando"

Body:
- Imagem do produto
- "Complete sua compra em 1 clique"
- CTA: "Finalizar compra"

EMAIL 2 - 24 horas depois
Subject: "Frete GRÁTIS no seu carrinho 🎉"
Preview: "Só hoje: Free shipping no [Produto X]"

Body:
- Incentivo (frete grátis, desconto 10%)
- "Oferta expira em 24h"
- Reviews do produto (social proof)
- CTA: "Aproveitar oferta"

EMAIL 3 - 3 dias depois
Subject: "Última chance: [Produto X] está acabando"
Preview: "Só restam X unidades"

Body:
- Escassez ("estoque baixo")
- "Não perca - outros clientes estão comprando"
- Última chance desconto
- CTA: "Comprar agora"
```

---

### Upsell/Cross-Sell (Clientes Existentes)

**Trigger:** Cliente usa feature X (sinal de fit para upgrade)

```
EMAIL 1 - Educação
Subject: "[Nome], você está usando [Feature X]! 🎉"
Preview: "Sabia que no plano Pro você pode fazer Y?"

Body:
- "Notamos que você está usando muito [Feature X]"
- "Clientes Pro que fazem Y veem Z resultado"
- Case study de upgrade
- CTA: "Ver planos"

EMAIL 2 - 3 dias depois (Se não clicou)
Subject: "Upgrade para Pro = 3x mais [Benefício]"
Preview: "Veja o que você está perdendo"

Body:
- Comparação de planos (tabela)
- Benefícios do Pro
- "Teste Pro por 30 dias - garantia devolução"
- CTA: "Experimentar Pro"

EMAIL 3 - 7 dias depois (Oferta)
Subject: "Só para você: 25% off upgrade para Pro"
Preview: "Oferta especial de cliente fiel"

Body:
- Desconto exclusivo
- "Oferta expira em 48h"
- One-click upgrade
- CTA: "Fazer upgrade"
```

---

## Retargeting Campaign (Display & Social)

### Objetivo
Re-engajar visitantes que não converteram

### Segmentação

```
Segment 1: Visitou site, não converteu (Warm)
├─ Visitou nos últimos 30 dias
├─ Não preencheu form
└─ Mensagem: Educação + Lead magnet

Segment 2: Baixou lead magnet, não avançou (Warmer)
├─ Baixou ebook/guide
├─ Não agendou demo/trial
└─ Mensagem: Case study + Demo offer

Segment 3: Iniciou trial, não converteu (Hot)
├─ Signup trial
├─ Não upgraded
└─ Mensagem: Urgência + Desconto

Segment 4: Abandonou carrinho (E-commerce)
├─ Adicionou produto
├─ Não comprou
└─ Mensagem: Incentivo (desconto, frete grátis)
```

---

### Creative Strategy

**Warm Audience:**
```
Visual: Product screenshot + benefício
Headline: "Lembra de nós? 😊 Aqui está 10% off"
Body: "Complete seu cadastro e ganhe desconto especial"
CTA: "Resgatar desconto"
```

**Warmer Audience:**
```
Visual: Cliente testimonial + logo
Headline: "Empresa X reduziu CAC 40% - Veja como"
Body: "Agende demo e veja aplicado ao seu caso"
CTA: "Agendar demo"
```

**Hot Audience:**
```
Visual: Urgência (clock, oferta limitada)
Headline: "Seu trial expira em 2 dias ⏰"
Body: "Upgrade agora = 30% off primeiro mês"
CTA: "Fazer upgrade"
```

---

**Última atualização:** 2025-11-26
**Mantido por:** Luna (Marketing Agent)

*"Copy, customize, execute. Esses playbooks já geraram milhões em ROI. Seu próximo."*
