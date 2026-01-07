@echo off
REM Garante que o terminal olhe para a pasta atual
cd /d "%~dp0"

echo === RODANDO TESTES UNITARIOS ===
echo.

REM Executa o modulo de teste especifico
python -m models.view.test_frota

REM Se houver erro, pausa para leitura
if %errorlevel% neq 0 (
    echo.
    echo [X] ALGUNS TESTES FALHARAM!
    pause
) else (
    echo.
    echo [OK] TODOS OS TESTES PASSARAM!
    pause
)