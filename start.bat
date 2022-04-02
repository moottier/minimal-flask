@echo off

if "%~1"=="" (
    cmd /K "%~dp0venv\Scripts\activate & python -m app.app development & exit"
)
) else (
    cmd /K "%~dp0venv\Scripts\activate & python -m app.app %1 & exit"
)