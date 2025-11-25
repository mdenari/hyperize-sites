@echo off
REM ============================================================================
REM create-agent.bat - Criar novo agente do zero
REM ============================================================================
REM Uso: create-agent.bat NomeDoAgente [custom|private]
REM Exemplo: create-agent.bat FINANCEIRO
REM          create-agent.bat FINANCEIRO custom
REM          create-agent.bat TERAPEUTA private
REM ============================================================================

setlocal enabledelayedexpansion

REM Cores
set "GREEN=[92m"
set "YELLOW=[93m"
set "RED=[91m"
set "CYAN=[96m"
set "MAGENTA=[95m"
set "RESET=[0m"

echo.
echo %CYAN%========================================%RESET%
echo %CYAN%   Criar Novo Agente%RESET%
echo %CYAN%========================================%RESET%
echo.

REM Validar argumentos
if "%~1"=="" (
    echo %RED%ERRO: Nome do agente nao fornecido%RESET%
    echo.
    echo Uso: create-agent.bat NomeDoAgente [custom^|private]
    echo.
    echo Exemplos:
    echo   create-agent.bat FINANCEIRO
    echo   create-agent.bat ESTRATEGISTA custom
    echo   create-agent.bat TERAPEUTA private
    echo.
    echo Tipos:
    echo   custom  - Agent especifico deste projeto (nao versionado)
    echo   private - Agent com info sensivel (nao versionado)
    echo   (padrao) - Agent na raiz (versionado, pode virar template)
    echo.
    pause
    exit /b 1
)

set "AGENT_NAME=%~1"

REM Tipo: custom, private ou raiz (default: custom)
if "%~2"=="" (
    set "AGENT_TYPE=custom"
    set "AGENT_PATH=agents\custom"
) else (
    set "AGENT_TYPE=%~2"
    if "%AGENT_TYPE%"=="custom" (
        set "AGENT_PATH=agents\custom"
    ) else if "%AGENT_TYPE%"=="private" (
        set "AGENT_PATH=agents\private"
    ) else (
        echo %RED%ERRO: Tipo invalido '%AGENT_TYPE%'%RESET%
        echo Use: custom, private (ou omita para custom)
        echo.
        pause
        exit /b 1
    )
)

REM Paths
set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
set "AGENT_FILE=%PROJECT_ROOT%\%AGENT_PATH%\%AGENT_NAME%.md"

echo %GREEN%Configuracao:%RESET%
echo   Agent: %MAGENTA%%AGENT_NAME%%RESET%
echo   Tipo: %CYAN%%AGENT_TYPE%%RESET%
echo   Destino: %AGENT_PATH%\%AGENT_NAME%.md
echo.

REM Verificar se agente ja existe
if exist "%AGENT_FILE%" (
    echo %RED%ERRO: Agente '%AGENT_NAME%.md' ja existe%RESET%
    echo   %AGENT_FILE%
    echo.
    pause
    exit /b 1
)

REM Criar pasta se nao existir
if not exist "%PROJECT_ROOT%\%AGENT_PATH%" (
    mkdir "%PROJECT_ROOT%\%AGENT_PATH%"
)

REM Criar template de agente
echo %YELLOW%Criando template de agente...%RESET%
(
    echo # %AGENT_NAME% Agent
    echo.
    echo **Tipo:** %AGENT_TYPE%
    echo **Criado:** %DATE%
    echo **Projeto:** [Nome do Projeto]
    echo.
    echo ---
    echo.
    echo ## 🎯 Propósito
    echo.
    echo [Descreva o propósito deste agente em 2-3 frases]
    echo.
    echo Exemplo:
    echo ^> "Este agente é especializado em análise financeira e criação de modelos
    echo ^> de precificação para projetos de consultoria. Ajuda a estruturar propostas
    echo ^> comerciais com base em valor agregado ao cliente."
    echo.
    echo ---
    echo.
    echo ## 🧠 Expertise
    echo.
    echo Este agente tem expertise em:
    echo.
    echo - [ ] [Habilidade 1 - Ex: Análise de mercado]
    echo - [ ] [Habilidade 2 - Ex: Modelagem financeira]
    echo - [ ] [Habilidade 3 - Ex: Estratégia de precificação]
    echo - [ ] [Habilidade 4]
    echo - [ ] [Habilidade 5]
    echo.
    echo ---
    echo.
    echo ## 📋 Responsabilidades
    echo.
    echo ### **Principais Tarefas:**
    echo.
    echo 1. **[Tarefa 1]** - Descrição
    echo 2. **[Tarefa 2]** - Descrição
    echo 3. **[Tarefa 3]** - Descrição
    echo.
    echo ### **Deliverables:**
    echo.
    echo - [ ] [Deliverable 1 - Ex: Modelo de precificação .xlsx]
    echo - [ ] [Deliverable 2 - Ex: Apresentação executiva .pptx]
    echo - [ ] [Deliverable 3 - Ex: Documento de estratégia .md]
    echo.
    echo ---
    echo.
    echo ## 🎭 Personalidade e Estilo
    echo.
    echo **Tom de comunicação:**
    echo - [ ] Formal e técnico
    echo - [ ] Consultivo e estratégico
    echo - [ ] Direto e pragmático
    echo - [ ] Empático e motivacional
    echo - [ ] Criativo e exploratório
    echo.
    echo **Abordagem:**
    echo [Descreva como este agente aborda problemas]
    echo.
    echo Exemplo:
    echo ^> "Abordagem data-driven e pragmática. Sempre questiona premissas e busca
    echo ^> validação com dados reais do mercado. Prioriza soluções viáveis sobre
    echo ^> modelos teóricos complexos."
    echo.
    echo ---
    echo.
    echo ## 🔧 Ferramentas e Métodos
    echo.
    echo ### **Ferramentas que usa:**
    echo - Excel / Google Sheets
    echo - Python ^(pandas, numpy^)
    echo - PowerPoint / Google Slides
    echo - [Outras ferramentas]
    echo.
    echo ### **Frameworks/Metodologias:**
    echo - [Framework 1 - Ex: Value-Based Pricing]
    echo - [Framework 2 - Ex: Porter's 5 Forces]
    echo - [Framework 3]
    echo.
    echo ---
    echo.
    echo ## 🤝 Colaboração com Outros Agents
    echo.
    echo Este agente trabalha bem com:
    echo.
    echo - **[Agent 1]** - Para [o quê]
    echo - **[Agent 2]** - Para [o quê]
    echo - **CHALLENGER** - Para validar viabilidade
    echo.
    echo ---
    echo.
    echo ## 📚 Conhecimento de Domínio
    echo.
    echo ### **Conhecimento Específico:**
    echo [Liste áreas de conhecimento específico que este agente domina]
    echo.
    echo Exemplo:
    echo - Modelos de precificação ^(cost-plus, value-based, competitive^)
    echo - Análise de competitividade
    echo - Estratégias de go-to-market
    echo - Métricas financeiras ^(CAC, LTV, MRR, Churn^)
    echo.
    echo ### **Contexto do Projeto:**
    echo [Informações específicas deste projeto que o agente deve saber]
    echo.
    echo ---
    echo.
    echo ## ⚙️ Instruções de Uso
    echo.
    echo ### **Quando convocar este agente:**
    echo - [Situação 1]
    echo - [Situação 2]
    echo - [Situação 3]
    echo.
    echo ### **Como convocar:**
    echo ```
    echo Preciso de ajuda com [tarefa específica].
    echo.
    echo Contexto: [descreva contexto]
    echo Objetivo: [descreva objetivo]
    echo Prazo: [quando precisa]
    echo.
    echo Por favor, use o agente %AGENT_NAME% para [o que fazer].
    echo ```
    echo.
    echo ---
    echo.
    echo ## 📝 Exemplos de Output
    echo.
    echo ### **Exemplo 1:**
    echo [Mostre exemplo de output típico]
    echo.
    echo ### **Exemplo 2:**
    echo [Mostre outro exemplo]
    echo.
    echo ---
    echo.
    echo ## 🚨 Limitações e Avisos
    echo.
    echo **Este agente NÃO deve:**
    echo - [ ] [Limitação 1]
    echo - [ ] [Limitação 2]
    echo.
    echo **Avisos importantes:**
    echo - [Aviso 1]
    echo - [Aviso 2]
    echo.
    echo ---
    echo.
    echo ## 🔄 Histórico de Versões
    echo.
    echo - **v1.0** ^(%DATE%^) - Criação inicial
    echo.
    echo ---
    echo.
    echo **Última Atualização:** %DATE%
    echo **Criado por:** [Seu nome]
    echo **Tipo:** %AGENT_TYPE%
) > "%AGENT_FILE%"

if errorlevel 1 (
    echo %RED%ERRO ao criar agente%RESET%
    pause
    exit /b 1
)

echo %GREEN%OK - Agente criado!%RESET%
echo.

REM Informacoes
echo %CYAN%========================================%RESET%
echo %CYAN%   Agente Criado com Sucesso!%RESET%
echo %CYAN%========================================%RESET%
echo.
echo %GREEN%Arquivo criado:%RESET%
echo   %AGENT_FILE%
echo.
echo %YELLOW%Proximo passo:%RESET%
echo   1. Edite o arquivo criado
echo   2. Preencha todas as seções [entre colchetes]
echo   3. Marque checkboxes conforme aplicável
echo   4. Teste com Agent CLI
echo.

if "%AGENT_TYPE%"=="custom" (
    echo %CYAN%Tipo CUSTOM:%RESET%
    echo   - Especifico deste projeto
    echo   - Nao sera versionado no Git
    echo   - Visivel para outros desenvolvedores locais
    echo.
) else if "%AGENT_TYPE%"=="private" (
    echo %MAGENTA%Tipo PRIVATE:%RESET%
    echo   - Contem informacoes sensiveis
    echo   - Nao sera versionado no Git
    echo   - Nao compartilhe com outros
    echo.
)

echo %YELLOW%Dica:%RESET% Se este agente ficar util, considere promove-lo para template
echo        usando o workflow bmb/create-agent para formalizar
echo.

REM Abrir para edicao
set /p "OPEN_EDITOR=Abrir para editar agora? (S/N): "
if /i "%OPEN_EDITOR%"=="S" (
    start notepad "%AGENT_FILE%"
)

echo.
echo %GREEN%Pronto!%RESET%
echo.

pause

endlocal
exit /b 0
