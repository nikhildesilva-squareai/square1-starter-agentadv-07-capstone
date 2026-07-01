"""System configuration for the Enterprise Agent System."""

from dataclasses import dataclass, field


@dataclass
class SystemConfig:
    """Configuration for the enterprise agent system.

    Learners should extend this with their own configuration fields
    as they build out their system architecture.
    """
    api_key: str | None = None
    model: str = "claude-sonnet-4-20250514"
    max_retries: int = 3
    timeout_seconds: float = 30.0
    enable_tracing: bool = True
    enable_security: bool = True
    custom_settings: dict = field(default_factory=dict)

    @classmethod
    def from_env(cls) -> "SystemConfig":
        """Load configuration from environment variables.

        Returns:
            A SystemConfig populated from the environment.
        """
        raise NotImplementedError("TODO: implement environment-based config loading")
