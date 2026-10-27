import pytest

from auralith.config.settings import AppSettings
from auralith.domain.errors import ConfigurationError, InvalidAudioError, AuralithError


def test_settings_read_valid_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AURALITH_MAX_CONCURRENCY", "3")
    monkeypatch.setenv("AURALITH_TEMP_DIR", "/var/tmp/auralith")
    monkeypatch.setenv("AURALITH_LOG_LEVEL", "debug")

    settings = AppSettings.from_env()

    assert settings.max_concurrency == 3
    assert str(settings.temp_dir) == "/var/tmp/auralith"
    assert settings.log_level == "DEBUG"


def test_settings_reject_invalid_positive_integer(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AURALITH_MAX_INPUT_BYTES", "0")

    with pytest.raises(ConfigurationError):
        AppSettings.from_env()


def test_settings_reject_invalid_log_level(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AURALITH_LOG_LEVEL", "TRACE")

    with pytest.raises(ConfigurationError):
        AppSettings.from_env()


def test_domain_errors_share_application_base() -> None:
    assert issubclass(ConfigurationError, AuralithError)
    assert issubclass(InvalidAudioError, AuralithError)