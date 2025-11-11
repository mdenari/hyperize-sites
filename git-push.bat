@echo off
echo ========================================
echo Git Push - Hyperize Sites
echo ========================================
echo.

REM Adiciona todos os arquivos modificados
echo Adicionando arquivos...
git add -A

REM Verifica se há mudanças para commitar
git diff-index --quiet HEAD
if %errorlevel% equ 0 (
    echo.
    echo Nenhuma mudanca para commitar.
    pause
    exit /b 0
)

REM Solicita mensagem de commit
echo.
set /p "mensagem=Digite a mensagem do commit: "

REM Se não digitar nada, usa mensagem padrão
if "%mensagem%"=="" set mensagem=Atualizacao do site

REM Faz o commit
echo.
echo Commitando mudancas...
git commit -m "%mensagem%"

REM Faz o push
echo.
echo Enviando para GitHub...
git push

echo.
echo ========================================
echo Concluido! Deploy na Vercel iniciado.
echo ========================================
pause
