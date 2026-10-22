# Diseño de despliegue

Este documento define el despliegue objetivo. La aplicación aún no está publicada ni desplegada.

## Render con Docker

Render deberá construir el mismo `Dockerfile` del repositorio, sin depender de `compose.yaml`. El proceso web escuchará en `0.0.0.0` y usará `PORT` cuando Render lo proporcione; `8501` será el valor predeterminado local. El healthcheck será una ruta mínima que no ejecute DSP.

## Persistencia y privacidad

El diseño inicial considera el filesystem de Render efímero: audio de entrada y resultados temporales vivirán solo durante la sesión y se ofrecerá descarga directa. SQLite no se tratará como persistente en producción sin verificar un disco duradero compatible con el plan elegido. Un almacenamiento externo compatible con S3 solo se añadirá si una necesidad real de historial o archivos lo justifica y sus secretos se gestionan mediante variables de entorno.

## Límites de producción

Antes de un despliegue público se fijarán y probarán límites configurables de tamaño, duración, trabajos concurrentes, tiempo máximo, espacio temporal, retención y memoria. La primera versión podrá procesar dentro del contenedor; una cola o worker separado queda fuera hasta demostrar que la concurrencia lo requiere.

## Criterios de salida

La documentación no bastará para cerrar las tareas de Render. Se exigirá una construcción Docker reproducible, arranque en entorno de prueba, healthcheck, procesamiento sintético, descarga, aislamiento entre sesiones y evidencia de los límites observados del servicio elegido. No habrá despliegue automático a producción.
