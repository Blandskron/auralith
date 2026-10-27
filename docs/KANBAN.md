# Kanban de Auralith

Fuente de verdad del avance. Estados permitidos: `NO INICIADA`, `INICIADA`, `TERMINADA`. Una tarea terminada necesita criterios de aceptación y pruebas o evidencia documentadas.

## Resumen

- Corte: 2026-10-22.
- Total: 116 tareas; `TERMINADA`: 17; `INICIADA`: 0; `NO INICIADA`: 99.
- Avance informativo: 14.7% (`17 / 116`), no esfuerzo completado.
- Bloqueos: ninguno. Siguiente tarea elegible: `AUD-011`.

## Registro

Los campos de cada fila son: ID, título, descripción, fase, prioridad, dependencias, criterios de aceptación verificables, pruebas necesarias, estado, fecha de inicio, fecha de finalización, evidencia y referencia a archivos/commits.

| ID | Título | Descripción | Fase | Prioridad | Dependencias | Criterios de aceptación | Pruebas necesarias | Estado | Inicio | Fin | Evidencia / archivos |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AUD-001 | Investigar tecnologías | Comparar stack de audio, UI, persistencia y calidad. | 0 | Alta | - | Alternativas, riesgos y selección documentados. | Revisión documental. | TERMINADA | 2026-10-22 | 2026-10-22 | `ARCHITECTURE.md`, `DECISIONS.md` |
| AUD-002 | Validar licencias y compatibilidad | Revisar licencias, versiones y restricciones de distribución. | 0 | Alta | AUD-001 | Matriz y condicionantes documentados; no presentar versiones no verificadas como definitivas. | Auditoría documental. | TERMINADA | 2026-10-22 | 2026-10-22 | ADR-006, `ARCHITECTURE.md` |
| AUD-003 | Definir requisitos | Separar requisitos funcionales, no funcionales y límites. | 0 | Alta | AUD-001 | Flujo objetivo, límites y criterios de calidad escritos. | Revisión contra prompt. | TERMINADA | 2026-10-22 | 2026-10-22 | `ROADMAP.md`, `ARCHITECTURE.md` |
| AUD-004 | Diseñar arquitectura | Definir capas, puertos, adaptadores y flujo. | 0 | Alta | AUD-001, AUD-003 | Dominio sin acoplamiento a Streamlit o Matchering. | Revisión de arquitectura. | TERMINADA | 2026-10-22 | 2026-10-22 | `ARCHITECTURE.md` |
| AUD-005 | Crear backlog y Kanban | Registrar tareas, dependencias y criterios. | 0 | Alta | AUD-003, AUD-004 | Las 69 tareas tienen trazabilidad y estado. | Conteo y revisión de tabla. | TERMINADA | 2026-10-22 | 2026-10-22 | `KANBAN.md` |
| AUD-006 | Estrategia de pruebas | Definir pruebas unitarias, integración, audio y seguridad. | 0 | Alta | AUD-003, AUD-004 | Ninguna tarea puede cerrarse sin evidencia de validación. | Revisión de criterios. | TERMINADA | 2026-10-22 | 2026-10-22 | `KANBAN.md`, `ARCHITECTURE.md` |
| AUD-007 | Estructura del proyecto | Crear paquete, tests y configuración base. | 1 | Alta | AUD-001..006 | Importación limpia y estructura documentada. | Smoke de importación. | TERMINADA | 2026-10-22 | 2026-10-22 | `compileall`, importación de capas; pytest pendiente de AUD-008 |
| AUD-008 | Entorno y dependencias | Fijar Python y dependencias reproducibles. | 1 | Alta | AUD-002, AUD-007 | Instalación limpia en entorno nuevo. | Instalación reproducible. | TERMINADA | 2026-10-22 | 2026-10-22 | `pyproject.toml`, `requirements.lock`; venv Python 3.14, pytest 1 passed |
| AUD-009 | Configuración, logs y errores | Añadir configuración tipada y errores de dominio. | 1 | Alta | AUD-007 | Errores controlados y logs sin datos sensibles. | Unitarias. | TERMINADA | 2026-10-27 | 2026-10-27 | `src/auralith/config/settings.py`, `src/auralith/config/logging.py`, `src/auralith/domain/errors.py`, `tests/unit/test_settings.py`; pytest |
| AUD-010 | Lint, tipos y pruebas | Configurar Ruff, tipado estático y pytest. | 1 | Alta | AUD-007, AUD-008 | Checks reproducibles sin errores. | Ruff, typecheck, pytest. | TERMINADA | 2026-10-27 | 2026-10-27 | `pyproject.toml`; `ruff check src tests`, `mypy src`, `pytest -q` |
| AUD-011 | CI | Automatizar calidad con GitHub Actions. | 1 | Media | AUD-010 | Workflow ejecuta los checks. | Ejecución CI. | NO INICIADA | - | - | - |
| AUD-012 | Instalación | Documentar preparación y ejecución local. | 1 | Media | AUD-008, AUD-011 | Usuario puede instalar desde cero. | Seguir README. | NO INICIADA | - | - | - |
| AUD-013 | Validación WAV | Validar entradas WAV seguras. | 2 | Alta | AUD-008..010 | Rechaza corruptos y límites; acepta formatos soportados. | Formato y límites. | NO INICIADA | - | - | - |
| AUD-014 | Adaptador Matchering | Integrar el motor detrás de contrato. | 2 | Alta | AUD-002, AUD-013 | Adaptador invocable y aislado. | Fixture autorizado. | NO INICIADA | - | - | - |
| AUD-015 | Procesamiento por referencia | Orquestar fuente y referencia. | 2 | Alta | AUD-014 | Produce salida nueva sin tocar entradas. | Integración. | NO INICIADA | - | - | - |
| AUD-016 | WAV 24 bits | Exportar master PCM validado. | 2 | Alta | AUD-015 | Profundidad, duración y canales correctos. | Inspección SoundFile. | NO INICIADA | - | - | - |
| AUD-017 | Temporales y errores | Gestionar fallos y limpieza. | 2 | Alta | AUD-015 | Limpieza en éxito y error. | Excepciones y filesystem. | NO INICIADA | - | - | - |
| AUD-018 | Pruebas de masterización | Cubrir flujo completo del motor. | 2 | Alta | AUD-013..017 | Flujo sintético reproducible y sin clipping inesperado. | Integración y numéricas. | NO INICIADA | - | - | - |
| AUD-019 | Aplicación Streamlit | Crear punto de entrada de UI. | 3 | Alta | AUD-018 | Arranque local correcto. | Smoke de arranque. | NO INICIADA | - | - | - |
| AUD-020 | Cargar canción propia | Incorporar archivo fuente. | 3 | Alta | AUD-019 | Carga y validación visibles. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-021 | Cargar referencia | Incorporar archivo de referencia. | 3 | Alta | AUD-019 | Referencia validada de forma independiente. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-022 | Metadatos y validaciones | Mostrar información y errores. | 3 | Media | AUD-020, AUD-021 | Mensajes accionables. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-023 | Controles de proceso | Exponer parámetros permitidos. | 3 | Alta | AUD-019 | Parámetros llegan al caso de uso. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-024 | Progreso y errores | Mostrar estado de procesamiento. | 3 | Media | AUD-023 | Fallos no dejan estado inconsistente. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-025 | Descargar resultado | Permitir descarga del master. | 3 | Alta | AUD-016, AUD-024 | Archivo descargado íntegro. | Integración UI. | NO INICIADA | - | - | - |
| AUD-026 | LUFS | Medir loudness integrado y short-term. | 4 | Alta | AUD-013 | Valores finitos y unidades documentadas. | Señales sintéticas. | NO INICIADA | - | - | - |
| AUD-027 | RMS y picos | Medir nivel, pico y clipping. | 4 | Alta | AUD-013 | Detecta silencio y clipping. | Pruebas numéricas. | NO INICIADA | - | - | - |
| AUD-028 | Espectro | Obtener respuesta de frecuencia. | 4 | Media | AUD-013 | Frecuencia y magnitud reproducibles. | Tonos sintéticos. | NO INICIADA | - | - | - |
| AUD-029 | Rango dinámico | Estimar dinámica con método explícito. | 4 | Media | AUD-026, AUD-027 | Método y limitaciones visibles. | Señales dinámicas. | NO INICIADA | - | - | - |
| AUD-030 | Imagen estéreo | Medir correlación y anchura. | 4 | Media | AUD-013 | Mono y estéreo diferenciables. | Señales de fase. | NO INICIADA | - | - | - |
| AUD-031 | Comparar características | Comparar fuente y referencia. | 4 | Alta | AUD-026..030 | Informe con diferencias y unidades. | Unitarias. | NO INICIADA | - | - | - |
| AUD-032 | Métricas antes/después | Exponer cambios del master. | 4 | Alta | AUD-031, AUD-018 | Sin NaN y sin modificar entradas. | Integración. | NO INICIADA | - | - | - |
| AUD-033 | EQ paramétrica | Añadir EQ modular. | 5 | Media | AUD-032 | Respuesta y límites validados. | Impulso y regresión. | NO INICIADA | - | - | - |
| AUD-034 | Procesamiento dinámico | Añadir dinámica configurable. | 5 | Media | AUD-032 | Ganancia y estabilidad controladas. | Señales sintéticas. | NO INICIADA | - | - | - |
| AUD-035 | Compresión multibanda | Evaluar e implementar si aporta valor. | 5 | Baja | AUD-034 | Beneficio medible y artefactos controlados. | Regresión acústica. | NO INICIADA | - | - | - |
| AUD-036 | Imagen estéreo DSP | Ajustar anchura con límites. | 5 | Media | AUD-030, AUD-032 | Sin clipping ni fase peligrosa por defecto. | Señales de fase. | NO INICIADA | - | - | - |
| AUD-037 | Limitación true peak | Limitar picos inter-sample. | 5 | Alta | AUD-032 | Objetivo respetado dentro de tolerancia. | Medición true peak. | NO INICIADA | - | - | - |
| AUD-038 | Objetivo LUFS | Normalizar a objetivo configurable. | 5 | Alta | AUD-026, AUD-037 | Tolerancia documentada. | Señales calibradas. | NO INICIADA | - | - | - |
| AUD-039 | Perfiles DSP | Crear perfiles reproducibles. | 5 | Media | AUD-033, AUD-034 | Serialización validada. | Unitarias. | NO INICIADA | - | - | - |
| AUD-040 | Protección contra clipping | Proteger toda la cadena. | 5 | Alta | AUD-033..038 | Sin clipping no intencional. | Casos extremos. | NO INICIADA | - | - | - |
| AUD-041 | Regresión acústica | Congelar invariantes medibles. | 5 | Alta | AUD-040 | Suite reproducible con tolerancias. | Suite acústica. | NO INICIADA | - | - | - |
| AUD-042 | Reproductor A/B | Comparar original y master. | 6 | Alta | AUD-025 | Cambio A/B sin alterar archivos. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-043 | Igualación percibida | Igualar loudness de comparación. | 6 | Alta | AUD-026, AUD-042 | Objetivo y diferencia documentados. | Medición LUFS. | NO INICIADA | - | - | - |
| AUD-044 | Formas de onda | Visualizar señal. | 6 | Media | AUD-019 | Render estable mono/estéreo. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-045 | Espectrogramas | Visualizar espectro temporal. | 6 | Media | AUD-028, AUD-019 | Escalas y unidades claras. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-046 | Panel comparativo | Unificar métricas. | 6 | Alta | AUD-032, AUD-043 | Comparación legible y consistente. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-047 | Presets musicales | Añadir perfiles editables. | 6 | Baja | AUD-039 | Presets explícitos y editables. | Unitarias/UI. | NO INICIADA | - | - | - |
| AUD-048 | UX y accesibilidad | Mejorar navegación y mensajes. | 6 | Media | AUD-046 | Flujo usable y errores claros. | Revisión manual. | NO INICIADA | - | - | - |
| AUD-049 | Investigar recomendaciones | Comparar heurísticas y ML. | 7 | Media | AUD-031, AUD-046 | Alternativas y baseline definidos. | Informe técnico. | NO INICIADA | - | - | - |
| AUD-050 | Diferencias automáticas | Detectar diferencias relevantes. | 7 | Media | AUD-049 | Detección reproducible y explicable. | Dataset sintético. | NO INICIADA | - | - | - |
| AUD-051 | Recomendaciones explicables | Asociar métrica, acción y riesgo. | 7 | Media | AUD-050 | Cada recomendación tiene justificación. | Unitarias. | NO INICIADA | - | - | - |
| AUD-052 | Selección automática | Proponer configuración. | 7 | Baja | AUD-051 | Supera baseline o se rechaza. | Evaluación objetiva. | NO INICIADA | - | - | - |
| AUD-053 | Evaluar ML open source | Medir utilidad de modelos. | 7 | Baja | AUD-049 | Decisión basada en métricas y coste. | Benchmark. | NO INICIADA | - | - | - |
| AUD-054 | Comparar resultados inteligentes | Comparar contra baseline. | 7 | Media | AUD-052, AUD-053 | Informe reproducible. | Evaluación acústica. | NO INICIADA | - | - | - |
| AUD-055 | Controles manuales | Aceptar o modificar sugerencias. | 7 | Media | AUD-051, AUD-054 | Usuario puede anular cada sugerencia. | Prueba UI. | NO INICIADA | - | - | - |
| AUD-056 | Base SQLite | Implementar esquema local. | 8 | Alta | AUD-009, AUD-057 | Migración reproducible. | Integración DB. | NO INICIADA | - | - | - |
| AUD-057 | Configuraciones y sesiones | Guardar estado de proyectos. | 8 | Alta | AUD-056 | Lectura y escritura consistentes. | Integración DB. | NO INICIADA | - | - | - |
| AUD-058 | Historial | Consultar masterizaciones previas. | 8 | Media | AUD-057 | Historial ordenado y filtrable. | Integración DB. | NO INICIADA | - | - | - |
| AUD-059 | WAV 16/24 bits | Exportar profundidades soportadas. | 8 | Alta | AUD-016 | Bits y metadatos correctos. | Inspección de archivos. | NO INICIADA | - | - | - |
| AUD-060 | MP3 320 kbps | Exportar con herramienta compatible. | 8 | Media | AUD-002, AUD-059 | Bitrate verificado y errores controlados. | Integración FFmpeg. | NO INICIADA | - | - | - |
| AUD-061 | Procesamiento por lotes | Procesar varios proyectos aislados. | 8 | Baja | AUD-017, AUD-058 | Error de un elemento no corrompe los demás. | Integración. | NO INICIADA | - | - | - |
| AUD-062 | Integración completa | Ejecutar flujos de extremo a extremo. | 9 | Alta | AUD-019..061 | Suite completa reproducible. | CI y local. | NO INICIADA | - | - | - |
| AUD-063 | Rendimiento y memoria | Medir recursos y duración. | 9 | Media | AUD-062 | Umbrales documentados y cumplidos. | Benchmark. | NO INICIADA | - | - | - |
| AUD-064 | Entradas corruptas/maliciosas | Probar robustez de entradas. | 9 | Alta | AUD-013, AUD-017 | Sin ejecución arbitraria ni bloqueos. | Seguridad. | NO INICIADA | - | - | - |
| AUD-065 | Limpieza segura | Revisar temporales y permisos. | 9 | Alta | AUD-017, AUD-064 | Temporales aislados y eliminados. | Filesystem. | NO INICIADA | - | - | - |
| AUD-066 | Licencias y atribuciones | Revisar distribución final. | 9 | Alta | AUD-002, AUD-060 | Inventario y avisos completos. | Auditoría documental. | NO INICIADA | - | - | - |
| AUD-067 | Distribución local | Crear instalador o paquete ejecutable. | 9 | Media | AUD-012, AUD-063, AUD-066 | Instalación limpia reproducible. | Smoke en entorno limpio. | NO INICIADA | - | - | - |
| AUD-068 | Manual de usuario y técnica | Completar documentación. | 9 | Media | AUD-048, AUD-061 | Flujos y límites documentados. | Revisión documental. | NO INICIADA | - | - | - |
| AUD-069 | Primera versión estable | Cerrar checklist de release. | 9 | Alta | AUD-062..068 | Checklist y artefactos verificables. | Suite final. | NO INICIADA | - | - | - |

## Fase 10 - Integración Agnara

| ID | Título | Descripción | Fase | Prioridad | Dependencias | Criterios de aceptación | Pruebas necesarias | Estado | Inicio | Fin | Evidencia / archivos |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AUD-070 | Investigar Agnara 1.0.3 | Revisar API pública, ejemplos, límites y licencia. | 10 | Alta | AUD-001, AUD-002 | API, Python mínimo, superficies y restricciones documentados desde fuentes primarias. | Revisión de release, PyPI y ejemplos. | TERMINADA | 2026-10-22 | 2026-10-22 | `DECISIONS.md` INV-002 |
| AUD-071 | Diseñar capacidades AURALITH | Mapear análisis, comparación, masterización y exportación a capacidades. | 10 | Alta | AUD-004, AUD-070 | Contratos, entradas/salidas y separación DSP/orquestación documentados. | Revisión arquitectónica. | TERMINADA | 2026-10-22 | 2026-10-22 | `ARCHITECTURE.md` |
| AUD-072 | Registrar y ejecutar capacidades | Implementar declaración, compilación, DI e invocación Agnara. | 10 | Alta | AUD-007, AUD-008, AUD-071 | Capacidades compiladas e invocables por API pública. | Unitarias y smoke Agnara. | NO INICIADA | - | - | - |
| AUD-073 | Integrar Matchering mediante Agnara | Conectar el motor existente como dependencia de una capacidad. | 10 | Alta | AUD-014, AUD-072 | Streamlit no importa ni ejecuta DSP directamente. | Integración Agnara + Matchering. | NO INICIADA | - | - | - |
| AUD-074 | Validaciones y políticas Agnara | Aplicar límites, autorización, errores y controles de operación. | 10 | Alta | AUD-009, AUD-072 | Entradas inválidas y operaciones fuera de límites son rechazadas. | Casos de política y seguridad. | NO INICIADA | - | - | - |
| AUD-075 | Pruebas Agnara + DSP | Cubrir capacidades con señales sintéticas. | 10 | Alta | AUD-072..074, AUD-018 | Resultados, errores y contratos son reproducibles. | Unitarias e integración. | NO INICIADA | - | - | - |
| AUD-076 | Documentar arquitectura Agnara | Registrar API usada, límites y no modificaciones al framework. | 10 | Media | AUD-070, AUD-071 | Documentación coincide con implementación y fuentes públicas. | Revisión documental. | TERMINADA | 2026-10-22 | 2026-10-22 | `ARCHITECTURE.md`, `DECISIONS.md` |

## Fase 11 - Docker y ejecución local

| ID | Título | Descripción | Fase | Prioridad | Dependencias | Criterios de aceptación | Pruebas necesarias | Estado | Inicio | Fin | Evidencia / archivos |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AUD-077 | Compatibilidad Linux en contenedor | Validar Python 3.14, Agnara, DSP y FFmpeg. | 11 | Alta | AUD-008, AUD-070 | Matriz instalada y reproducible en imagen Linux. | Build e importación. | NO INICIADA | - | - | - |
| AUD-078 | Crear Dockerfile | Crear una imagen multi-stage mantenible y mínima. | 11 | Alta | AUD-077 | Imagen construye desde checkout limpio, sin secretos ni audio. | `docker build`. | NO INICIADA | - | - | - |
| AUD-079 | Crear .dockerignore | Excluir caches, Git, secretos, audio, DB y resultados. | 11 | Alta | AUD-078 | Contexto no incluye rutas prohibidas y sí incluye archivos requeridos. | Inspección de contexto. | NO INICIADA | - | - | - |
| AUD-080 | Crear compose.yaml | Definir servicio `auralith` y puerto 8501. | 11 | Alta | AUD-078, AUD-079 | `docker compose up -d --build` arranca sin configuración obligatoria. | Arranque Compose. | NO INICIADA | - | - | - |
| AUD-081 | Volúmenes persistentes | Separar configuración, SQLite, historial, resultados y temporales. | 11 | Alta | AUD-080 | Reinicio/rebuild conserva datos permitidos y no temporales. | Prueba de persistencia. | NO INICIADA | - | - | - |
| AUD-082 | Variables de entorno | Crear `.env.example` con valores seguros y límites. | 11 | Alta | AUD-080 | Configuración documentada sin secretos en Git. | Arranque con defaults y overrides. | NO INICIADA | - | - | - |
| AUD-083 | Healthcheck | Implementar endpoint y healthcheck de contenedor. | 11 | Alta | AUD-080 | Estado saludable se detecta sin ejecutar DSP. | `docker inspect` y HTTP. | NO INICIADA | - | - | - |
| AUD-084 | Usuario no root | Ejecutar proceso con UID no privilegiado. | 11 | Alta | AUD-078 | UID efectivo no es root y puede escribir solo en rutas previstas. | Inspección y smoke. | NO INICIADA | - | - | - |
| AUD-085 | Límites de recursos | Configurar tamaño, duración, concurrencia, timeout y espacio. | 11 | Alta | AUD-074, AUD-080 | Excesos se rechazan o terminan controladamente. | Casos de límite. | NO INICIADA | - | - | - |
| AUD-086 | Instalación desde repositorio limpio | Validar clone, build y arranque sin archivos locales. | 11 | Alta | AUD-078..085 | Flujo oficial funciona con los tres comandos documentados. | Smoke limpio. | NO INICIADA | - | - | - |
| AUD-087 | Docker Desktop y Engine | Probar Linux, Windows y macOS con Docker. | 11 | Media | AUD-086 | Diferencias, requisitos y resultados documentados. | Matriz multiplataforma. | NO INICIADA | - | - | - |
| AUD-088 | Documentación local Docker | Completar instalación, uso, persistencia y troubleshooting. | 11 | Media | AUD-086, AUD-087 | Usuario puede ejecutar modalidad local sin Python instalado. | Revisión siguiendo `DOCKER.md`. | NO INICIADA | - | - | - |

## Fase 12 - Render y producción

| ID | Título | Descripción | Fase | Prioridad | Dependencias | Criterios de aceptación | Pruebas necesarias | Estado | Inicio | Fin | Evidencia / archivos |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AUD-089 | Investigar requisitos Render | Revisar Docker web service, plan, healthcheck y persistencia vigente. | 12 | Alta | AUD-070, AUD-077 | Fuente, límites y plan elegido documentados; no asumir filesystem persistente. | Revisión documental y smoke de plataforma. | TERMINADA | 2026-10-22 | 2026-10-22 | `DECISIONS.md` INV-002, `DEPLOYMENT.md` |
| AUD-090 | Puerto dinámico | Configurar `PORT` y bind `0.0.0.0`, con 8501 local. | 12 | Alta | AUD-083, AUD-089 | Servicio arranca con puerto inyectado y default local. | Arranque con variables. | NO INICIADA | - | - | - |
| AUD-091 | Build de producción | Validar la misma imagen Docker en Render. | 12 | Alta | AUD-086, AUD-089 | Build y arranque no dependen de Compose. | Build de servicio. | NO INICIADA | - | - | - |
| AUD-092 | Estrategia de almacenamiento | Resolver temporales, descargas y persistencia opcional. | 12 | Alta | AUD-081, AUD-089 | No se pierde información prometida; SQLite no se usa sin disco duradero validado. | Reinicio y descarga. | NO INICIADA | - | - | - |
| AUD-093 | Límites de producción | Aplicar recursos, concurrencia, timeout y retención. | 12 | Alta | AUD-085, AUD-091 | Procesamiento excesivo no bloquea indefinidamente el servicio. | Carga y timeout. | NO INICIADA | - | - | - |
| AUD-094 | Protección contra abuso | Aislar sesiones y restringir entradas públicas. | 12 | Alta | AUD-074, AUD-093 | Sin path traversal, acceso cruzado ni consumo ilimitado. | Seguridad y fuzzing. | NO INICIADA | - | - | - |
| AUD-095 | Despliegue de prueba | Validar servicio en entorno Render no productivo. | 12 | Alta | AUD-090..094 | Healthcheck, masterización sintética y limpieza funcionan. | Smoke remoto. | NO INICIADA | - | - | - |
| AUD-096 | Documentación Render | Documentar configuración, límites, privacidad y rollback manual. | 12 | Media | AUD-092, AUD-095 | Guía reproducible y sin secretos. | Revisión documental. | NO INICIADA | - | - | - |
| AUD-097 | Acceso web y descarga | Validar flujo público de carga, procesamiento y descarga. | 12 | Alta | AUD-095, AUD-096 | Usuario puede completar el flujo sin exponer archivos ajenos. | Prueba web de extremo a extremo. | NO INICIADA | - | - | - |
| AUD-098 | CI de calidad, imagen y seguridad | Ampliar GitHub Actions con tests Agnara, Docker, healthcheck y escaneos. | 12 | Alta | AUD-075, AUD-083, AUD-086 | CI ejecuta checks sin publicar imágenes ni desplegar producción. | pytest, build, smoke y scanner. | NO INICIADA | - | - | - |

## Fase 13 - Distribución nativa Windows

Esta fase solo puede comenzar después de estabilizar las modalidades Docker local y Render. Los artefactos estables requieren autorización explícita para publicarse.

| ID | Título | Descripción | Fase | Prioridad | Dependencias | Criterios de aceptación | Pruebas necesarias | Estado | Inicio | Fin | Evidencia / archivos |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AUD-099 | Investigar empaquetadores Python Windows | Comparar PyInstaller y Nuitka, tamaño, runtime, imports y licencias. | 13 | Alta | AUD-002, AUD-069, AUD-098 | Selección documentada con fuentes y riesgos reproducibles. | Pruebas de empaquetado de muestra. | TERMINADA | 2026-10-22 | 2026-10-22 | `WINDOWS.md`, `DECISIONS.md` INV-003 |
| AUD-100 | Investigar MSIX, MSI y EXE | Comparar distribución, firma, actualización y mantenimiento. | 13 | Alta | AUD-099 | MSIX, MSI y EXE tienen decisión y alternativa documentadas. | Revisión de documentación oficial. | TERMINADA | 2026-10-22 | 2026-10-22 | `WINDOWS.md`, `DECISIONS.md` INV-003 |
| AUD-101 | Comparar UI nativa y WebView2 | Evaluar PySide6/Qt frente a WebView2 con servidor local. | 13 | Alta | AUD-019, AUD-099 | Se documentan compatibilidad, licencia, tamaño, loopback y cierre. | Prototipos comparables posteriores. | TERMINADA | 2026-10-22 | 2026-10-22 | `WINDOWS.md`, `ARCHITECTURE.md` |
| AUD-102 | Diseñar arquitectura de escritorio | Separar interfaz Windows de capacidades Agnara y DSP. | 13 | Alta | AUD-071, AUD-099..101 | Mismo dominio y motor que Docker/Render; sin DSP duplicado. | Revisión arquitectónica. | TERMINADA | 2026-10-22 | 2026-10-22 | `ARCHITECTURE.md`, `DECISIONS.md` |
| AUD-103 | Implementar lanzador AURALITH | Crear ciclo de vida, inicio, cierre y errores de la app Windows. | 13 | Alta | AUD-007, AUD-072, AUD-102 | Arranca sin terminal visible y cierra recursos correctamente. | Smoke en Windows 10/11. | NO INICIADA | - | - | - |
| AUD-104 | Empaquetar Agnara y DSP | Incluir capacidades, dependencias Python y motor común. | 13 | Alta | AUD-075, AUD-099, AUD-103 | La aplicación instalada invoca Agnara y procesa señales sintéticas. | Integración empaquetada. | NO INICIADA | - | - | - |
| AUD-105 | Empaquetar nativas y FFmpeg | Incluir DLLs, librerías y FFmpeg legalmente compatible. | 13 | Alta | AUD-002, AUD-077, AUD-104 | No requiere instalaciones externas y el inventario legal está completo. | Arranque limpio y auditoría de artefactos. | NO INICIADA | - | - | - |
| AUD-106 | Implementar almacenamiento local | Guardar configuración y proyectos en rutas de usuario Windows. | 13 | Alta | AUD-056, AUD-102 | Reinicio conserva configuración; instalación y datos están separados. | Escritura, reinicio y permisos. | NO INICIADA | - | - | - |
| AUD-107 | Crear instalador Windows | Generar MSIX y EXE alternativo con accesos directos y menú Inicio. | 13 | Alta | AUD-103..106 | Instala sin Python/Docker/Git/FFmpeg externos. | Instalación en Windows limpio. | NO INICIADA | - | - | - |
| AUD-108 | Implementar desinstalación | Eliminar aplicación sin borrar datos personales por defecto. | 13 | Alta | AUD-106, AUD-107 | Desinstalación completa y datos conservados según política. | Instalar, guardar, desinstalar y verificar. | NO INICIADA | - | - | - |
| AUD-109 | Versionado y actualización | Añadir SemVer, integridad y actualización segura. | 13 | Alta | AUD-107, AUD-108 | Actualización entre versiones conserva configuración y rechaza artefactos alterados. | Upgrade/downgrade controlado. | NO INICIADA | - | - | - |
| AUD-110 | Evaluar firma de código | Documentar certificados, costes, renovación y confianza. | 13 | Alta | AUD-100, AUD-107 | Firma pública diferenciada de autofirma y verificación automatizada. | Validación de firma. | NO INICIADA | - | - | - |
| AUD-111 | Automatizar builds Windows | Crear workflow con runners Windows y artefactos de prueba. | 13 | Alta | AUD-010, AUD-098, AUD-107 | CI construye y valida instaladores sin publicar estable automáticamente. | GitHub Actions Windows. | NO INICIADA | - | - | - |
| AUD-112 | Probar Windows 10/11 | Ejecutar instalación, uso, actualización y desinstalación en ambas versiones. | 13 | Alta | AUD-107..111 | Criterios funcionales pasan en Windows 10 y 11 limpios. | Matriz Windows 10/11. | NO INICIADA | - | - | - |
| AUD-113 | Validar ausencia de Python y Docker | Confirmar ejecución en equipo sin runtimes externos. | 13 | Alta | AUD-112 | App opera sin Python, Docker, Git ni FFmpeg instalado aparte. | Máquina limpia. | NO INICIADA | - | - | - |
| AUD-114 | Probar operación offline | Validar flujo completo sin internet tras instalar. | 13 | Alta | AUD-104, AUD-105, AUD-112 | Carga, masterización, A/B y exportación funcionan offline. | Desconexión de red. | NO INICIADA | - | - | - |
| AUD-115 | Documentar usuario Windows | Preparar guía de instalación, privacidad, uso y recuperación. | 13 | Media | AUD-108, AUD-109, AUD-112 | Manual reproducible para usuarios sin herramientas técnicas. | Revisión siguiendo manual. | NO INICIADA | - | - | - |
| AUD-116 | Candidata Windows autorizada | Preparar release candidate y publicación autorizada en GitHub Releases/WinGet. | 13 | Alta | AUD-109..115 | Checklist final completo y autorización explícita antes de publicar. | Validación final de release. | NO INICIADA | - | - | - |

## Política de actualización

Al comenzar una sesión se revisan las filas `INICIADA`, bloqueos y dependencias. Solo se cambia a `TERMINADA` después de ejecutar las pruebas indicadas y registrar evidencia. Las referencias a commits se añadirán cuando existan commits posteriores; este ciclo no crea commits.
