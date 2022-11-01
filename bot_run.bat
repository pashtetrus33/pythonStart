@echo off

call %~dp0dz_10\venv\Scripts\activate
cd %~dp0dz_10

set TOKEN=

python bot_telegram.py

pause