"""Configuración tipada y validada para la ejecución local."""

from dataclasses import dataclass
import os
from pathlib import Path

from auralith.domain.errors import ConfigurationError


@dataclass(frozen=True, slots=True)
class AppSettings:
    """Límites y opciones operativas obtenidos del entorno."""

    max_input_bytes: int = 500 * 1024 * 1024
    max_duration_seconds: int = 900
    max_concurrency: int = 1
    processing_timeout_seconds: int = 900
    temp_dir: Path = Path("/tmp/auralith")
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "AppSettings":
        """Construye ajustes desde variables `AURALITH_*` o sus valores por defecto."""
        defaults = cls()
        return cls(
            max_input_bytes=_positive_int(
                "AURALITH_MAX_INPUT_BYTES", defaults.max_input_bytes
            ),
            max_duration_seconds=_positive_int(
                "AURALITH_MAX_DURATION_SECONDS", defaults.max_duration_seconds
            ),
            max_concurrency=_positive_int(
                "AURALITH_MAX_CONCURRENCY", defaults.max_concurrency
            ),
            processing_timeout_seconds=_positive_int(
                "AURALITH_PROCESSING_TIMEOUT_SECONDS",
                defaults.processing_timeout_seconds,
            ),
            temp_dir=Path(os.environ.get("AURALITH_TEMP_DIR", defaults.temp_dir)),
            log_level=_log_level(os.environ.get("AURALITH_LOG_LEVEL", defaults.log_level)),
        )


def _positive_int(name: str, default: int) -> int:
    value = os.environ.get(name)
    if value is None:
        return default
    try:
        parsed = int(value)
    except ValueError as error:
        raise ConfigurationError(f"{name} debe ser un entero positivo") from error
    if parsed <= 0:
        raise ConfigurationError(f"{name} debe ser un entero positivo")
    return parsed


def _log_level(value: str) -> str:
    level = value.upper()
    if level not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
        raise ConfigurationError("AURALITH_LOG_LEVEL no es un nivel válido")
    return level