@echo off
REM Programming Visualization Platform - Windows Installer
REM Developed by issu321
REM https://github.com/issu321/Programming-Visualization

title Programming Visualization Installer
color 0B

echo ==========================================
echo   Programming Visualization Installer
echo   Developed by issu321
echo ==========================================
echo.

REM Check Python
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python 3.11+ from https://python.org
    pause
    exit /b 1
)
for /f "tokens=2" %%a in ('python --version') do set PYTHON_VERSION=%%a
echo ^> Python %PYTHON_VERSION% found

REM Create virtual environment
echo.
echo [2/6] Creating virtual environment...
if exist venv (
    echo ^> Removing existing virtual environment...
    rmdir /s /q venv
)
python -m venv venv
echo ^> Virtual environment created

REM Activate virtual environment
echo.
echo [3/6] Activating virtual environment...
call venv\Scripts\activate.bat
echo ^> Virtual environment activated

REM Upgrade pip
echo.
echo [4/6] Upgrading pip...
python -m pip install --upgrade pip
echo ^> Pip upgraded

REM Install dependencies
echo.
echo [5/6] Installing dependencies...
pip install -r requirements.txt
echo ^> Dependencies installed

REM Initialize database
echo.
echo [6/6] Initializing database...
python -c "from database import init_db; init_db()"
echo ^> Database initialized

echo.
echo ==========================================
echo   Installation Complete!
echo ==========================================
echo.
echo Developed by issu321
echo https://github.com/issu321/Programming-Visualization
echo.
echo "Launching...(Please Wait)"
python app.py
echo.
echo.
    pause
