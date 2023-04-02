@echo off
setlocal

set requirements=requirements.txt

:check_pip
pip -V > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pip...
    python -m ensurepip --default-pip > nul
    if %errorlevel% neq 0 (
        echo Failed to install pip.
        exit /b 1
    )
)

echo Updating pip...
python -m pip install --upgrade pip > nul
if %errorlevel% neq 0 (
    echo Failed to update pip.
    exit /b 1
)

echo Checking requirements...
python -m pip install -r %requirements% > nul
if %errorlevel% neq 0 (
    echo Failed to install requirements.
    exit /b 1
)

echo All required libraries are installed.

rem Wait for 1 day before checking again
ping -n 86400 127.0.0.1 > nul

goto :check_pip
