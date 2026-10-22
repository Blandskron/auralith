# Arquitectura inicial

## Criterios

Auralith será una aplicación monolítica local con separación por capas y un único código de negocio para Compose y Render. Agnara será el núcleo de capacidades y orquestación; Streamlit será un adaptador de entrada, no el lugar donde se decidan las reglas de audio. El motor de masterización se invocará mediante una interfaz para que Matchering pueda sustituirse o complementarse.

## Capas y módulos previstos

```text
Interfaz Streamlit / PySide6 (Windows)
        |
Capacidades Agnara: analizar, comparar, masterizar, exportar, consultar historial
        |
Planes y políticas Agnara
        |
Puertos de aplicación: AudioAnalyzer, MasteringEngine, AudioExporter, ProjectRepository
        |
Dominio: Project, AudioAsset, AnalysisReport, MasteringProfile, ProcessingResult
        |
Adaptadores de infraestructura
  - Audio I/O: SoundFile / FFmpeg
  - DSP y análisis: NumPy, SciPy, librosa, pyloudnorm
        - Orquestación: Agnara 1.0.3 (`Agnara`, `@app.capability`, `ExecutionPlan`)
        - Motor: adaptador Matchering
  - Persistencia: SQLite
  - Observabilidad: logging estructurado y errores de dominio
```

La estructura concreta prevista es `src/auralith/` para producción y `tests/` para pruebas unitarias, de integración y de validación acústica. Los adaptadores previstos son `infrastructure/agnara`, `infrastructure/audio`, `infrastructure/dsp` y `infrastructure/storage`; la interfaz queda en `interface/streamlit`. Los nombres podrán ajustarse durante `AUD-007` si la herramienta de empaquetado elegida lo requiere.

## Contrato de capacidades

Cada capacidad AURALITH se declarará una vez en Agnara y recibirá dependencias DSP por inyección. Las capacidades iniciales serán `audio.analyze`, `audio.compare`, `audio.master` y `audio.export`. La entrada será un esquema validado sin rutas arbitrarias; la salida será un resultado canónico con métricas, artefactos y errores de dominio. Agnara podrá compilar planes y aplicar políticas, pero no contendrá algoritmos DSP.

La integración debe usar únicamente la API pública estable documentada por Agnara 1.0.3. No se importarán módulos internos ni se modificará Agnara para resolver necesidades específicas de AURALITH. Las capacidades se probarán con invocación directa y, cuando corresponda, con el adaptador de transporte; Streamlit solo traducirá interacción de usuario a invocaciones de capacidades.

## Cliente nativo Windows

La distribución Windows tendrá una interfaz PySide6 separada de `application`, `domain` e `infrastructure`. Reutilizará las mismas capacidades Agnara y los mismos puertos DSP que Streamlit, sin duplicar masterización ni análisis. El selector de archivos, accesos directos, configuración de usuario y cierre de procesos serán responsabilidades del adaptador Windows.

La primera ruta de empaquetado seleccionada para validar es PyInstaller + PySide6 + MSIX. PyInstaller permite distribuir aplicaciones no libres mediante su excepción específica; MSIX aporta instalación moderna, aislamiento y actualización, pero exige resolver firma y confianza del certificado. Inno Setup será el EXE de respaldo para GitHub Releases. Nuitka y WebView2 solo podrán sustituir esta ruta si benchmarks, tamaño, licencia y mantenimiento muestran una ventaja verificable.

Si se necesitara WebView2, el servidor local quedaría limitado a loopback, con puerto efímero, token de sesión y cierre garantizado. No se asumirá que Streamlit se convierte directamente en una aplicación nativa.

## Flujo principal

1. La interfaz recibe archivos y parámetros en una sesión aislada.
2. Streamlit invoca la capacidad Agnara correspondiente.
3. Agnara valida entrada, políticas, límites y dependencias antes del plan.
4. Un caso de uso valida formato, tamaño, duración, canales y frecuencia de muestreo.
5. El análisis genera métricas sin modificar los archivos de entrada.
6. El motor recibe rutas temporales controladas y produce un artefacto nuevo.
7. El resultado se valida contra NaN, clipping inesperado, formato y duración.
8. El exportador crea WAV o MP3 dentro del espacio permitido para la sesión.
9. SQLite registra metadatos; nunca almacena audio binario por defecto.

## Límites de responsabilidad

- `ui`: presentación, estado de sesión y mensajes; no DSP.
- `application`: orquestación y políticas de casos de uso.
- `domain`: modelos, contratos y errores independientes de librerías.
- `audio`: lectura, validación, análisis y DSP.
- `infrastructure/agnara`: declaración, compilación y ejecución de capacidades.
- `adapters`: Matchering, FFmpeg, SQLite y Streamlit.
- `interface/windows`: PySide6, lanzador, ciclo de vida y selección de archivos.
- `tests`: señales sintéticas, fixtures autorizadas y pruebas de integración.

## Seguridad y operación

Los nombres de archivo se tratarán como datos, se usarán directorios temporales controlados y se evitará interpolar entradas en comandos de shell. FFmpeg se invocará con argumentos estructurados y se comprobarán códigos de salida. Los temporales se eliminarán en bloques de limpieza incluso ante errores. Los límites de tamaño, duración, concurrencia, tiempo y espacio se aplicarán como política antes de aceptar procesamiento. El contenedor ejecutará con usuario no root y escuchará en `0.0.0.0` usando `PORT` en Render.

## Despliegue

Docker es el mecanismo oficial de distribución. `compose.yaml` ofrecerá el servicio `auralith`, SQLite y resultados en volúmenes persistentes, con temporales separados. Render construirá el mismo `Dockerfile`, sin depender de Compose. En Render se tratará el filesystem como efímero salvo que una tarea de infraestructura confirme un disco persistente apropiado; por defecto los resultados se descargarán directamente y los temporales se limpiarán.

Windows será una distribución adicional, no un fork: incluirá el runtime Python empaquetado, Agnara, DSP y FFmpeg compatible. Los datos de usuario se guardarán bajo directorios apropiados de Windows, separados de la instalación; la desinstalación no borrará proyectos salvo consentimiento explícito.

## Decisiones aún abiertas

La versión exacta de Matchering, la matriz definitiva de versiones de Python, la API de Agnara y la estrategia de empaquetado se validarán contra documentación y pruebas reproducibles antes de `AUD-008`. Agnara 1.0.3 fija un mínimo de Python 3.14, por lo que la imagen base y las dependencias DSP deberán validarse juntas.
