@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

<<<<<<< HEAD:venv/Scripts/activate.bat
set VIRTUAL_ENV=C:\Users\Abdaisy Conaição\Desktop\PI1\salvação\programacao-avancada-com-python-10794\venv
=======
set VIRTUAL_ENV=C:\Users\Lara Pires\OneDrive\PI-2\programacao-avancada-com-python-10794\.venv
>>>>>>> f1a2089aa2a64c0e43513479e552cf759ae1a700:.venv/Scripts/activate.bat

if not defined PROMPT set PROMPT=$P$G

if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

set _OLD_VIRTUAL_PROMPT=%PROMPT%
<<<<<<< HEAD:venv/Scripts/activate.bat
set PROMPT=(venv) %PROMPT%
=======
set PROMPT=(.venv) %PROMPT%
>>>>>>> f1a2089aa2a64c0e43513479e552cf759ae1a700:.venv/Scripts/activate.bat

if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not defined _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

set PATH=%VIRTUAL_ENV%\Scripts;%PATH%
<<<<<<< HEAD:venv/Scripts/activate.bat
set VIRTUAL_ENV_PROMPT=(venv) 
=======
set VIRTUAL_ENV_PROMPT=(.venv) 
>>>>>>> f1a2089aa2a64c0e43513479e552cf759ae1a700:.venv/Scripts/activate.bat

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)
