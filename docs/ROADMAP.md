# Roadmap de Auralith

## Objetivo

Auralith será una plataforma local, gratuita y open source para masterización musical por referencia. Permitirá analizar una canción propia y una referencia, ejecutar un motor de masterización reemplazable, comparar resultados con volumen igualado y conservar el historial local.

El producto no promete copiar una referencia de forma idéntica. Las métricas acústicas sirven para orientar el procesamiento; la evaluación auditiva y los límites de seguridad siguen siendo necesarios. Tampoco se llamará IA a un algoritmo DSP convencional.

## Principios de entrega

- Desarrollo incremental gobernado por `docs/KANBAN.md`.
- Una sola tarea de implementación en estado `INICIADA` por agente.
- Cada tarea termina únicamente con criterios de aceptación y pruebas documentadas.
- Arquitectura modular, local, Docker First y sin servicios externos obligatorios.
- Procesamiento no destructivo: los originales nunca se modifican.
- Dependencias justificadas por compatibilidad, licencia y valor técnico.

## Fases y hitos

| Fase | Alcance | Hito |
| --- | --- | --- |
| 0 | Investigación, requisitos, arquitectura y calidad | Decisiones documentadas y tablero operativo |
| 1 | Estructura Python, configuración, calidad, CI y documentación | Proyecto instalable y verificable |
| 2 | Validación WAV, Matchering, temporales y exportación WAV | Masterización por referencia desde Python |
| 3 | Aplicación Streamlit y flujo MVP | MVP utilizable en navegador local |
| 4 | Métricas LUFS, RMS, picos, espectro, dinámica y estéreo | Comparación acústica antes/después |
| 5 | DSP modular, objetivos, clipping y regresión acústica | Procesamiento controlable y medible |
| 6 | A/B, igualación, formas de onda, espectrogramas y UX | Flujo de revisión profesional |
| 7 | Recomendaciones explicables y evaluación de ML | Automatización con ventaja medible |
| 8 | SQLite, historial, formatos y lotes | Sesiones persistentes y exportación completa |
| 9 | Seguridad, rendimiento, distribución y versión estable | Primera versión estable local |
| 10 | Integración Agnara | Capacidades declaradas, compiladas, validadas y ejecutadas mediante Agnara |
| 11 | Docker y ejecución local | Compose reproducible, persistencia local y healthcheck |
| 12 | Render y producción | Imagen compartida, límites, privacidad y despliegue documentado |
| 13 | Distribución nativa Windows | Aplicación instalable offline para Windows 10/11, actualizable y desinstalable |

## Orden de ejecución

La fuente de verdad del estado es `docs/KANBAN.md`. Las dependencias impiden comenzar una tarea antes de completar sus prerrequisitos, salvo que el bloqueo quede documentado. Agnara 1.0.3 y Docker pasan a ser restricciones arquitectónicas desde `AUD-007`; Windows queda deliberadamente después de Render y de la estabilización local. No se marcarán tareas de Docker o Windows como terminadas sin pruebas reales. El siguiente trabajo elegible sigue siendo `AUD-007`.
