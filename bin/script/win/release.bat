echo ON

activate
if errorlevel 1 exit 1
rmdir %CONDA_PREFIX%conda-bld /S /q
if errorlevel 1 exit 1

cd ..\..\conda
if errorlevel 1 exit 1
conda build fp17
if errorlevel 1 exit 1

cd ..\script\win
if errorlevel 1 exit 1

echo OFF