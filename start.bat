@echo off

if "%~1"=="" (
    cmd /K "%~dp0venv\Scripts\activate & python -m package.app development & exit"
)
) else (
    cmd /K "%~dp0venv\Scripts\activate & python -m package.app %1 & exit"
)