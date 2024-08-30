@echo off
:: Verificar si el entorno virtual ya existe
if exist .venv (
    echo El entorno virtual ya existe. Activando...
) else (
    echo Creando el entorno virtual...
    python -m venv .venv
    if %ERRORLEVEL% neq 0 (
        echo Error: No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

echo Activando el entorno virtual...
call .venv\Scripts\activate
if %ERRORLEVEL% neq 0 (
    echo Error: No se pudo activar el entorno virtual.
    pause
    exit /b 1
)

:: Verificar si el archivo requirements.txt existe
if not exist .\assets\requirements.txt (
    echo Error: No se encontró el archivo requirements.txt en la carpeta 'assets'.
    deactivate
    pause
    exit /b 1
)

echo Instalando dependencias...
pip install -r .\assets\requirements.txt
if %ERRORLEVEL% neq 0 (
    echo Error: No se pudieron instalar las dependencias.
    deactivate
    pause
    exit /b 1
)

:: Ejecutar el script main.py
echo Ejecutando el script main.py...
python .\main.py
if %ERRORLEVEL% neq 0 (
    echo Error: No se pudo ejecutar main.py.
    deactivate
    pause
    exit /b 1
)

:: Desactivar el entorno virtual
echo Desactivando el entorno virtual...
deactivate

:: Indicar que todo se ejecutó correctamente
echo El entorno virtual ha sido creado, las dependencias han sido instaladas, y el script main.py ha sido ejecutado correctamente.

:: Mantener la ventana abierta
pause
