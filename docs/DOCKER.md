# Diseño Docker

Este documento define el comportamiento esperado antes de implementar Docker. No es evidencia de que la imagen exista o haya sido probada.

## Contrato local

La ejecución oficial será:

```text
docker compose up -d --build
```

El servicio se llamará `auralith` y expondrá `http://localhost:8501` por defecto. `compose.yaml` deberá montar volúmenes separados para datos SQLite/configuración, resultados conservados y temporales. Los temporales tendrán limpieza por política y no se reutilizarán entre sesiones.

## Imagen

El único `Dockerfile` deberá usar una imagen oficial compatible con Python 3.14 y Agnara 1.0.3, instalar FFmpeg y solo dependencias necesarias, aprovechar el caché de capas, ejecutar como usuario no root y no copiar secretos, audios, bases de datos ni resultados. Deberá declarar `PORT`, exponer el puerto efectivo y tener un healthcheck que no dependa de una ruta local del desarrollador.

## Configuración

`.env.example` documentará valores seguros para puerto, límites de tamaño/duración, concurrencia, timeout, retención, rutas internas y nivel de logs. Los valores sensibles no se incluirán en el repositorio.

## Verificación obligatoria

Una tarea Docker solo podrá pasar a `TERMINADA` con evidencia de construcción desde un checkout limpio, arranque, healthcheck, procesamiento sintético, persistencia tras reinicio y limpieza de temporales. También se documentarán límites conocidos de Docker Desktop en Windows y macOS frente a Docker Engine en Linux.
