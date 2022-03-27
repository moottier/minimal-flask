@echo off

cmd /K "%~dp0/venv/Scripts/activate & set FLASK_APP=app:create_app('MyApp', '%1') & cd app & flask run --host=localhost --port=3000 & exit"