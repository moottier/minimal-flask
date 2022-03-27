@echo off

cmd /K "python -m venv venv & %~dp0/venv/Scripts/activate & pip install -e . & exit"
