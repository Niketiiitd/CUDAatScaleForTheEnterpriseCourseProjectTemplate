@echo off
setlocal

REM Define directories
set DATA_DIR=data
set TEXTURES_DIR=%DATA_DIR%\textures
set AERIALS_DIR=%DATA_DIR%\aerials

REM Define URLs
set TEXTURES_URL=https://sipi.usc.edu/database/textures.tar.gz
set AERIALS_URL=https://sipi.usc.edu/database/aerials.tar.gz

REM Define tar files
set TEXTURES_TAR=%TEXTURES_DIR%.tar.gz
set AERIALS_TAR=%AERIALS_DIR%.tar.gz

REM Ensure curl and tar are available
where curl >nul
if errorlevel 1 (
    echo curl is not installed. Please install curl and try again.
    exit /b 1
)

where tar >nul
if errorlevel 1 (
    echo tar is not installed. Please install tar and try again.
    exit /b 1
)

REM Create directories if they don't exist and download/extract data
if not exist "%TEXTURES_DIR%" (
    mkdir "%TEXTURES_DIR%"
    curl -L -o "%TEXTURES_TAR%" "%TEXTURES_URL%"
    tar -xzf "%TEXTURES_TAR%" -C "%TEXTURES_DIR%"
    del "%TEXTURES_TAR%"
)

if not exist "%AERIALS_DIR%" (
    mkdir "%AERIALS_DIR%"
    curl -L -o "%AERIALS_TAR%" "%AERIALS_URL%"
    tar -xzf "%AERIALS_TAR%" -C "%AERIALS_DIR%"
    del "%AERIALS_TAR%"
)

REM Run extract.py
python extract.py
if errorlevel 1 (
    echo Failed to run extract.py.
    exit /b 1
)

REM Install required packages
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install requirements.
    exit /b 1
)

REM Run main.py
python scripts\main.py
if errorlevel 1 (
    echo Failed to run main.py.
    exit /b 1
)

echo All tasks completed successfully.
endlocal
