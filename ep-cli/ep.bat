@echo off
REM Call this wrapper from anywhere to start a ep request. All arguments are forwarded to ep.py
REM This wrapper will first initialize (or activate) a python environment with all needed packages.
REM Intended usage is a convenient integration into external tools, e.g. IDEs.

IF NOT EXIST "%~dp0\\venv" goto :createAndInvoke
goto :invoke

:createAndInvoke
echo First time use detected. Preparing python environment...
cd %~dp0
py -m venv venv
%~dp0\venv\Scripts\activate.bat && pip install -r requirements.txt && echo Environment prepared. && echo. && echo. && python ep.py %*

:invoke
%~dp0\venv\Scripts\activate.bat && python %~dp0\ep.py %*