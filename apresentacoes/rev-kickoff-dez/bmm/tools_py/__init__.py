"""
ELabs-Agile Python Tools

Biblioteca de ferramentas Python para agents da metodologia ELabs-Agile.
Permite que agents executem ações reais (não apenas planejamento).

Core Tools:
- SystemFileHandler: Operações com arquivos (read, write, list)
- APICaller: Chamadas HTTP para APIs externas

Optional Tools (Fase 2):
- N8NTrigger: Disparar workflows N8N
- WebFetcher: Web scraping (requests + BeautifulSoup)
- PDFExtractor: Extrair dados de PDFs
- DataTransformer: Manipulação de dados com pandas
"""

__version__ = "1.0.0"
__author__ = "ELabs-Agile Team"

# Import core tools for easy access
from bmm.tools_py.core.file_handler import SystemFileHandler
from bmm.tools_py.core.api_caller import APICaller

__all__ = [
    "SystemFileHandler",
    "APICaller",
]
