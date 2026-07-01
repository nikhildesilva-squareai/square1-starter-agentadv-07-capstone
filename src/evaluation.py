"""Evaluation harness for the enterprise agent system."""

from dataclasses import dataclass

from .system import AgentSystem


@dataclass
class EvaluationMetrics:
    """Metrics from evaluating the agent system."""
    total_cases: int
    passed: int
    failed: int
    avg_confidence: float
    avg_latency_ms: float
    pass_rate: float


def evaluate_system(system: AgentSystem, test_cases: list[dict]) -> EvaluationMetrics:
    """Evaluate the agent system against a set of test cases.

    Runs each test case through the system and computes aggregate
    performance metrics.

    Args:
        system: The AgentSystem to evaluate.
        test_cases: List of dicts with 'input' and optionally 'expected' keys.

    Returns:
        EvaluationMetrics summarising system performance.
    """
    raise NotImplementedError("TODO: implement system evaluation harness")
