# auralith
Open-source, AI-assisted audio mastering platform powered by Python, DSP, and reference-based processing.

## Estado del proyecto

La planificación y el tablero de trabajo están en [`docs/KANBAN.md`](docs/KANBAN.md). La arquitectura integra Agnara como núcleo de capacidades y define Docker Compose como distribución local y Render como despliegue web objetivo.

- [Roadmap](docs/ROADMAP.md)
- [Arquitectura](docs/ARCHITECTURE.md)
- [Decisiones](docs/DECISIONS.md)
- [Diseño Docker](docs/DOCKER.md)
- [Diseño de despliegue](docs/DEPLOYMENT.md)

Dockerfile, Compose, interfaz y motor de audio aún no están implementados; no se debe interpretar esta documentación como evidencia de funcionamiento.

## Instalación local

La base de desarrollo requiere Python 3.14 o posterior, Git y acceso a Internet para descargar las dependencias. La instalación actual está validada para entornos locales de Linux; la distribución nativa de Windows se documentará en la fase correspondiente.

Desde un checkout limpio:

```bash
git clone https://github.com/Blandskron/auralith.git
cd auralith
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --requirement requirements.lock
python -m pip install --no-deps --editable .
```

En PowerShell, crea y activa el entorno con:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --requirement requirements.lock
python -m pip install --no-deps --editable .
```

La opción `--no-deps` en la instalación editable evita que pip sustituya las versiones fijadas en `requirements.lock`. Para comprobar la instalación y la calidad del checkout:

```bash
python -m compileall -q src tests
ruff check src tests
mypy src
pytest -q
```

El resultado esperado actualmente es una importación correcta, checks de calidad sin errores y cinco pruebas unitarias. Todavía no existe un comando de ejecución de la interfaz: Streamlit, Docker y el motor de audio pertenecen a tareas posteriores del roadmap.
