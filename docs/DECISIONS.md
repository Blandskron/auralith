# Registro de decisiones

## ADR-001: aplicación local monolítica

- **Estado:** aceptada.
- **Decisión:** comenzar con una aplicación Python local, sin microservicios ni backend remoto.
- **Motivo:** el objetivo es procesamiento local sin suscripciones, APIs comerciales ni límites artificiales.
- **Consecuencia:** el rendimiento y la gestión de temporales deben probarse dentro de un único proceso.

## ADR-002: Streamlit como interfaz inicial

- **Estado:** aceptada para la primera interfaz.
- **Decisión:** usar Streamlit como adaptador de UI y conservar los casos de uso fuera de sus callbacks.
- **Motivo:** permite validar pronto el flujo de carga, análisis, procesamiento y descarga.
- **Consecuencia:** la lógica no dependerá del estado global de Streamlit.

## ADR-003: Matchering detrás de un puerto

- **Estado:** aceptada.
- **Decisión:** integrar Matchering mediante `MasteringEngine`.
- **Motivo:** es el motor exigido para la primera versión, pero el dominio no debe quedar acoplado a su API.
- **Consecuencia:** las pruebas del dominio usarán dobles y las de integración cubrirán el adaptador real.

## ADR-004: análisis DSP separado de la etiqueta IA

- **Estado:** aceptada.
- **Decisión:** describir como análisis DSP las métricas y transformaciones deterministas; reservar IA para recomendaciones o modelos cuya ventaja se mida.
- **Motivo:** precisión técnica y explicabilidad.

## ADR-005: SQLite para metadatos

- **Estado:** aceptada.
- **Decisión:** almacenar proyectos, configuraciones, métricas e historial en SQLite; conservar audio fuera de la base de datos salvo decisión posterior.
- **Motivo:** persistencia local sin servicio adicional y con respaldo sencillo.

## ADR-006: validar licencias antes de fijar dependencias

- **Estado:** aceptada.
- **Decisión:** no fijar versiones definitivas ni distribuir binarios hasta revisar licencia, compatibilidad Python y redistribución de cada dependencia y FFmpeg.
- **Motivo:** el requisito open source no elimina obligaciones de licencia ni incompatibilidades entre paquetes.

## ADR-007: Agnara como núcleo de capacidades

- **Estado:** aceptada para diseño; integración pendiente.
- **Decisión:** declarar y ejecutar las operaciones AURALITH mediante la API pública de Agnara 1.0.3, manteniendo DSP y audio en adaptadores propios.
- **Evidencia:** la release 1.0.3 documenta `Agnara`, decoradores de capacidad, compilación de capacidades, `ExecutionPlan`, `Invocation` y DI; el núcleo es transport-neutral.
- **Restricción:** Agnara 1.0.3 requiere Python `>=3.14`. No se usarán módulos internos ni se modificará el framework para AURALITH.
- **Consecuencia:** habrá pruebas directas Agnara + DSP y una validación de compatibilidad de Python antes de fijar la imagen.

## ADR-008: Docker First y una imagen compartida

- **Estado:** aceptada para diseño; implementación pendiente.
- **Decisión:** usar un único Dockerfile para Compose local y Render, con usuario no root, FFmpeg, healthcheck y configuración por entorno.
- **Motivo:** reproducibilidad, aislamiento de dependencias y distribución sin instalación local de Python.
- **Consecuencia:** Dockerfile, `.dockerignore`, `compose.yaml`, `.env.example`, CI y documentación son entregables verificables del roadmap.

## ADR-009: Render sin persistencia implícita

- **Estado:** aceptada para diseño; validación de plan pendiente.
- **Decisión:** tratar el filesystem de Render como efímero por defecto; usar temporales para procesamiento y descarga directa de resultados.
- **Motivo:** no asumir que SQLite o archivos generados sobreviven a reinicios/despliegues.
- **Consecuencia:** cualquier persistencia de producción requerirá validar un disco persistente o almacenamiento externo, además de una justificación de coste, privacidad y complejidad.

## ADR-010: cliente nativo Windows y doble distribución

- **Estado:** aceptada para validación; implementación pendiente.
- **Decisión:** evaluar primero PySide6 + PyInstaller empaquetado como MSIX, con Inno Setup como EXE de respaldo para GitHub Releases.
- **Motivo:** PySide6 permite selector y ciclo de vida nativos; PyInstaller tiene una excepción de distribución de aplicaciones no libres; MSIX ofrece instalación y actualización modernas; Inno Setup cubre descargas directas sin exigir Store.
- **Alternativas:** Nuitka queda para benchmark por su impacto de licencia y mantenimiento; WebView2 solo se elegirá si reutilizar la UI web compensa gestionar runtime, loopback y cierre seguro.
- **Consecuencia:** la UI Windows será un adaptador nuevo y compartirá casos de uso, Agnara y DSP con Docker/Render. Una firma autofirmada no se presentará como confianza pública.

## ADR-011: datos de usuario fuera de la instalación

- **Estado:** aceptada para diseño; implementación pendiente.
- **Decisión:** configuración, proyectos, historial y resultados conservados vivirán en rutas de usuario de Windows; el desinstalador no los eliminará por defecto.
- **Motivo:** actualizaciones y desinstalaciones no deben destruir datos personales.
- **Consecuencia:** habrá pruebas de instalación limpia, actualización, desinstalación y reinicio sin pérdida de configuración.

## Investigación INV-001: fotografía de PyPI

- **Fecha de consulta:** 2026-10-22.
- **Fuente:** metadatos JSON públicos de PyPI; no se instalaron paquetes.
- **Resultado:** Matchering `2.0.6` declara GPLv3 y requiere Python `>=3.8`; librosa `1.0.0` declara ISC y requiere `>=3.12`; NumPy `2.5.4` requiere `>=3.12`; SciPy `1.18.1` requiere `>=3.12`; SoundFile `0.14.0` declara BSD 3-Clause y requiere `>=3.10`; pyloudnorm `0.2.0` requiere `>=3.9`; Streamlit `1.66.1` requiere `>=3.11`; pytest `9.1.1` requiere `>=3.10`; Ruff `0.17.1` requiere `>=3.7`.
- **Interpretación:** la base común inmediata de Python debe ser al menos 3.12 para esas versiones consultadas, pero la selección final debe probarse como conjunto. Los campos de licencia ausentes o incompletos en PyPI no sustituyen la revisión de los repositorios y archivos LICENSE.
- **Acción:** `AUD-008` debe fijar una matriz reproducible de versiones y `AUD-066` debe revisar dependencias transitivas, FFmpeg y obligaciones GPL antes de distribuir.

## Investigación INV-002: Agnara y Render

- **Fecha de consulta:** 2026-10-22.
- **Agnara:** `v1.0.3` está publicado en GitHub y PyPI como Apache-2.0, requiere Python `>=3.14`, y separa el núcleo de los transportes HTTP, MCP, CLI y telemetría. La documentación de contenedores indica que Docker no es obligatorio para usar el núcleo, pero sí describe una imagen de referencia independiente.
- **Render:** la documentación Docker exige un proceso web que escuche en `0.0.0.0` y contempla healthchecks y persistent disks; no se asumirá persistencia sin validar el servicio/plan elegido.
- **Riesgo:** la matriz previa de DSP tendrá que comprobarse con Python 3.14 y con FFmpeg dentro de la imagen; la implementación de capacidades y el arranque de Streamlit no se consideran validados por esta investigación.

## Investigación INV-003: distribución nativa Windows

- **Fecha de consulta:** 2026-10-22.
- **Fuentes:** documentación oficial de Microsoft para MSIX, Windows Installer y WebView2; documentación oficial de PyInstaller, Nuitka, Qt for Python, Inno Setup y NSIS; metadatos públicos de PyPI.
- **Hallazgos:** PyInstaller `6.22.3` declara GPLv2-or-later con excepción para distribuir programas no libres y soporta Python `<3.16,>=3.8`; PySide6 `6.12.0` ofrece LGPL-3.0-only/GPL o comercial y soporta Python `<3.16,>=3.10`; Nuitka `4.3.1` declara AGPLv3. MSIX requiere resolver firma/confianza; WebView2 requiere gestionar el runtime Evergreen o Fixed Version.
- **Selección provisional:** PySide6 + PyInstaller + MSIX como ruta primaria; Inno Setup como EXE alternativo. Esta selección no está implementada ni validada en un Windows limpio.
- **Riesgos abiertos:** compatibilidad concreta de Agnara con PyInstaller/PySide6, inclusión legal de FFmpeg, tamaño final, firma de código, actualización entre versiones y pruebas Windows 10/11.
