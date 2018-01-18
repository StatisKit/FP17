echo ON

set PY2K=2.7
set PY3K=3.6

:: activate
:: if errorlevel 1 exit 1
rmdir %CONDA_PREFIX%\conda-bld /S /q

cd ..\..\conda
if errorlevel 1 exit 1
conda build fp17 --python=%PY2K%
if errorlevel 1 exit 1
conda build fp17 --python=%PY3K%
if errorlevel 1 exit 1

cd ..\script\win
if errorlevel 1 exit 1

echo OFF