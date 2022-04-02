@echo off
if "%~1"=="" (
    set env=development
) else (
    set env=%~1
)
cmd /K "set FLASK_APP=app.app:create_app('%env%') & flask db init & flask db migrate & flask db upgrade & exit"
