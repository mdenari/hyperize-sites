@echo off
REM ============================================================================
REM start-gemini.bat - Inicia CLI Gemini para este projeto
REM ============================================================================
REM Coloque este arquivo na raiz do projeto
REM ============================================================================

setlocal

REM Cores
set "GREEN=[92m"
set "YELLOW=[93m"
set "CYAN=[96m"
set "RESET=[0m"

echo.
echo %CYAN%========================================%RESET%
echo %CYAN%   Gemini CLI - ELabs-Agile%RESET%
echo %CYAN%========================================%RESET%
echo.

REM Verificar se API key existe
if not defined GEMINI_API_KEY (
    if exist ".env" (
        echo %YELLOW%Carregando .env...%RESET%
        for /f "usebackq tokens=1,* delims==" %%a in (".env") do (
            if "%%a"=="GEMINI_API_KEY" set "GEMINI_API_KEY=%%b"
        )
    )
)

if not defined GEMINI_API_KEY (
    echo %YELLOW%AVISO: GEMINI_API_KEY nao configurada%RESET%
    echo.
    echo Configure em:
    echo   1. Variavel de ambiente (Windows)
    echo   2. Arquivo .env na raiz do projeto
    echo.
    echo Exemplo .env:
    echo   GEMINI_API_KEY=SUA_CHAVE_AQUI
    echo.
    echo Obtenha sua chave: https://makersuite.google.com/app/apikey
    echo.
    pause
    exit /b 1
)

REM Informacoes do projeto
set "PROJECT_DIR=%CD%"
echo %GREEN%Projeto:%RESET% %PROJECT_DIR%
echo %GREEN%Agent:%RESET% Gemini 1.5 Flash (custo-efetivo)
echo.

REM Verificar arquivos importantes
if not exist "agents\config.md" (
    echo %YELLOW%AVISO: agents\config.md nao encontrado%RESET%
    echo Por favor, configure o projeto primeiro.
    echo.
    pause
    exit /b 1
)

echo %YELLOW%Preparando contexto...%RESET%
echo.

REM Determinar se e primeira vez ou retomada
if exist "CHECKPOINT-SESSAO-*.md" (
    echo %GREEN%[OK]%RESET% Projeto existente - modo RETOMADA
    echo      Leia: docs\COMO-RETOMAR.md
    set "INIT_MODE=RETOMADA"
) else (
    echo %GREEN%[OK]%RESET% Projeto novo - modo INICIO
    echo      Leia: docs\COMO-INICIAR.md
    set "INIT_MODE=INICIO"
)

echo.
echo %YELLOW%Arquivos disponiveis para o agent:%RESET%
echo   - agents\config.md
echo   - agents\*.md (outros agents)
echo   - docs\COMO-!INIT_MODE!.md
if exist "CHECKPOINT-SESSAO-*.md" echo   - CHECKPOINT-SESSAO-*.md
if exist "docs\prd.md" echo   - docs\prd.md
if exist "docs\tech-spec.md" echo   - docs\tech-spec.md
echo.

echo %CYAN%========================================%RESET%
echo %CYAN%   Iniciando Gemini CLI...%RESET%
echo %CYAN%========================================%RESET%
echo.

REM TODO: Adicionar comando real do Gemini CLI quando disponivel
REM Por enquanto, instrucoes
echo %YELLOW%INSTRUCOES:%RESET%
echo.
echo 1. Execute seu CLI Gemini preferido
echo 2. No prompt, diga:
echo.
echo %CYAN%"Ola! Estou trabalhando no projeto em: %PROJECT_DIR%"
echo.
echo "Por favor, leia:"
echo "- agents/config.md"
echo "- docs/COMO-!INIT_MODE!.md"
if exist "CHECKPOINT-SESSAO-*.md" echo "- CHECKPOINT-SESSAO-[ultima data].md"
echo.
echo "Me ajude a [seu objetivo de hoje]"%RESET%
echo.

REM Placeholder - substitua com CLI real
echo %YELLOW%Aguardando implementacao do Gemini CLI...%RESET%
echo.
echo Por enquanto, use:
echo   - Claude Code (se configurado)
echo   - Cursor (se configurado)
echo   - Gemini web (https://gemini.google.com)
echo.

pause

endlocal
exit /b 0
