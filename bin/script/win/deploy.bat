echo ON

:: activate
:: if errorlevel 1 exit 1

rmdir %CONDA_PREFIX%\conda-bld\src_cache /S /q
rmdir %CONDA_PREFIX%\conda-bld\broken /S /q

for /R %%i in ("%CONDA_PREFIX%\conda-bld\*.tar.bz2") do (
    anaconda upload %%i -u %ANACONDA_UPLOAD% --label win-release
    if errorlevel 1 exit 1
)

echo OFF
