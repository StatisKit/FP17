echo ON

for %%i in ("%CONDA_PREFIX%\conda-bld\win-64\*.tar.bz2") do (
    anaconda upload %%i -u %ANACONDA_UPLOAD% --label win-x86_64_release
    if errorlevel 1 exit 1
)

echo OFF
