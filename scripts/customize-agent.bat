@echo off
REM ============================================================================
REM customize-agent.bat - Customizar agente existente para este projeto
REM ============================================================================
REM Uso: customize-agent.bat NomeDoAgente [custom|private]
REM Exemplo: customize-agent.bat pm
REM          customize-agent.bat pm custom
REM          customize-agent.bat financas private
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
echo %CYAN%   Customizar Agente%RESET%
echo %CYAN%========================================%RESET%
echo.

REM Validar argumentos
if "%~1"=="" (
    echo %RED%ERRO: Nome do agente nao fornecido%RESET%
    echo.
    echo Uso: customize-agent.bat NomeDoAgente [custom^|private]
    echo.
    echo Exemplos:
    echo   customize-agent.bat pm
    echo   customize-agent.bat analyst custom
    echo   customize-agent.bat financas private
    echo.
    echo Tipos:
    echo   custom  - Customizacao local (nao versionado, mas visivel)
    echo   private - Agente privado (nao versionado, informacao sensivel)
    echo.
    pause
    exit /b 1
)

set "AGENT_NAME=%~1"

REM Tipo: custom ou private (default: custom)
if "%~2"=="" (
    set "AGENT_TYPE=custom"
) else (
    set "AGENT_TYPE=%~2"
)

REM Validar tipo
if not "%AGENT_TYPE%"=="custom" (
    if not "%AGENT_TYPE%"=="private" (
        echo %RED%ERRO: Tipo invalido '%AGENT_TYPE%'%RESET%
        echo Use: custom ou private
        echo.
        pause
        exit /b 1
    )
)

REM Paths
set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
set "AGENT_SOURCE=%PROJECT_ROOT%\agents\%AGENT_NAME%.md"
set "AGENT_DEST=%PROJECT_ROOT%\agents\%AGENT_TYPE%\%AGENT_NAME%-custom.md"

echo %GREEN%Configuracao:%RESET%
echo   Agent: %MAGENTA%%AGENT_NAME%%RESET%
echo   Tipo: %CYAN%%AGENT_TYPE%%RESET%
echo   Origem: agents\%AGENT_NAME%.md
echo   Destino: agents\%AGENT_TYPE%\%AGENT_NAME%-custom.md
echo.

REM Verificar se agente original existe
if not exist "%AGENT_SOURCE%" (
    echo %RED%ERRO: Agente '%AGENT_NAME%.md' nao encontrado%RESET%
    echo.
    echo Agentes disponiveis:
    dir /b "%PROJECT_ROOT%\agents\*.md" 2>nul
    echo.
    pause
    exit /b 1
)

REM Verificar se customizacao ja existe
if exist "%AGENT_DEST%" (
    echo %YELLOW%AVISO: Customizacao ja existe:%RESET%
    echo   %AGENT_DEST%
    echo.
    set /p "OVERWRITE=Sobrescrever? (S/N): "
    if /i not "!OVERWRITE!"=="S" (
        echo Operacao cancelada.
        echo.
        pause
        exit /b 0
    )
    echo.
)

REM Criar pasta se nao existir
if not exist "%PROJECT_ROOT%\agents\%AGENT_TYPE%" (
    mkdir "%PROJECT_ROOT%\agents\%AGENT_TYPE%"
)

REM Copiar agente
echo %YELLOW%Criando customizacao...%RESET%
copy "%AGENT_SOURCE%" "%AGENT_DEST%" >nul 2>&1
if errorlevel 1 (
    echo %RED%ERRO ao copiar agente%RESET%
    pause
    exit /b 1
)

REM Adicionar header de customizacao
echo %YELLOW%Adicionando header de customizacao...%RESET%
powershell -Command "$content = Get-Content '%AGENT_DEST%' -Raw; $header = '# CUSTOMIZADO - %AGENT_NAME%`n`nEste agente foi customizado para este projeto especifico.`nBaseado em: agents/%AGENT_NAME%.md`nTipo: %AGENT_TYPE%`nData: %DATE%`n`n---`n`n'; Set-Content '%AGENT_DEST%' ($header + $content)" >nul 2>&1

echo %GREEN%OK - Customizacao criada!%RESET%
echo.

REM Informacoes
echo %CYAN%========================================%RESET%
echo %CYAN%   Customizacao Criada!%RESET%
echo %CYAN%========================================%RESET%
echo.
echo %GREEN%Arquivo criado:%RESET%
echo   %AGENT_DEST%
echo.
echo %YELLOW%Proximo passo:%RESET%
echo   1. Edite o arquivo customizado
echo   2. Personalize para seu projeto
echo   3. Use no Agent CLI
echo.

if "%AGENT_TYPE%"=="custom" (
    echo %CYAN%Tipo CUSTOM:%RESET%
    echo   - Nao sera versionado no Git
    echo   - Especifico deste projeto
    echo   - Visivel para outros desenvolvedores
) else (
    echo %MAGENTA%Tipo PRIVATE:%RESET%
    echo   - Nao sera versionado no Git
    echo   - Contem informacoes sensiveis
    echo   - Nao compartilhe com outros
)
echo.

REM Abrir para edicao
set /p "OPEN_EDITOR=Abrir para editar agora? (S/N): "
if /i "%OPEN_EDITOR%"=="S" (
    start notepad "%AGENT_DEST%"
)

echo.
echo %GREEN%Pronto!%RESET%
echo.

pause

endlocal
exit /b 0
