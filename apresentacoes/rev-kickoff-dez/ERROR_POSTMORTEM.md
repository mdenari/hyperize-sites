# Relatório de Erro e Correção Arquitetural (Post-Mortem)

**Data:** 30/11/2025
**Incidente:** Falha recorrente de `SyntaxError` no script `publish.py`.

## 1. O Problema (Root Cause)
O script Python tentava armazenar um template HTML inteiro (com CSS e tags) dentro de uma variável usando **f-strings de aspas triplas** (`f"""..."""`).
*   **Conflito de Sintaxe:** O Python tentava interpretar chaves `{}` do CSS como variáveis Python.
*   **Erro de Escape:** Ao tentar corrigir, aspas internas do HTML entravam em conflito com as aspas do Python.
*   **Resultado:** O arquivo gerado sempre quebrava porque o parser do Python não encontrava o fim da string.

## 2. A Solução (Architecture Shift)
Abandonamos a abordagem de "HTML dentro do Python". Adotamos o padrão **External Template**.

### Nova Estrutura:
1.  **`menu_template.html`**: Arquivo HTML puro. Contém um placeholder `<!-- ITEMS_PLACEHOLDER -->` onde os cards serão inseridos. Zero código Python aqui.
2.  **`publish.py`**: O script agora apenas **lê** o arquivo acima, gera os cards HTML em um loop simples, e faz um `.replace()`.

## 3. Benefícios
*   **Imune a SyntaxError:** O Python não "executa" o HTML, apenas lê como texto.
*   **Manutenibilidade:** Você pode editar o design do menu mexendo no HTML sem risco de quebrar o script de publicação.

---
**Assinado:** CTO & Lead Architect
