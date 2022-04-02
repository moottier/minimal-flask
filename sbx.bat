@echo off
if "%1" == "testing" (
    echo toto
) else if "%1" == "production" (
    echo prodo
) else if "%1" == "development" (
    echo dev
) else (
    echo "default"
)