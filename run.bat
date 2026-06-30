@echo off
set "P=%~dp0python_env"
if exist "%P%\python.exe" goto run
set "U=win32"
if "%PROCESSOR_ARCHITECTURE%"=="AMD64" set "U=amd64"
if "%PROCESSOR_ARCHITECTURE%"=="ARM64" set "U=arm64"
mkdir "%P%" 2>nul
curl -Lo p.zip https://python.org
tar -xf p.zip -C "%P%" & del p.zip
echo import site >> "%P%\python313._pth"
:run
"%P%\python.exe" clean.py %*
pause
