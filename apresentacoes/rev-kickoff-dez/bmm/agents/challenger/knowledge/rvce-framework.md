# 🔥 Framework RVCE - Reality Check Completo

**RVCE** = Real, Viável, Custável, Executável

Framework de avaliação brutal honest para toda e qualquer proposta de projeto/feature.

---

## R - REAL (Problema existe AGORA?)

### Perguntas Chave

1. **O problema existe e dói AGORA?**
   - ✅ Usuários reclamando diariamente
   - ✅ Processo manual queima 4h/dia
   - ✅ Cliente perdido por falta de feature
   - ❌ "Algum dia vamos precisar"
   - ❌ "Seria legal ter"
   - ❌ "Concorrente tem então precisamos"

2. **O problema está documentado?**
   - ✅ Tickets abertos, reclamações registradas
   - ✅ Métricas mostram impacto
   - ✅ ROI calculado
   - ❌ "Acho que usuários vão gostar"
   - ❌ "Faz sentido adicionar"

3. **Quantas pessoas/processos impacta?**
   - ✅ > 10 usuários diários
   - ✅ > 50% dos workflows
   - ⚠️ 3-10 usuários (avaliar custo-benefício)
   - ❌ 1-2 pessoas (não vale over-engineering)

### Red Flags ❌

- "Futuramente vamos precisar" (wishful thinking)
- "Seria útil para escalar depois" (YAGNI - You Aren't Gonna Need It)
- "Boas práticas recomendam" (sem contexto real)
- "Concorrente tem" (sem análise de impacto)

### Aprovação

✅ **REAL** se:
- Problema documentado com evidências
- Dói AGORA (não hipotético)
- Impacta > 10 usuários/processos significativos

---

## V - VIÁVEL (Consegue implementar < 2 semanas?)

### Perguntas Chave

1. **Consegue MVP funcional em < 2 semanas?**
   - ✅ 3-5 dias: ideal
   - ✅ 1-2 semanas: aceitável
   - ⚠️ 2-4 semanas: quebrar em fases
   - ❌ > 4 semanas: over-engineered

2. **Depende de quantas integrações?**
   - ✅ 0-1 integrações (self-contained)
   - ⚠️ 2-3 integrações (gerenciável)
   - ❌ > 3 integrações (frágil, interdependente)

3. **Usa stack existente ou precisa aprender nova?**
   - ✅ Docker Swarm, n8n, Supabase (dominado)
   - ⚠️ Nova lib em stack conhecida (rápido)
   - ❌ Nova stack completa (curva aprendizado)

4. **Arquitetura explica em < 2 min?**
   - ✅ Diagrama simples, fluxo claro
   - ❌ Múltiplos diagramas, ninguém explica completo

### Red Flags ❌

- "Só falta..." + lista de 10 coisas
- Múltiplas integrações interdependentes
- Arquitetura que depende de "tudo funcionando perfeitamente"
- Solução quebra se 1 API cair
- Precisa aprender 3+ tecnologias novas

### Aprovação

✅ **VIÁVEL** se:
- MVP em < 2 semanas (ou quebrável em fases)
- Usa stack existente
- Arquitetura simples (explica em 2 min)
- Máximo 2-3 dependências externas

---

## C - CUSTÁVEL (ROI positivo em 30 dias?)

### Perguntas Chave

1. **Quanto CUSTA implementar? (tempo)**
   - ✅ 1-5 dias: ótimo ROI
   - ⚠️ 1-2 semanas: ROI OK se impacto grande
   - ❌ > 2 semanas: ROI negativo (a não ser que...)

2. **Quanto ECONOMIZA/GERA? (tempo/dinheiro)**
   - ✅ Economiza > 5h/semana
   - ✅ Gera receita direta
   - ✅ Evita perda de cliente
   - ❌ Economiza < 2h/mês (não vale)

3. **ROI positivo em quanto tempo?**
   - ✅ 1-7 dias: ROI excelente
   - ✅ 1-4 semanas: ROI bom
   - ⚠️ 1-3 meses: ROI aceitável
   - ❌ > 3 meses: questionar fortemente

4. **Custo de MANUTENÇÃO?**
   - ✅ Self-service, zero manutenção
   - ⚠️ Manutenção ocasional (< 1h/mês)
   - ❌ Precisa atenção constante

### Fórmula ROI Simples

```
ROI = (Economia/Receita mensal) / (Custo implementação + Custo manutenção mensal)

✅ ROI > 3x = Excelente
✅ ROI > 2x = Bom
⚠️ ROI 1-2x = Aceitável
❌ ROI < 1x = Rejeitar
```

### Red Flags ❌

- "Depois traz ROI" (spoiler: não traz)
- Custo implementação alto + economia pequena
- Manutenção complexa/constante
- Payback > 6 meses

### Aprovação

✅ **CUSTÁVEL** se:
- ROI > 2x em 30 dias
- OU ROI > 3x em 90 dias
- OU impacto crítico (evita perda cliente, compliance)

---

## E - EXECUTÁVEL (Consegue manter rodando sozinho?)

### Perguntas Chave

1. **Consegue operar sozinho?**
   - ✅ Self-service completo
   - ✅ Logs/alertas automáticos
   - ⚠️ Requer atenção ocasional
   - ❌ Precisa babysitting constante

2. **Observabilidade configurada?**
   - ✅ Logs estruturados
   - ✅ Métricas em Grafana/Sentry
   - ✅ Alertas configurados
   - ❌ "Depois a gente adiciona" (spoiler: não adiciona)

3. **Rollback é possível?**
   - ✅ Rollback em < 5 min
   - ⚠️ Rollback manual (< 30 min)
   - ❌ Rollback complexo (> 1h)
   - ❌ Sem estratégia de rollback

4. **Debugging é simples?**
   - ✅ Logs claros, fácil reproduzir
   - ⚠️ Debugging médio (30-60 min)
   - ❌ Debugging complexo (> 2h)

5. **Documentação existe?**
   - ✅ Como rodar, troubleshooting, rollback
   - ⚠️ Documentação mínima
   - ❌ Zero documentação

### Red Flags ❌

- "Depois a gente melhora" (observabilidade, logs, docs)
- Arquitetura frágil (quebra fácil)
- Sem estratégia de rollback
- Debugging complexo (black box)
- Dependência de pessoa específica

### Aprovação

✅ **EXECUTÁVEL** se:
- Self-service ou requer mínima atenção
- Observabilidade completa (logs, métricas, alertas)
- Rollback simples (< 15 min)
- Debugging claro
- Documentação básica existe

---

## 🚦 VEREDITOS POSSÍVEIS

### ✅ APROVAR (4/4 ou 3/4 com justificativa)

**Quando:**
- Real ✅ + Viável ✅ + Custável ✅ + Executável ✅
- OU 3/4 com justificativa forte no 4º

**Output:**
```markdown
✅ APROVAR

Proposta passa no RVCE:
- Real: ✅ [justificativa]
- Viável: ✅ [justificativa]
- Custável: ✅ [ROI calculado]
- Executável: ✅ [justificativa]

Pode prosseguir com implementação.
```

---

### ⚠️ AJUSTAR (2-3/4)

**Quando:**
- Boa ideia mas over-engineered
- MVP possível mas precisa simplificar
- ROI OK mas custo alto (simplificar)

**Output:**
```markdown
⚠️ AJUSTAR

Proposta tem potencial mas precisa simplificação:

RVCE atual:
- Real: ✅ [ok]
- Viável: ❌ [muito complexo]
- Custável: ⚠️ [ROI marginal]
- Executável: ✅ [ok]

💡 ALTERNATIVA VIÁVEL:
[proposta simplificada cortando 70% mantendo 90% valor]

PRÓXIMOS PASSOS:
1. [ação simplificada]
2. [validação rápida]
3. [decisão go/no-go]
```

---

### ❌ REJEITAR (0-1/4)

**Quando:**
- Problema não existe (wishful thinking)
- Over-engineering extremo
- ROI negativo claro
- Manutenção insustentável

**Output:**
```markdown
❌ REJEITAR

Proposta não passa no RVCE:

- Real: ❌ [problema hipotético]
- Viável: ❌ [muito complexo]
- Custável: ❌ [ROI negativo]
- Executável: ❌ [manutenção insustentável]

MOTIVO PRINCIPAL: [explicação brutal honest]

💡 ALTERNATIVA (se houver):
[solução mais simples que resolve o problema real]

OU

RECOMENDAÇÃO: Não implementar. Foco em [X] que tem ROI claro.
```

---

## 📊 EXEMPLOS REAIS

### Exemplo 1: APROVAR

**Proposta:** Adicionar cache Redis para queries repetitivas

**RVCE:**
- **Real:** ✅ 80% queries são repetitivas, API lenta (2-3s)
- **Viável:** ✅ Redis já usado, implementação 2 dias
- **Custável:** ✅ ROI 10x (2 dias impl, economiza 20 dias CPU/mês)
- **Executável:** ✅ Redis monitorado, fallback para DB

**Veredito:** ✅ APROVAR

---

### Exemplo 2: AJUSTAR

**Proposta:** Sistema de RAG com embeddings, vector DB, fine-tuning

**RVCE:**
- **Real:** ✅ Usuários precisam buscar docs
- **Viável:** ❌ 3-4 semanas, múltiplas tecnologias novas
- **Custável:** ❌ ROI negativo (custo alto, economia pequena)
- **Executável:** ⚠️ Complexidade alta, manutenção constante

**Veredito:** ⚠️ AJUSTAR

**Alternativa Viável:**
- Fase 1: Gemini lê .md direto (0 infra nova, 1 dia impl)
- Testa 30 dias
- Se não resolver → considera RAG simplificado

---

### Exemplo 3: REJEITAR

**Proposta:** Microserviços com 10 services para MVP

**RVCE:**
- **Real:** ⚠️ "Futuramente vai escalar" (hipotético)
- **Viável:** ❌ 6+ semanas, arquitetura complexa
- **Custável:** ❌ ROI negativo massivo
- **Executável:** ❌ Debugging inferno, deploy complexo

**Veredito:** ❌ REJEITAR

**Alternativa:** Monolito modular (FastAPI), escala depois SE necessário

---

## 🎯 CHECKLIST RÁPIDO

Antes de aprovar qualquer proposta:

- [ ] Problema existe AGORA (não hipotético)?
- [ ] MVP implementável em < 2 semanas?
- [ ] ROI > 2x em 30 dias?
- [ ] Consegue manter rodando sozinho?
- [ ] Usa stack existente (Docker, n8n, Supabase)?
- [ ] Observabilidade configurada?
- [ ] Rollback simples?
- [ ] Arquitetura explica em < 2 min?

Se > 6 respostas SIM → ✅ APROVAR
Se 4-5 respostas SIM → ⚠️ AJUSTAR
Se < 4 respostas SIM → ❌ REJEITAR

---

**Framework RVCE v2.0**
*Mantém simples ou morre tentando* 🔥
