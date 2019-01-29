echo ON

scons py --prefix=%LIBRARY_PREFIX% -j%CPU_COUNT% --package=fp17
if errorlevel 1 exit 1

echo OFF