@echo off

set CDIR=%cd%
cd %cd%\..\ & python -m app.main.src.CommandLine %* & cd %CDIR%