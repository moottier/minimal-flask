@echo off

cmd /K "%~dp0/venv/Scripts/activate & python -m unittest %1 & exit"
