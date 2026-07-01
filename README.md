# Capstone: Enterprise Agent System — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · LLM Agent Architect Advanced · Project 7.**

🤖 **Agent project.** This repo provides the project scaffold, function stubs, and contract tests. Read the full brief on Square 1 for guidance.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# P7: Capstone — Enterprise Agent System

Design and build a production-grade enterprise agent system that integrates concepts from all prior projects: retrieval, routing, security, multi-agent coordination, evaluation, and observability.

This is an open-ended capstone. The starter provides a minimal scaffold — you design and build the architecture.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # Add your ANTHROPIC_API_KEY
```

## Usage

```bash
python -m src.system
```

## Running Tests

```bash
pytest tests/ -v
```

## Project Structure

```
src/
  system.py      — Core agent system entry point
  config.py      — System configuration
  evaluation.py  — System evaluation harness
tests/
  test_system.py — Contract tests
```
