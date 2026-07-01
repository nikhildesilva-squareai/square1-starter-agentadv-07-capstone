"""Contract tests for the Enterprise Agent System capstone."""

import pytest

from src.config import SystemConfig
from src.system import AgentSystem, AgentResponse
from src.evaluation import evaluate_system, EvaluationMetrics


class TestSystemInit:
    """System must initialise correctly from config."""

    def test_system_initializes_from_config(self):
        config = SystemConfig(
            api_key="test-key",
            model="claude-sonnet-4-20250514",
            enable_tracing=True,
            enable_security=True,
        )
        system = AgentSystem(config)

        assert system.config.api_key == "test-key"
        assert system.config.enable_tracing is True
        assert system.config.enable_security is True


class TestProcessRequest:
    """process_request must return a structured AgentResponse."""

    def test_process_request_returns_structured_response(self):
        config = SystemConfig()
        system = AgentSystem(config)

        response = system.process_request("What is prompt engineering?")

        assert isinstance(response, AgentResponse), "Must return AgentResponse"
        assert isinstance(response.answer, str), "Answer must be a string"
        assert len(response.answer) > 0, "Answer must not be empty"
        assert 0.0 <= response.confidence <= 1.0, "Confidence must be 0-1"


class TestEvaluation:
    """Evaluation must produce aggregate metrics."""

    def test_evaluation_produces_metrics(self):
        config = SystemConfig()
        system = AgentSystem(config)

        test_cases = [
            {"input": "What is AI?", "expected": "Artificial Intelligence"},
            {"input": "What is ML?", "expected": "Machine Learning"},
        ]

        metrics = evaluate_system(system, test_cases)

        assert isinstance(metrics, EvaluationMetrics), "Must return EvaluationMetrics"
        assert metrics.total_cases == 2, "Must count all test cases"
        assert 0.0 <= metrics.pass_rate <= 1.0, "Pass rate must be 0-1"
