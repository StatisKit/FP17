echo ON

activate
if errorlevel 1 exit 1
rmdir ${CONDA_PREFIX}/conda-bld/win-64 /S /q
if errorlevel 1 exit 1

git clone --recursive http://github.com/StatisKit/FP17
if errorlevel 1 exit 1

cd FP17\bin\conda
if errorlevel 1 exit 1
conda build fp17
if errorlevel 1 exit 1

cd ..\..\..

echo OFF
