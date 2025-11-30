# ELabs Publish Tool 🚀

Ferramenta CLI para automação de publicação de apresentações estáticas no portal Expert Labs (Vercel).

## 📋 Como Usar

Para publicar uma nova apresentação, abra o terminal nesta pasta (`Sites`) e execute:

```bash
python publish.py --name "Nome da Apresentação" --source "C:\Caminho\Para\Pasta\Original" --slug "nome-curto-url" [OPÇÕES]
```

### Argumentos:
*   `--name`: Título que aparecerá no menu principal do portal.
*   `--source`: Caminho completo da pasta onde está o `index.html` da apresentação. Esta pasta deve ser **autocontida** (todos os assets como imagens, CSS, JS devem estar nela ou em subpastas relativas).
*   `--slug`: (Opcional) Nome usado na URL (ex: `kickoff-dez`). Se não informado, será gerado a partir do nome.
*   `--protected`: (Opcional) Se presente, a apresentação exigirá senha para acesso.

### Exemplos:

**1. Publicar apresentação pública:**
```bash
python publish.py --name "Relatório Comex" --source "C:\Users\mauri\mycode\Projetos\RelatorioComex"
```

**2. Publicar apresentação protegida por senha:**
```bash
python publish.py --name "Kickoff Dezembro" --source "C:\Users\mauri\mycode\Projetos\ExecutiveMeeting" --slug "kickoff-dez" --protected
```

---

## 🔐 Segurança (Senha Mestra)

Este portal utiliza uma **Senha Mestra Única** para proteger conteúdos sensíveis. Essa senha é a "Senha da Diretoria" ou "Expert Labs Confidencial".

1.  **Como definir a Senha Mestra (no Vercel):**
    *   Vá para o painel da Vercel (`https://vercel.com/dashboard`).
    *   Selecione o projeto correspondente ao repositório `Sites`.
    *   Vá em **Settings > Environment Variables**.
    *   Crie uma variável chamada `SITE_PASSWORD` e defina a senha (ex: `ExpertLabs2026!`).
    *   Esta senha será a única a ser gerenciada para todas as apresentações protegidas.

2.  **Como proteger uma apresentação:**
    *   Ao usar o `publish.py`, inclua a flag `--protected` no comando.
    *   O script registrará no `presentations.json` que essa apresentação é protegida.
    *   O Vercel Edge Middleware detectará isso e exigirá a `SITE_PASSWORD` para acesso.

---

## 📂 Estrutura do Projeto (dentro da pasta `Sites`)

```text
Sites/
├── public/
│   ├── index.html        # Menu Principal do Portal (Gerado Automaticamente pelo publish.py)
│   ├── assets/           # (Opcional: Assets globais do portal, ex: logo da Expert Labs)
│   └── apresentacoes/    # Subpastas com as apresentações publicadas
│       └── {slug_da_apresentacao}/
│           └── index.html # A apresentação HTML copiada
│           └── ... (outros assets da apresentação)
├── publish.py            # O Script de Automação do ELabs Publish Tool
├── presentations.json    # Banco de Dados de Metadados das apresentações
├── middleware.js         # Lógica de Segurança para Vercel Edge Functions
└── README.md             # Este arquivo
```

## 🛠️ Manutenção

*   **Para remover uma apresentação:** Edite o `presentations.json` manualmente e apague a pasta correspondente em `public/apresentacoes/`. Rode o `publish.py` sem argumentos (futuro `--rebuild`) para regenerar o menu.
*   **Para atualizar uma apresentação:** Basta rodar o comando de publicação novamente com o mesmo `--slug`. O script substituirá os arquivos da apresentação.
