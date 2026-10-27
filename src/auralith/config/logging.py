"""Configuración centralizada de logs sin datos de entrada."""

import logging


def configure_logging(level: str = "INFO") -> None:
    """Configura un formato estable; los llamadores no deben incluir datos sensibles."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        force=True,
    )


def get_logger(name: str) -> logging.Logger:
    """Obtiene un logger para un módulo de Auralith."""
    return logging.getLogger(name)