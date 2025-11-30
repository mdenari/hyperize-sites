# 🏗️ Hyperize Stack Reference

**Max's baseline knowledge - Stack Hyperize 2025**

## Cloud-Native Infrastructure

### Orquestração
- **Docker Swarm** (produção)
- **Portainer** (gestão centralizada)
- **Hetzner Cloud** (Europa) - 4 VPS: 3 managers + 1 database
- **Cloudflare tunnels** (DNS, alta disponibilidade)

### Observabilidade
- **Sentry** - Error tracking
- **Grafana** - Métricas e dashboards

### SLA
- 99.9% uptime
- Failover < 30 segundos

---

## AI & Automação

### Plataformas
- **n8n** - Workflows e agentes (editor, webhook, workers distribuídos)
- **Windmill** - Orquestração (editor, webhook, workers distribuídos)
- **Langgraph** - Agentes de IA complexos
- **Kestra** - Orquestração adicional

### Workers
- Python para transformações de alta performance
- TypeScript para lógica de negócio
- 50+ scripts reutilizáveis

### Métricas
- 100k+ transações/dia
- Latência média: 180ms
- 99.7% confiabilidade

---

## Frontend

- **React** (Replit)
- **Node.js**

---

## Backend

- **Python 3.11+**
- **TypeScript**
- **FastAPI** (quando necessário)

---

## Database

### Primary
- **Supabase Cloud** (gerenciado)
- **PostgreSQL** (via Supabase)

### Caching
- **Redis**

### n8n Database
- **PostgreSQL** dedicado

---

## Integrações

### Comunicação
- **Gmail API**
- **WhatsApp** (Evolution API)

### Pagamentos
- **Stripe**

### Dados
- **REST APIs**
- **GraphQL APIs**

---

## DevOps

### Deployment
- Docker Swarm deploy
- Distribuição: n8n e Windmill nos managers
- Editor, webhook, workers separados

### CI/CD
- Deployment: desenvolvimento → homologação → produção (< 5 min)

---

## Architectural Patterns

### Multi-Tenant
- Isolamento por cliente
- Segurança garantida

### Distributed Workers
- n8n workers nos 3 managers
- Windmill workers nos 3 managers
- Load balancing automático

### High Availability
- Redundância geográfica
- Failover automático
- DNS via Cloudflare

---

## Decision Framework

**Use essa stack SEMPRE que possível:**

✅ **Quando usar o quê:**
- Automação visual → n8n
- Automação code-first → Windmill
- Agentes IA complexos → Langgraph
- Database → Supabase/PostgreSQL primeiro
- Caching → Redis
- WhatsApp → Evolution API
- Pagamentos → Stripe

❌ **Evite adicionar:**
- Outro orquestrador (temos n8n + Windmill)
- Outro database (temos Supabase + Redis)
- Outro WhatsApp client (temos Evolution)
- Framework pesado quando FastAPI resolve

---

## Performance Benchmarks

- **Latência:** < 200ms target
- **Throughput:** 100k+ transações/dia
- **Confiabilidade:** > 99.5%
- **Uptime:** > 99.9%

---

## Contact Points

- **Infra issues:** Check Portainer
- **Errors:** Check Sentry
- **Performance:** Check Grafana
- **Logs:** Docker Swarm logs
