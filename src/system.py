"""Core enterprise agent system."""

from dataclasses import dataclass

from .config import SystemConfig


@dataclass
class AgentResponse:
    """Structured response from the agent system."""
    answer: str
    confidence: float
    sources: list[str]
    trace_id: str | None = None
    metadata: dict | None = None


class AgentSystem:
    """Production-grade enterprise agent system.

    Integrates retrieval, routing, security, multi-agent coordination,
    evaluation, and observability into a unified system.
    """

    def __init__(self, config: SystemConfig):
        """Initialise the agent system from configuration.

        Args:
            config: System configuration.
        """
        self.config = config

    def process_request(self, request: str) -> AgentResponse:
        """Process a user request through the full agent pipeline.

        This is the main entry point. The learner designs the internal
        architecture — routing, retrieval, security checks, agent
        orchestration, and observability are all fair game.

        Args:
            request: The user's natural-language request.

        Returns:
            An AgentResponse with the answer and metadata.
        """
        raise NotImplementedError("TODO: implement the enterprise agent pipeline")


if __name__ == "__main__":
    config = SystemConfig()
    system = AgentSystem(config)
    response = system.process_request("Hello, world!")
    print(response)
