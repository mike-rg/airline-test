# Sistema de Compañía Aérea

Este es un sistema de compañía aérea simple implementado en Python.

## Creación de un Entorno Virtual

Se recomienda el uso de un entorno virtual para evitar conflictos con las dependencias de otros proyectos. Puedes crear un entorno virtual y activarlo con los siguientes comandos:


En la raíz del proyecto
```bash
python -m venv venv
```

En Windows:
```bash
venv\Scripts\activate
```

En macOS/Linux:
```bash
source venv/bin/activate
```

## Instalación de Dependencias

Instala las dependencias del proyecto utilizando pip:
```bash
pip install -r requirements.tx`
```

## Ejecución de Tests

Asegúrate de tener el entorno virtual activado y las dependencias instaladas. Luego, ejecuta los tests utilizando pytest:

```bash
pytest
```

Esto buscará automáticamente los archivos de tests en la carpeta tests/ y los ejecutará.
Estructura de Archivos

    client.py: Contiene la implementación de la clase Client.
    company.py: Contiene la implementación de la clase Company.
    package.py: Contiene la implementación de las clases Package y PackageStatus.
    tests/: Carpeta que contiene los archivos de tests.

### Ejecución de Test con Coverage
Ejecuta tus pruebas con coverage:

```bash
coverage run -m pytest
```
Genera el informe de cobertura:

```bash
coverage report -m
```

Generar un informe HTML más visual, puedes usar:

```bash
coverage html
```

## Análisis estático del código fuente
Ejecitar Análisis
```bash
flake8
```
