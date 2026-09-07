@echo off
chcp 65001 > nul
title Santini Digital - Enviar para GitHub
echo ========================================================
echo   SANTINI DIGITAL - ENVIAR SITES DE PADARIAS PARA O GITHUB
echo ========================================================
echo.
cd /d "E:\SANTINI DIGITAL\MARKETING\pages\SITES PADARIAS"
echo Conectando e enviando para https://github.com/cascramer4/sites-padarias.git ...
echo.
"C:\Program Files\Git\cmd\git.exe" push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo ========================================================
    echo   [SUCESSO] Repositório publicado com sucesso no GitHub!
    echo ========================================================
) else (
    echo ========================================================
    echo   [AVISO] Verifique a autorização no GitHub acima.
    echo ========================================================
)
echo.
pause
