@echo off
title NeuroQuest Application Launcher
echo ======================================================================
echo           LAUNCHING NEUROQUEST PLATFORM (BACKEND + FRONTEND)
echo ======================================================================
echo.

cd /d "%~dp0"

echo [1/3] Starting FastAPI Backend Daemon on port 8000...
start "NeuroQuest Backend (Port 8000)" cmd /k "cd /d "%~dp0backend" && python run.py"

timeout /t 2 /nobreak >nul

echo [2/3] Starting Vite React Frontend on port 5173...
start "NeuroQuest Frontend (Port 5173)" cmd /k "cd /d "%~dp0frontend" && npm run dev"

timeout /t 3 /nobreak >nul

echo [3/3] Opening Web Browser to http://localhost:5173/ ...
start http://localhost:5173/

echo.
echo ======================================================================
echo   NeuroQuest is LIVE!
echo   * Frontend : http://localhost:5173/
echo   * Backend  : http://127.0.0.1:8000/docs
echo ======================================================================
echo.
pause
