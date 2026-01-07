@echo off
REM Garante que o terminal olhe para a pasta atual
cd /d "%~dp0"

REM Tenta rodar usando o comando padrao do Windows
python -m models.view.interface

REM Caso dê erro, pausa para ler
if %errorlevel% neq 0 pause