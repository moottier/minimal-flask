@echo off

Rem run these from the app folder
Rem $env:FLASK_APP = "app:create_app('MyApp', 'TEST')"
Rem flask run --host=localhost --port=3000


Rem cmd /K "%~dp0/venv/Scripts/activate & cd app & flask run & exit"

cmd /K "%~dp0/venv/Scripts/activate & set FLASK_APP=app:create_app('MyApp', 'TEST') & cd app & flask run --host=localhost --port=3000 & exit"