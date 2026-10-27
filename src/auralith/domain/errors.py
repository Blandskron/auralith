"""Errores controlados del dominio de Auralith."""


class AuralithError(Exception):
    """Base para errores que pueden mostrarse como fallos de la aplicación."""


class ConfigurationError(AuralithError, ValueError):
    """La configuración no es válida o no se puede interpretar."""


class InvalidAudioError(AuralithError, ValueError):
    """Una entrada de audio no cumple el contrato del dominio."""


class ProcessingError(AuralithError):
    """El procesamiento no pudo completarse de forma controlada."""


class StorageError(AuralithError):
    """Una operación de almacenamiento no pudo completarse."""