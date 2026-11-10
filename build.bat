@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

echo ============================================
echo  PayrollPro build script (PyInstaller)
echo ============================================

rem ---- 1. Prepare virtual environment ----
if not exist .venv (
    echo [1/4] Creating virtual environment .venv ...
    where py >nul 2>nul
    if %errorlevel%==0 (
        py -3 -m venv .venv
    ) else (
        python -m venv .venv
    )
) else (
    echo [1/4] Virtual environment .venv already exists.
)

call .venv\Scripts\activate.bat

rem ---- 2. Install dependencies ----
echo [2/4] Installing dependencies ...
python -m pip install -q -r requirements.txt
python -m pip install -q -r requirements-dev.txt

rem ---- 3. Run unit tests ----
echo [3/4] Running unit tests ...
python -m pytest -q
if errorlevel 1 goto :err

rem ---- 4. Build exe ----
echo [4/4] Building dist\PayrollPro.exe ...
python -m PyInstaller --noconfirm --clean --onefile --windowed ^
    --name PayrollPro ^
    --icon assets/icon.ico ^
    --add-data "assets/icon.ico;assets" ^
    --paths . main.py
if errorlevel 1 goto :err

echo.
echo Build OK: dist\PayrollPro.exe
pause
exit /b 0

:err
echo.
echo Build FAILED. Please check the error messages above.
pause
exit /b 1
