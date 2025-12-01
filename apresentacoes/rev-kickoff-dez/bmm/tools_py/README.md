# 🛠️ ELabs-Agile Python Tools

**Biblioteca de ferramentas Python para agents da metodologia ELabs-Agile.**

Permite que agents **executem ações reais** (não apenas planejamento), transformando conversas em outputs tangíveis.

---

## 📦 Instalação

```bash
# Instalar dependências
cd bmm/tools_py
pip install -r requirements.txt
```

---

## 🎯 Tools Disponíveis

### **Core Tools** (sempre disponíveis)

| Tool | Descrição | Use Case |
|------|-----------|----------|
| **SystemFileHandler** | Operações com arquivos (read, write, list) | Salvar relatórios, templates, configs |
| **APICaller** | Chamadas HTTP para APIs externas | Integrar CRM, enviar notificações |

### **Optional Tools** (Fase 2 - futuro)

| Tool | Descrição | Dependencies |
|------|-----------|--------------|
| **N8NTrigger** | Disparar workflows N8N | requests |
| **WebFetcher** | Web scraping | beautifulsoup4 |
| **PDFExtractor** | Extrair dados de PDFs | pdfplumber |
| **DataTransformer** | Manipulação de dados | pandas |

---

## 🚀 Quick Start

### **SystemFileHandler - Operações com Arquivos**

```python
from bmm.tools_py.core import SystemFileHandler

# Criar handler
handler = SystemFileHandler()

# Escrever arquivo
result = handler.write_file(
    "reports/analysis.md",
    "# Market Analysis\n\nContent here..."
)

if result["success"]:
    print(f"✅ {result['message']}")
    print(f"Bytes written: {result['bytes_written']}")
else:
    print(f"❌ Error: {result['error']}")

# Ler arquivo
result = handler.read_file("reports/analysis.md")

if result["success"]:
    print(f"Content:\n{result['content']}")

# Listar arquivos
result = handler.list_directory("reports", pattern="*.md")

print(f"Found {result['count']} markdown files:")
for file in result["files"]:
    print(f"  - {file}")
```

---

### **APICaller - Chamadas HTTP** *(Dia 2)*

```python
from bmm.tools_py.core import APICaller

# Criar caller
api = APICaller(base_url="https://api.example.com")

# GET request
result = api.get("/users", params={"page": 1})

if result["success"]:
    users = result["data"]
    print(f"Status: {result['status_code']}")
    print(f"Users: {users}")

# POST request
result = api.post(
    "/customers",
    json={"name": "João", "email": "joao@exemplo.com"}
)

if result["success"]:
    print(f"✅ Customer created: {result['data']}")
else:
    print(f"❌ Error: {result['error']}")
```

---

## 📚 SystemFileHandler - Documentação Completa

### **Métodos Disponíveis**

#### **1. write_file()** - Escrever arquivo

```python
result = handler.write_file(
    file_path="output.txt",
    content="Content to write",
    mode="overwrite",  # ou "append"
    encoding="utf-8"
)

# Returns:
# {
#     "success": bool,
#     "message": str,
#     "file_path": str,
#     "bytes_written": int,
#     "error": str | None
# }
```

**Parâmetros:**
- `file_path` (str): Caminho do arquivo (relativo ou absoluto)
- `content` (str): Conteúdo a escrever
- `mode` (str): `"overwrite"` (padrão) ou `"append"`
- `encoding` (str): Encoding do arquivo (padrão: `"utf-8"`)

**Comportamento:**
- Cria diretórios pai automaticamente se não existirem
- Modo `overwrite`: Substitui conteúdo existente
- Modo `append`: Adiciona ao final do arquivo

---

#### **2. read_file()** - Ler arquivo

```python
result = handler.read_file(
    file_path="input.txt",
    encoding="utf-8"
)

# Returns:
# {
#     "success": bool,
#     "content": str | None,
#     "file_path": str,
#     "error": str | None
# }
```

**Parâmetros:**
- `file_path` (str): Caminho do arquivo
- `encoding` (str): Encoding do arquivo (padrão: `"utf-8"`)

**Erros comuns:**
- `"File not found"`: Arquivo não existe
- `"Encoding error"`: Tente encoding diferente (ex: `"latin-1"`)
- `"Permission denied"`: Sem permissão para ler

---

#### **3. list_directory()** - Listar arquivos

```python
result = handler.list_directory(
    directory_path="reports",
    pattern="*.md",
    recursive=False
)

# Returns:
# {
#     "success": bool,
#     "files": List[str] | None,
#     "count": int,
#     "directory": str,
#     "error": str | None
# }
```

**Parâmetros:**
- `directory_path` (str): Diretório a listar (padrão: `"."`)
- `pattern` (str, opcional): Glob pattern (ex: `"*.py"`, `"**/*.md"`)
- `recursive` (bool): Busca recursiva (padrão: `False`)

**Exemplos de patterns:**
- `"*.md"`: Todos `.md` no diretório
- `"**/*.md"`: Todos `.md` recursivamente
- `"test_*.py"`: Arquivos que começam com `test_`

---

#### **4. file_exists()** - Verificar existência

```python
result = handler.file_exists("test.txt")

# Returns:
# {
#     "success": bool,
#     "exists": bool,
#     "is_file": bool,
#     "is_dir": bool,
#     "file_path": str
# }
```

---

#### **5. get_file_info()** - Metadata do arquivo

```python
result = handler.get_file_info("test.txt")

# Returns:
# {
#     "success": bool,
#     "size_bytes": int,
#     "created": str,
#     "modified": str,
#     "extension": str,
#     "error": str | None
# }
```

---

## 🎯 Casos de Uso Reais

### **Caso 1: Agent gerando relatório de análise**

```python
# Agent pesquisa dados e gera relatório
handler = SystemFileHandler()

# Gerar conteúdo
content = """# Análise de Mercado - SaaS XYZ

## Resumo Executivo
- TAM: $50M
- Concorrentes: 5 principais
- Oportunidade: Gap em UX

## Concorrentes
1. **Competitor A** - $10M ARR, 2,000 clientes
2. **Competitor B** - $8M ARR, 1,500 clientes
...

## Recomendação
Focar em simplicidade e UX para diferenciar.
"""

# Salvar relatório
result = handler.write_file(
    "reports/market-analysis-2025-11-30.md",
    content
)

# Agent retorna: "✅ Relatório salvo em reports/market-analysis-2025-11-30.md"
```

**Antes das tools:** Usuário copia/cola manualmente (5 min)
**Com as tools:** Agent salva automaticamente (0 min)
**Economia: 5 min por relatório**

---

### **Caso 2: Agent gerando múltiplos templates**

```python
# Agent cria templates para 3 verticais
handler = SystemFileHandler()

verticais = ["Comex", "DocsFlow", "Hyperize"]

for vertical in verticais:
    template = f"""# Reunião Estratégica - {vertical}

## Pauta (1 hora)
1. Passivo Técnico (10 min)
2. Segurança (10 min)
3. UX/Simplicidade (20 min)
4. Métricas e Ações (20 min)

## Responsável
- Líder: [Nome]
- Facilitador: SM
"""

    result = handler.write_file(
        f"templates/REV-{vertical.lower()}.md",
        template
    )

# Agent retorna: "✅ 3 templates criados: templates/REV-*.md"
```

**Antes das tools:** Criar 3 arquivos manualmente (15 min)
**Com as tools:** Agent cria automaticamente (0 min)
**Economia: 15 min**

---

### **Caso 3: Agent lendo inputs para continuar trabalho**

```python
# Agent lê arquivo de objetivos antes de gerar proposta
handler = SystemFileHandler()

# Ler input
result = handler.read_file("objetivo.md")

if result["success"]:
    objetivos = result["content"]

    # Agent analisa objetivos
    # Agent gera proposta baseada em objetivos REAIS
    # Agent salva proposta

    handler.write_file(
        "proposta-gerada.md",
        f"# Proposta\n\nBaseado em:\n{objetivos}\n\n..."
    )

# Agent NÃO inventa, usa dados REAIS do arquivo
```

---

## 🧪 Testes

```bash
# Rodar todos os testes
cd bmm/tools_py
pytest tests/ -v

# Rodar testes específicos
pytest tests/test_file_handler.py -v

# Rodar com coverage
pytest tests/ --cov=bmm.tools_py --cov-report=html
```

---

## 🔧 Troubleshooting

### **Erro: "File not found"**
```python
# Verificar se arquivo existe antes de ler
result = handler.file_exists("test.txt")
if not result["exists"]:
    print("Arquivo não existe, criando...")
    handler.write_file("test.txt", "Default content")
```

### **Erro: "Permission denied"**
- Verifique permissões da pasta
- Windows: Execute como administrador se necessário
- Linux/Mac: `chmod` a pasta

### **Erro: "Encoding error"**
```python
# Tentar encoding diferente
result = handler.read_file("file.txt", encoding="latin-1")
```

---

## 📊 Métricas de Performance

| Operação | Tempo médio | Notas |
|----------|-------------|-------|
| `write_file()` 1KB | < 1ms | Muito rápido |
| `read_file()` 1MB | ~50ms | Depende do disco |
| `list_directory()` 1000 files | ~100ms | Cache do SO ajuda |

---

## 🚀 Roadmap

### **Fase 1 (Atual - MVP):**
- ✅ SystemFileHandler (read, write, list)
- 🚧 APICaller (GET, POST, PUT, DELETE)
- 📝 Testes unitários
- 📝 Documentação completa

### **Fase 2 (Futuro):**
- ⏸️ N8NTriggerTool (disparar workflows)
- ⏸️ WebFetcherTool (web scraping)
- ⏸️ PDFExtractorTool (ler PDFs)
- ⏸️ DataTransformerTool (pandas)

---

## 📝 Changelog

### v1.0.0 (2025-11-30)
- ✅ SystemFileHandler implementado
- ✅ Testes unitários completos
- ✅ Documentação inicial
- 🚧 APICaller em progresso

---

## 🤝 Contribuindo

Para adicionar novas tools:
1. Criar arquivo em `core/` ou `optional/`
2. Seguir padrão de retorno: `{"success": bool, "data": any, "error": str | None}`
3. Adicionar testes em `tests/`
4. Documentar em README.md
5. Atualizar `__init__.py`

---

## 📄 Licença

Parte da metodologia ELabs-Agile.
Uso interno Hyperize/ZPT Digital.

---

**ELabs-Agile Tools** - Transformando agents em executores reais 🚀
