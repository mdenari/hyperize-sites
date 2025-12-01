@echo off
REM ============================================================================
REM start-claude.bat - Inicia CLI Claude para este projeto
REM ============================================================================
REM Coloque este arquivo na raiz do projeto
REM USE OCASIONALMENTE - Claude e mais caro que Gemini
REM ============================================================================

setlocal

REM Cores
set "GREEN=[92m"
set "YELLOW=[93m"
set "MAGENTA=[95m"
set "RESET=[0m"

echo.
echo %MAGENTA%========================================%RESET%
echo %MAGENTA%   Claude CLI - ELabs-Agile%RESET%
echo %MAGENTA%========================================%RESET%
echo.

REM Verificar se API key existe
if not defined ANTHROPIC_API_KEY (
    if exist ".env" (
        echo %YELLOW%Carregando .env...%RESET%
        for /f "usebackq tokens=1,* delims==" %%a in (".env") do (
            if "%%a"=="ANTHROPIC_API_KEY" set "ANTHROPIC_API_KEY=%%b"
        )
    )
)

if not defined ANTHROPIC_API_KEY (
    echo %YELLOW%AVISO: ANTHROPIC_API_KEY nao configurada%RESET%
    echo.
    echo Configure em:
    echo   1. Variavel de ambiente (Windows)
    echo   2. Arquivo .env na raiz do projeto
    echo.
    echo Exemplo .env:
    echo   ANTHROPIC_API_KEY=SUA_CHAVE_AQUI
    echo.
    echo Obtenha sua chave: https://console.anthropic.com
    echo.
    pause
    exit /b 1
)

REM Informacoes do projeto
set "PROJECT_DIR=%CD%"
echo %GREEN%Projeto:%RESET% %PROJECT_DIR%
echo %GREEN%Agent:%RESET% Claude 3.5 Sonnet (premium - caro!)
echo.

echo %YELLOW%ATENCAO: Claude e ~6x mais caro que Gemini%RESET%
echo Use apenas para:
echo   - Analise complexa (arquitetura, decisoes tecnicas)
echo   - Empatia necessaria (terapia, coaching profundo)
echo   - Raciocinio avancado (debugging dificil)
echo.
echo Para desenvolvimento geral, use start-gemini.bat
echo.
set /p "CONFIRM=Tem certeza que quer usar Claude? (S/N): "
if /i not "%CONFIRM%"=="S" (
    echo Operacao cancelada. Use start-gemini.bat
    pause
    exit /b 0
)
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

echo %MAGENTA%========================================%RESET%
echo %MAGENTA%   Iniciando Claude CLI...%RESET%
echo %MAGENTA%========================================%RESET%
echo.

REM TODO: Adicionar comando real do Claude CLI quando disponivel
REM Por enquanto, instrucoes
echo %YELLOW%INSTRUCOES:%RESET%
echo.
echo 1. Execute seu CLI Claude preferido (Claude Code, Cursor, etc)
echo 2. No prompt, diga:
echo.
echo %MAGENTA%"Ola! Estou trabalhando no projeto em: %PROJECT_DIR%"
echo.
echo "Por favor, leia:"
echo "- agents/config.md"
echo "- docs/COMO-!INIT_MODE!.md"
if exist "CHECKPOINT-SESSAO-*.md" echo "- CHECKPOINT-SESSAO-[ultima data].md"
echo.
echo "Me ajude a [seu objetivo de hoje]"
echo.
echo "OBS: Use sua empatia e raciocinio profundo para esta task complexa."%RESET%
echo.

REM Placeholder - substitua com CLI real
echo %YELLOW%Aguardando implementacao do Claude CLI...%RESET%
echo.
echo Por enquanto, use:
echo   - Claude Code (https://claude.ai/code)
echo   - Cursor (https://cursor.sh)
echo   - Claude web (https://claude.ai)
echo.

pause

endlocal
exit /b 0
