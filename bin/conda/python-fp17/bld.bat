echo ON

mkdir %SP_DIR%\fp17
if errorlevel 1 exit 1
copy %RECIPE_DIR%\__init__.py %SP_DIR%\fp17\__init__.py
if errorlevel 1 exit 1

echo OFF