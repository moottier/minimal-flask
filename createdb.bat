@echo off
cd app
echo  ; | sqlite3 app.db
cd ..
@rem have to set env var to get flask commands to work. commands come from flask-sqlalchemy
$env:FLASK_APP = "app.app:create_app('%1')"
flask db init
flask db migrate
flask db upgrade