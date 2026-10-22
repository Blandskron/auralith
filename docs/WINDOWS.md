# Diseño de distribución Windows

Este documento describe la fase final. No demuestra todavía una instalación funcional.

## Comparación

| Opción | Ventajas | Riesgos o costes | Decisión |
| --- | --- | --- | --- |
| MSIX | Instalación moderna, identidad de paquete, actualizaciones y desinstalación limpias | Firma y confianza del certificado; restricciones de escritura y distribución | Primaria, después de validar firma |
| MSI | Integración tradicional con Windows Installer y despliegues administrados | Más complejo de mantener; no resuelve por sí solo empaquetado Python | No será primera ruta |
| EXE + Inno Setup | Descarga directa sencilla, accesos directos y control del instalador | Actualizaciones y firma deben diseñarse aparte | Respaldo para GitHub Releases |
| EXE + NSIS | Ligero y flexible | Más trabajo de integración y mantenimiento del script | No seleccionado inicialmente |
| PyInstaller | Empaquetado probado y excepción de distribución para aplicaciones no libres | Tamaño, análisis de imports y datos nativos | Primera herramienta a validar |
| Nuitka | Compilación y posibles mejoras de distribución/rendimiento | AGPLv3 declarada y mayor complejidad de build/licencia | Benchmark opcional |
| PySide6/Qt | UI nativa, selector de archivos y ciclo de vida controlables | Licencia LGPL/GPL/comercial y tamaño de Qt | Interfaz primaria |
| WebView2 | Reutiliza una UI web existente | Runtime, exposición loopback, puertos y cierre seguro | Solo si benchmark lo justifica |

## Ruta seleccionada

La primera prueba de concepto usará PySide6 con llamadas a los casos de uso de Agnara, sin lógica DSP en la UI. PyInstaller empaquetará Python, Agnara, DSP y FFmpeg compatible. El artefacto primario será MSIX una vez resueltos certificado e instalación; Inno Setup será el artefacto EXE alternativo para usuarios que descarguen desde GitHub Releases.

## Requisitos de aceptación

La fase no termina con un build. Un Windows 10/11 limpio debe instalar, iniciar desde el menú Inicio, cargar fuente y referencia, ejecutar Agnara/DSP, reproducir A/B, exportar WAV/MP3, cerrar liberando recursos, conservar configuración, actualizar y desinstalar sin borrar datos personales.

La firma autofirmada solo servirá para pruebas controladas. Para distribución pública se documentarán certificado, proveedor, coste, renovación y verificación de integridad. Las versiones estables se publicarán mediante una acción autorizada, no automáticamente.
